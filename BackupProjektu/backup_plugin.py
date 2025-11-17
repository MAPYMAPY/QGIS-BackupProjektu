# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BackupProjektu
                                 A QGIS plugin
 Creates timestamped backups of QGIS projects with Memory Layer Saver support
 
 Tworzy kopie zapasowe projektów QGIS ze znacznikiem czasowym z opcjonalną 
 integracją Memory Layer Saver
                              -------------------
        begin                : 2025-11-16
        copyright            : (C) 2025 by Artur Otremba
        email                : kontakt@szkolenia.pro
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""



import os
import shutil
import time
from datetime import datetime

from qgis.PyQt.QtWidgets import (
    QAction,
    QMessageBox,
    QDialog,
    QVBoxLayout,
    QCheckBox,
    QPushButton,
    QLabel,
    QHBoxLayout
)
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QSettings
from qgis.core import QgsProject
from qgis.utils import plugins


# =========================================
# SYSTEM TŁUMACZEŃ
# =========================================
class Translations:
    """Klasa zarządzająca tłumaczeniami PL/EN"""
    
    TEXTS = {
        # Menu i toolbar
        'menu_name': {
            'pl': 'Archiwizacja',
            'en': 'Archiving'
        },
        'action_backup': {
            'pl': 'Backup projektu',
            'en': 'Project Backup'
        },
        'action_settings': {
            'pl': 'Ustawienia backupu…',
            'en': 'Backup Settings…'
        },
        'toolbar_name': {
            'pl': 'Archiwizacja',
            'en': 'Archiving'
        },
        
        # Okno ustawień
        'settings_title': {
            'pl': 'Ustawienia backupu',
            'en': 'Backup Settings'
        },
        'settings_label': {
            'pl': 'Opcje tworzenia kopii zapasowej:',
            'en': 'Backup creation options:'
        },
        'checkbox_mls': {
            'pl': 'Użyj Memory Layer Saver (jeśli dostępny)',
            'en': 'Use Memory Layer Saver (if available)'
        },
        'checkbox_mldata': {
            'pl': 'Utwórz kopię pliku .mldata',
            'en': 'Create copy of .mldata file'
        },
        'btn_save': {
            'pl': 'Zapisz',
            'en': 'Save'
        },
        'btn_cancel': {
            'pl': 'Anuluj',
            'en': 'Cancel'
        },
        
        # Komunikaty - sukces
        'msg_settings_saved': {
            'pl': 'Ustawienia zapisane.',
            'en': 'Settings saved.'
        },
        'msg_creating_backup': {
            'pl': 'Tworzę kopię projektu: {path}',
            'en': 'Creating project backup: {path}'
        },
        'msg_layers_saved': {
            'pl': 'Warstwy zapisane przez Memory Layer Saver.',
            'en': 'Layers saved by Memory Layer Saver.'
        },
        'msg_backup_created': {
            'pl': 'Utworzono kopię: {name}',
            'en': 'Backup created: {name}'
        },
        'msg_mldata_copied': {
            'pl': 'Utworzono kopię .mldata.',
            'en': '.mldata file copied.'
        },
        'msg_mldata_not_copied': {
            'pl': 'Plik .mldata nie został skopiowany.',
            'en': '.mldata file was not copied.'
        },
        
        # Komunikaty - ostrzeżenia
        'warn_no_project': {
            'pl': 'Najpierw zapisz projekt, aby utworzyć backup.',
            'en': 'Please save the project first to create a backup.'
        },
        'warn_mls_inactive': {
            'pl': 'Wtyczka Memory Layer Saver nie jest aktywna.',
            'en': 'Memory Layer Saver plugin is not active.'
        },
        'warn_save_data_error': {
            'pl': 'save_data() zgłosiło wyjątek: {error}',
            'en': 'save_data() raised exception: {error}'
        },
        'warn_mldata_copy_failed': {
            'pl': 'Nie udało się skopiować .mldata: {error}',
            'en': 'Failed to copy .mldata: {error}'
        },
        
        # Komunikaty - błędy
        'error_title': {
            'pl': 'Brak projektu',
            'en': 'No Project'
        },
        'error_backup_failed': {
            'pl': 'Błąd backupu',
            'en': 'Backup Error'
        },
        'error_occurred': {
            'pl': 'Wystąpił błąd: {error}',
            'en': 'An error occurred: {error}'
        },
        'error_save_failed': {
            'pl': 'Nie udało się zapisać projektu.',
            'en': 'Failed to save project.'
        },
        'error_generic': {
            'pl': 'Błąd',
            'en': 'Error'
        },
        
        # Nagłówki sekcji (dla messageBar)
        'header_backup': {
            'pl': 'Backup',
            'en': 'Backup'
        }
    }
    
    def __init__(self):
        """Inicjalizacja - automatyczne wykrycie języka z ustawień QGIS"""
        settings = QSettings()
        locale = settings.value('locale/userLocale', 'en_US')
        
        # Wykryj język (bierzemy pierwsze 2 znaki, np. 'pl' z 'pl_PL')
        self.current_lang = locale[:2].lower() if locale else 'en'
        
        # Jeśli język nie jest polski, użyj angielskiego
        if self.current_lang not in ['pl', 'en']:
            self.current_lang = 'en'
    
    def get(self, key, **kwargs):
        """
        Pobiera tłumaczenie dla danego klucza
        
        Args:
            key: klucz tłumaczenia
            **kwargs: parametry do formatowania (np. {path}, {error})
        
        Returns:
            Przetłumaczony i sformatowany tekst
        """
        if key not in self.TEXTS:
            return f"[MISSING: {key}]"
        
        text = self.TEXTS[key].get(self.current_lang, self.TEXTS[key].get('en', key))
        
        # Formatowanie z parametrami
        if kwargs:
            try:
                text = text.format(**kwargs)
            except KeyError:
                pass
        
        return text
    
    def get_lang(self):
        """Zwraca aktualny język (pl lub en)"""
        return self.current_lang


