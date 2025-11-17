# QGIS Backup Plugin / Wtyczka Backup Projektu

[EN] QGIS plugin creates timestamped backups of QGIS project file with Memory Layer Saver plugin support<br>
[PL] wtyczka do QGIS tworzy kopie zapasowe projektów QGIS ze znacznikiem czasowym i wsparciem wtyczki Memory Layer Saver

[![QGIS](https://img.shields.io/badge/QGIS-3.4+-green.svg)](https://qgis.org)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Version](https://img.shields.io/badge/version-1.0-orange.svg)](https://github.com/MAPYMAPY/qgis-backup-plugin/releases)

[🇬🇧 English](#english) | [🇵🇱 Polski](#polski)

---

## English

### 📋 Description

A QGIS plugin that creates timestamped backups of your projects with optional Memory Layer Saver integration. Never lose your work again!

### ✨ Features

- **Automatic timestamped backups** - Creates copies in `_backups` subfolder with format: `PROJECT_NAME (backup YYYY-MM-DD HH.MM.SS).qgz`
- **One-click backup** - Toolbar button for instant project backup
- **Auto-save** - Automatically saves project before creating backup
- **Memory Layer Saver integration** - Optional support for temporary layers
- **.mldata backup** - Copies associated Memory Layer Saver data files
- **Bilingual interface** - Full support for Polish and English
- **Configurable options** - Customize backup behavior in settings

### 📦 Installation

#### From QGIS Plugin Repository (Recommended)

1. Open QGIS
2. Go to `Plugins` → `Manage and Install Plugins`
3. Search for "BackupProjektu" or "Backup"
4. Click `Install Plugin`

#### Manual Installation

**Method 1: Install from ZIP (Recommended)**

1. Download the latest release ZIP from [Releases](https://github.com/MAPYMAPY/qgis-backup-plugin/releases)
2. Open QGIS
3. Go to `Plugins` → `Manage and Install Plugins`
4. Click `Install from ZIP`
5. Select the downloaded `BackupProjektu.zip` file
6. Click `Install Plugin`

**Method 2: Manual extraction**

1. Download the latest release ZIP from [Releases](https://github.com/MAPYMAPY/qgis-backup-plugin/releases)
2. Extract to your QGIS plugins directory:
   - **Windows**: `C:\Users\USERNAME\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. Restart QGIS
4. Enable the plugin in `Plugins` → `Manage and Install Plugins` → `Installed`

### 🚀 Usage

#### Quick Backup

1. Click the floppy disk icon in the toolbar
2. Backup is created automatically in `_backups` folder

#### Settings

1. Go to `Plugins` → `Archiving` → `Backup Settings...`
2. Configure options:
   - **Use Memory Layer Saver** - Saves temporary layers before backup (requires Memory Layer Saver plugin)
   - **Create copy of .mldata file** - Backs up Memory Layer Saver data file

### 🔧 Requirements

- QGIS 3.4 or higher
- **Optional**: [Memory Layer Saver](https://plugins.qgis.org/plugins/MemoryLayerSaver/) plugin for temporary layers backup

### 📝 Backup File Structure

```
your_project_folder/
├── your_project.qgz                                    # Original project
├── your_project.qgz.mldata                            # Memory layers (if exists)
└── _backups/
    ├── your_project (backup 2025-11-16 14.30.45).qgz
    ├── your_project (backup 2025-11-16 14.30.45).qgz.mldata
    ├── your_project (backup 2025-11-16 15.22.10).qgz
    └── your_project (backup 2025-11-16 15.22.10).qgz.mldata
```

### 🐛 Bug Reports & Feature Requests

Found a bug or have an idea? Please [open an issue](https://github.com/MAPYMAPY/qgis-backup-plugin/issues).

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/MAPYMAPY/QGIS-BackupProjektu/blob/main/LICENSE) file for details.

### 👤 Author

**Artur Otremba**

### 🙏 Acknowledgments

- Memory Layer Saver plugin authors

## ⚠️ Disclaimer

This plugin is provided "as is" under GPL-3.0 license. 
While it has been tested, users should:
- Test backups before relying on them
- Keep multiple backup copies
- Verify backup integrity regularly

This is a convenience tool, not a professional backup solution.
The author is not responsible for any data loss or damages.

---

## Polski

### 📋 Opis

Wtyczka QGIS do tworzenia kopii zapasowych pliku projektu ze znacznikiem czasowym z opcjonalną integracją z Memory Layer Saver. Nigdy więcej nie stracisz swojej pracy!

### ✨ Funkcje

- **Automatyczne kopie ze znacznikiem czasowym** - Tworzy kopie w podkatalogu `_backups` w formacie: `NAZWA_PROJEKTU (backup RRRR-MM-DD GG.MM.SS).qgz`
- **Backup jednym kliknięciem** - Przycisk na pasku narzędzi do natychmiastowej kopii
- **Autozapis** - Automatycznie zapisuje projekt przed utworzeniem backupu
- **Integracja z Memory Layer Saver** - Opcjonalne wsparcie dla warstw tymczasowych
- **Backup .mldata** - Kopiuje powiązane pliki danych Memory Layer Saver
- **Interfejs dwujęzyczny** - Pełne wsparcie dla języka polskiego i angielskiego
- **Konfigurowalne opcje** - Dostosuj zachowanie backupu w ustawieniach

### 📦 Instalacja

#### Z Repozytorium Wtyczek QGIS (Zalecane)

1. Otwórz QGIS
2. Przejdź do `Wtyczki` → `Zarządzaj wtyczkami i instaluj`
3. Wyszukaj "BackupProjektu" lub "Backup"
4. Kliknij `Zainstaluj wtyczkę`

#### Instalacja ręczna

**Metoda 1: Instalacja z pliku ZIP (Zalecane)**

1. Pobierz najnowszą wersję ZIP z [Releases](https://github.com/MAPYMAPY/qgis-backup-plugin/releases)
2. Otwórz QGIS
3. Przejdź do `Wtyczki` → `Zarządzaj wtyczkami i instaluj`
4. Kliknij `Instaluj z pliku ZIP`
5. Wybierz pobrany plik `BackupProjektu.zip`
6. Kliknij `Zainstaluj wtyczkę`

**Metoda 2: Ręczna rozpakowanie**

1. Pobierz najnowszą wersję ZIP z [Releases](https://github.com/MAPYMAPY/qgis-backup-plugin/releases)
2. Rozpakuj do katalogu wtyczek QGIS:
   - **Windows**: `C:\Users\NAZWA_UŻYTKOWNIKA\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. Uruchom ponownie QGIS
4. Włącz wtyczkę w `Wtyczki` → `Zarządzaj wtyczkami i instaluj` → `Zainstalowane`

### 🚀 Użytkowanie

#### Szybki backup

1. Kliknij ikonę dyskietki na pasku narzędzi
2. Backup zostanie utworzony automatycznie w folderze `_backups`

#### Ustawienia

1. Przejdź do `Wtyczki` → `Archiwizacja` → `Ustawienia backupu...`
2. Skonfiguruj opcje:
   - **Użyj Memory Layer Saver** - Zapisuje warstwy tymczasowe przed backupem (wymaga wtyczki Memory Layer Saver)
   - **Utwórz kopię pliku .mldata** - Tworzy kopię zapasową pliku danych Memory Layer Saver

### 🔧 Wymagania

- QGIS 3.4 lub wyższy
- **Opcjonalnie**: Wtyczka [Memory Layer Saver](https://plugins.qgis.org/plugins/MemoryLayerSaver/) dla backupu warstw tymczasowych

### 📝 Struktura plików backupu

```
folder_twojego_projektu/
├── twoj_projekt.qgz                                    # Oryginalny projekt
├── twoj_projekt.qgz.mldata                            # Warstwy tymczasowe (jeśli istnieją)
└── _backups/
    ├── twoj_projekt (backup 2025-11-16 14.30.45).qgz
    ├── twoj_projekt (backup 2025-11-16 14.30.45).qgz.mldata
    ├── twoj_projekt (backup 2025-11-16 15.22.10).qgz
    └── twoj_projekt (backup 2025-11-16 15.22.10).qgz.mldata
```

### 🐛 Zgłaszanie błędów i propozycje funkcji

Znalazłeś błąd lub masz pomysł? Proszę [otwórz issue](https://github.com/MAPYMAPY/qgis-backup-plugin/issues).

### 🤝 Współpraca

Wkład w rozwój projektu jest mile widziany! Zapraszam do zgłaszania Pull Requestów.

### 📄 Licencja

Ten projekt jest licencjonowany na zasadach GNU General Public License v3.0 - szczegóły w pliku [LICENSE](https://github.com/MAPYMAPY/QGIS-BackupProjektu/blob/main/LICENSE).

### 👤 Autor

**Artur Otremba**

### 🙏 Podziękowania

- Autorzy wtyczki Memory Layer Saver

## ⚠️ Zastrzeżenie

Wtyczka jest dostarczana "w stanie, w jakim jest" na licencji GPL-3.0.
Mimo że została przetestowana, użytkownicy powinni:
- Testować kopie zapasowe przed poleganiem na nich
- Zachowywać wiele kopii zapasowych
- Regularnie weryfikować integralność kopii zapasowych

To narzędzie ułatwiające pracę, a nie profesjonalne rozwiązanie do backupu.
Autor nie ponosi odpowiedzialności za utratę danych lub szkody.

---

## 📊 Changelog

### Version 1.0 (2025-11-16)
- Initial release
- Timestamped project backups
- Memory Layer Saver integration
- Bilingual interface (Polish/English)
- Configurable backup options
