#!/usr/bin/python
# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2015 vagnum08
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import gtk
from subprocess import call, check_call

from pywb import Btsync
# from token_read import init, get_folders
import sys
import btsync_lib as bt

if sys.platform == 'darwin':
    def openFolder(path):
        check_call(['open',  path])
elif sys.platform == 'linux2':
    def openFolder(path):
        check_call(['xdg-open',  path])
elif sys.platform == 'win32':
    def openFolder(path):
        check_call(['explorer', path])

class SystrayIconApp:
    def __init__(self, client):
        self.tray = gtk.StatusIcon()
        self.tray.set_from_stock(gtk.STOCK_ABOUT)
        self.tray.set_from_file('btsync.png')
        self.tray.connect('popup-menu', self.on_right_click)
        self.tray.set_tooltip(('BtSync 2.0'))
        self.btclient = client
        self.f_list = self.btclient.sync_folders

    def on_right_click(self, icon, event_button, event_time):
        self.make_menu(event_button, event_time)

    def make_menu(self, event_button, event_time):
        menu = gtk.Menu()

        # show about dialog
        about = gtk.MenuItem("About")
        about.show()
        menu.append(about)
        about.connect('activate', self.show_about_dialog)

        # add quit item
        quit = gtk.MenuItem("Quit")
        quit.show()
        menu.append(quit)
        quit.connect('activate', self.exit)

        # add btsync item
        bt = gtk.MenuItem("Open BtSync GUI")
        bt.show()
        menu.append(bt)
        bt.connect('activate', self.show_bt)

        # add foldermenu item
        # add foldersubmenu item
        folder_menu = gtk.Menu()

        for f in self.f_list:
            mi = gtk.MenuItem(f['name'])
            folder_menu.append(mi)
            mi.show()
            mi.connect('activate', self.open_folder, f['path'])

        folder_menu.show()

        sf = gtk.MenuItem("Synced Folders")
        sf.set_submenu(folder_menu)
        sf.show()
        menu.append(sf)
        # bt.connect('activate', self.show_bt)

        menu.popup(None, None, gtk.status_icon_position_menu,
                    event_button, event_time, self.tray)

    def show_about_dialog(self, widget):
        about_dialog = gtk.AboutDialog()
        about_dialog.set_destroy_with_parent (True)
        # about_dialog.set_icon_name ("SystrayIcon")
        about_dialog.set_icon_from_file("favicon.ico")
        about_dialog.set_name('Btsync Python GUI')
        about_dialog.set_version('0.1')
        about_dialog.set_copyright("(C) 2015 vagnum08")
        about_dialog.set_comments(("Python gui with systray for btsync 2.0"))
        about_dialog.set_authors(['vagnum08 <vagnum08@gmail.com>'])
        about_dialog.run()
        about_dialog.destroy()

    def exit(self, menu):
        call(["killall", "btsync"])
        gtk.main_quit(menu)

    def show_bt(self, widget):
        Btsync()

    def open_folder(self,widget, fpath):
        openFolder(fpath)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit('Usage: python %s username password' % sys.argv[0])
    call(["./btsync"])
    client = bt.Client(host='127.0.0.1',
                       port='8888',
                       username=sys.argv[1],
                       password=sys.argv[2])

    SystrayIconApp(client)
    gtk.main()
