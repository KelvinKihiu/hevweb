call pip uninstall hevweb
call cd package
call setup.py sdist
call cd dist
call pip install hevweb-1.0.0.tar.gz