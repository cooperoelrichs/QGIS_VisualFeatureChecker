# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VisualFeatureChecker
                                 A QGIS plugin
 test
                             -------------------
        begin                : 2014-10-24
        copyright            : (C) 2014 by me
        email                : me
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load VisualFeatureChecker class from file VisualFeatureChecker
    from visualfeaturechecker import VisualFeatureChecker
    return VisualFeatureChecker(iface)
