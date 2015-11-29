#!/usr/bin/env python
import gtk, webkit
import subprocess
import sys


if sys.platform == 'darwin':
    def openFolder(path):
        subprocess.check_call(['open',  path])
elif sys.platform == 'linux2':
    def openFolder(path):
        subprocess.check_call(['xdg-open',  path])
elif sys.platform == 'win32':
    def openFolder(path):
        subprocess.check_call(['explorer', path])


class Btsync():

    def __init__(self):
        # Create window
        self.window = gtk.Window()
        self.window.set_icon_from_file('btsync.png')
        self.window.connect('destroy', lambda w: gtk.main_quit())
        self.window.set_default_size(800, 600)

        # Create view for webpage
        self.view = gtk.ScrolledWindow()
        self.webview = webkit.WebView()
        self.webview.open('https://localhost:8888/gui/')
        self.webview.connect('title-changed', self.change_title)
        self.webview.connect('load-committed', self.change_url)
        self.webview.connect("navigation-policy-decision-requested", self.check)
        self.webview. connect("load-finished", self.load_finished)
        self.view.add(self.webview)

        # Add everything and initialize
        self.container = gtk.VBox()
        self.container.pack_start(self.view)

        self.window.add(self.container)
        self.window.show_all()
        gtk.main()


    def check(self, view, frame, req, nav, policy):
        #webkit_web_policy_decision_ignore(TRUE)
       uri=req.get_uri()
       print "request to go to %s" % uri
       openFolder(uri[7:])
       return 1

    def load_finished(self, webview, frame):
        print "in"
        gtk.timeout_add(1*1000, self.my_timer) # call every min
        # self.webview.execute_script(js)

    def my_timer(self, *args):
        print " in timer"
        js = '''
                $(".nameLabel").click(function() {{
                            var elm = this.text
                            $(app.folders.models).each( function( key, value ) {{
                                if (elm==value.attributes.name) {{
                                // alert("Same value", value.attributes.name);
                                //alert('<a href="file://'+value.attributes.path+'">open folder</a>');
                               // if (window.confirm('If you click "ok" you would be redirected . Cancel will load this website '))
                                   // {{
                            //window.location.href='https://www.google.com/chrome/browser/index.html';
                //}};
                                //window.open("file://"+value.attributes.path);
                               window.location.href = "https://"+value.attributes.path;
                                }}
                            }});
                        }});
                '''
        self.webview.execute_script(js)
        return False# do ur work here, but not for long

    def load_page(self, widget):
        so_add = self.wow_address_bar.get_text()
        if so_add.startswith('http://') or so_add.startswith('https://'):
            self.webview.open(so_add)
        else:
            so_add = 'http://' + so_add
            self.wow_address_bar.set_text(so_add)
            self.webview.open(so_add)

    def change_title(self, widget, frame, title):
        self.window.set_title('Btsync UI' + title)

    def change_url(self, widget, frame):
        uri = frame.get_uri()




#call(["./btsync"])
# web_browser = Btsync()
