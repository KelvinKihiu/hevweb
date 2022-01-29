pip uninstall hevweb
cd package
python3 setup.py sdist
cd dist
pip install hevweb-1.0.0.tar.gz