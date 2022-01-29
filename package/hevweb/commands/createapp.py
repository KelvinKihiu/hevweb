"""
createapp command
"""

import os

from hevweb.commands.base import Base
from distutils.dir_util import copy_tree

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class CreateApp(Base):
    def run(self):
        if not self.args:
            print("The application name is required.")
        else:
            appname = self.args[0]
            self.createapp(appname)


    def createapp(self, appname):
        print("Generating your application...")
        #get current directory
        proj_dir = os.path.join(os.getcwd(), appname.lower())
        if os.path.exists(proj_dir):
            print("Project already exists")
        else:
            os.mkdir(proj_dir)

            from_dir = os.path.join(APP_DIR, 'bootstrapper')

            copy_tree(from_dir, proj_dir)

            #models
            models_dir = os.path.join(proj_dir, 'models')
            os.mkdir(models_dir)
            open(os.path.join(models_dir, '__init__.py'), 'wt')
            
            old_name = 'APPLICATION_NAME'
            config_file = os.path.join(proj_dir, 'manage', 'config.py')
            with open(config_file) as f:
                s = f.read()
                if old_name not in s:
                    return
                    
            with open(config_file, 'w') as f:
                s = s.replace(old_name, appname)
                f.write(s)

            index_file = os.path.join(proj_dir, 'views', 'layout.html')
            with open(index_file) as f:
                s = f.read()
                if old_name not in s:
                    return
                    
            with open(index_file, 'w') as f:
                s = s.replace(old_name, appname)
                f.write(s)

            file_to_remove = os.path.join(proj_dir, '__init__.py')
            if os.path.isfile(file_to_remove):
                os.remove(file_to_remove)

        print("Application created successfully")