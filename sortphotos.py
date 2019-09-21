from datetime import datetime
from os import listdir, rename
from os.path import isfile, join
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path

def get_dir(time):
    return join('.', str(time.year), time.strftime('%m'))

def get_info(image):
    info = image._getexif()
    ret = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value

    return ret

def main():
    files = [f for f in listdir('.') if isfile(join('.', f))]
    for file in files:
        try:
            info = get_info(Image.open(file))
            if ('DateTime' in info):
                time = datetime.strptime(info['DateTime'], '%Y:%m:%d %H:%M:%S')
                targetDir = get_dir(time)
                Path(targetDir).mkdir(parents=True, exist_ok=True)
                dest = join(targetDir, file)
                rename(file, dest)
        except:
            pass
            
if __name__ == "__main__":
    main()