# Globalna instancja tłumaczeń
tr = Translations()


# =========================================
# OKNO USTAWIEŃ
# =========================================
class BackupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QSettings()

        self.setWindowTitle(tr.get('settings_title'))
        self.setMinimumWidth(320)

        layout = QVBoxLayout(self)

        lbl = QLabel(tr.get('settings_label'))
        layout.addWidget(lbl)

        # Wczytywanie ustawień
        self.use_mls = QCheckBox(tr.get('checkbox_mls'))
        self.use_mls.setChecked(self.settings.value("backup/use_mls", True, bool))
        layout.addWidget(self.use_mls)

        self.copy_mldata = QCheckBox(tr.get('checkbox_mldata'))
        self.copy_mldata.setChecked(self.settings.value("backup/copy_mldata", True, bool))
        layout.addWidget(self.copy_mldata)

        # Przyciski
        h = QHBoxLayout()
        ok_btn = QPushButton(tr.get('btn_save'))
        cancel_btn = QPushButton(tr.get('btn_cancel'))
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        h.addWidget(ok_btn)
        h.addWidget(cancel_btn)
        layout.addLayout(h)

    def save_settings(self):
        self.settings.setValue("backup/use_mls", self.use_mls.isChecked())
        self.settings.setValue("backup/copy_mldata", self.copy_mldata.isChecked())


