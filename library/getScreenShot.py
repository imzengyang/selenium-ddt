import os

def getRootPath():
    rootpath = os.path.dirname(os.path.abspath(__file__))
    while rootpath:
        if os.path.exists(os.path.join(rootpath, 'readme.md')):
            break
        rootpath = rootpath[0:rootpath.rfind(os.path.sep)]

    return rootpath

def getScreenShotsPath():
    rootPath = getRootPath()
    screenshotpath = os.path.join(rootPath, "screenshots")
    if not os.path.exists(screenshotpath):
        os.makedirs(screenshotpath)
    return screenshotpath

    