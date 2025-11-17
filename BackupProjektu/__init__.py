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

def classFactory(iface):
    from .backup_plugin import BackupPlugin
    return BackupPlugin(iface)