# =========================================
# GŁÓWNY PLUGIN
# =========================================
class BackupPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.toolbar = None
        self.action = None
        self.settings_action = None

    # =========================================
    # INICJALIZACJA GUI
    # =========================================
    def initGui(self):

        # Ścieżka do ikony dyskietki
        icon_path = os.path.join(os.path.dirname(__file__), "icons", "backup_floppy.png")
        icon = QIcon(icon_path)

        # Akcja backupu – uruchamiana bez okna
        self.action = QAction(icon, tr.get('action_backup'), self.iface.mainWindow())
        self.action.triggered.connect(self.run_backup_with_saved_settings)

        # Własny pasek narzędzi
        self.toolbar = self.iface.addToolBar(tr.get('toolbar_name'))
        self.toolbar.setObjectName("Archiwizacja_Toolbar")
        self.toolbar.addAction(self.action)

        # Akcja ustawień
        self.settings_action = QAction(tr.get('action_settings'), self.iface.mainWindow())
        self.settings_action.triggered.connect(self.show_settings_dialog)

        # Menu
        menu_name = f"&{tr.get('menu_name')}"
        self.iface.addPluginToMenu(menu_name, self.action)
        self.iface.addPluginToMenu(menu_name, self.settings_action)

    # =========================================
    # USUWANIE GUI
    # =========================================
    def unload(self):
        menu_name = f"&{tr.get('menu_name')}"
        if self.toolbar:
            self.iface.mainWindow().removeToolBar(self.toolbar)
        if self.action:
            self.iface.removePluginMenu(menu_name, self.action)
        if self.settings_action:
            self.iface.removePluginMenu(menu_name, self.settings_action)

    # =========================================
    # OKNO USTAWIEŃ
    # =========================================
    def show_settings_dialog(self):
        dlg = BackupDialog(self.iface.mainWindow())
        if dlg.exec_() == QDialog.Accepted:
            dlg.save_settings()
            self.iface.messageBar().pushSuccess(
                tr.get('header_backup'), 
                tr.get('msg_settings_saved')
            )

    # =========================================
    # BACKUP WG ZAPISANYCH USTAWIEŃ
    # =========================================
    def run_backup_with_saved_settings(self):
        settings = QSettings()
        use_mls = settings.value("backup/use_mls", True, bool)
        copy_mldata = settings.value("backup/copy_mldata", True, bool)

        try:
            self.create_backup(use_mls=use_mls, backup_mldata=copy_mldata)
        except Exception as e:
            QMessageBox.critical(
                None, 
                tr.get('error_backup_failed'), 
                tr.get('error_occurred', error=str(e))
            )

    # =========================================
    # WYSZUKIWANIE .mldata
    # =========================================
    def _find_mldata_path(self, project_path, feedback, mls_plugin=None, wait_seconds=5):
        candidates = [
            project_path + ".mldata",
            os.path.splitext(project_path)[0] + ".mldata"
        ]

        # Memory Layer Saver – jeśli ma własną ścieżkę
        if mls_plugin:
            try:
                func = getattr(mls_plugin, "memory_layer_file", None)
                if callable(func):
                    p = func()
                    if p:
                        if not os.path.isabs(p):
                            p = os.path.join(os.path.dirname(project_path), p)
                        candidates.insert(0, p)
            except Exception:
                pass

        # Usunięcie duplikatów
        unique_candidates = []
        seen = set()
        for c in candidates:
            if c not in seen:
                unique_candidates.append(c)
                seen.add(c)

        # Oczekiwanie na zapis pliku .mldata
        waited = 0
        while waited < wait_seconds:
            for c in unique_candidates:
                if os.path.exists(c):
                    return c
            time.sleep(0.2)
            waited += 0.2

        return None

    # =========================================
    # GŁÓWNY MECHANIZM BACKUPU
    # =========================================
    def create_backup(self, use_mls=True, backup_mldata=True):

        project = QgsProject.instance()
        project_path = project.fileName()

        if not project_path:
            QMessageBox.warning(
                None, 
                tr.get('error_title'),
                tr.get('warn_no_project')
            )
            return

        self.iface.messageBar().pushInfo(
            tr.get('header_backup'), 
            tr.get('msg_creating_backup', path=project_path)
        )

        # Memory Layer Saver
        mls_plugin = None
        if use_mls:
            mls_plugin = plugins.get("MemoryLayerSaver", None)
            if not mls_plugin:
                self.iface.messageBar().pushWarning(
                    tr.get('header_backup'),
                    tr.get('warn_mls_inactive')
                )

        # wymuszenie zapisu MLS
        if mls_plugin:
            try:
                if hasattr(mls_plugin, "has_modified_layers"):
                    mls_plugin.has_modified_layers = True
            except Exception:
                pass

            try:
                if hasattr(mls_plugin, "save_data"):
                    mls_plugin.save_data()
                    time.sleep(0.3)
                    self.iface.messageBar().pushInfo(
                        tr.get('header_backup'),
                        tr.get('msg_layers_saved')
                    )
            except Exception as e:
                self.iface.messageBar().pushWarning(
                    tr.get('header_backup'), 
                    tr.get('warn_save_data_error', error=str(e))
                )

        # zapis projektu
        project.setDirty(True)
        if not project.write():
            QMessageBox.critical(
                None, 
                tr.get('error_generic'), 
                tr.get('error_save_failed')
            )
            return

        # chwila na dokończenie zapisu
        time.sleep(0.6)

        project_dir = os.path.dirname(project_path)
        project_name = os.path.splitext(os.path.basename(project_path))[0]

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H.%M.%S")

        backup_base = f"{project_name} (backup {date_str} {time_str})"
        backups_dir = os.path.join(project_dir, "_backups")
        os.makedirs(backups_dir, exist_ok=True)

        # kopia projektu
        backup_project = os.path.join(backups_dir, f"{backup_base}.qgz")
        shutil.copy2(project_path, backup_project)

        # kopia .mldata
        copied_mldata = False
        if backup_mldata:
            mldata_path = self._find_mldata_path(project_path, None, mls_plugin)
            if mldata_path:
                dest = backup_project + ".mldata"
                try:
                    shutil.copy2(mldata_path, dest)
                    copied_mldata = True
                except Exception as e:
                    self.iface.messageBar().pushWarning(
                        tr.get('header_backup'), 
                        tr.get('warn_mldata_copy_failed', error=str(e))
                    )

        # podsumowanie
        summary = [tr.get('msg_backup_created', name=os.path.basename(backup_project))]
        if backup_mldata:
            summary.append(
                tr.get('msg_mldata_copied') if copied_mldata else
                tr.get('msg_mldata_not_copied')
            )

        self.iface.messageBar().pushSuccess(tr.get('header_backup'), "\n".join(summary))