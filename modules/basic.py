"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 15/02/2023
"""
import sys
import os
import time
import shutil
import platform

def sprint(text):
    for i in str(text) + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.1)


def DataBaseCreatorCleaner(basedir, app, db, dir=False):
    if dir:
        try:
            os.makedirs(os.path.join(basedir, "database"), exist_ok=True)
            os.remove(os.path.join(basedir, "database", "database.db"))
        except Exception:
            pass

    app.app_context().push()
    db.drop_all()
    db.create_all()

    return 'DataBase Created'

def log_clear(path):
    try:
        shutil.rmtree(path)
    except Exception:
        pass

    try:
        os.makedirs(path, exist_ok=True)
    except Exception:
        pass

    return 'Log Cleared'

def path(x):
    Operating_System = platform.system().lower()
    if Operating_System == 'windows':
        y = "\\"[0]
        path = f"{y}".join(str(x).split(y)[:-1])
    else:
        y = "/"
        path = f"{y}".join(str(x).split(y)[:-1])

    return path
