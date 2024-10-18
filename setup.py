from distutils.core import setup
import py2exe

setup(
    windows=['2fa.py'],  # Change to 'windows=['my_script.py']' if you want a windowed app
    options={
        'py2exe': {
            'bundle_files': 1,  # Bundle everything into a single executable
            'compressed': True,  # Compress the executable
            'optimize': 2,       # Optimize bytecode
            'includes': ["sqlite3","PyQt5","bcrypt"],      # Any additional modules to include
        }
    },
    zipfile=None,  # No separate zipfile
    data_files=[("", ["resources/icon.ico"])],  # Path to your icon file
)
