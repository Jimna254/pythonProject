# Files and Directories
from pathlib import Path
path = Path()
#path = Path('Automations')

def filefinder():
 for file in (path.glob('*')):
    print(file)

filefinder()
#path.mkdir()
  