import pyqrcode
import os
import hashlib
import json


def generate_qr_code(link,image_path):
    pyqrcode.create(link).svg(image_path,xmldecl=True)


def iterate_links(lists_of_links):
    output_dir = os.path.join("static","image_links")
    os.makedirs(output_dir,exist_ok=True)
    lists_of_paths = []
    with open("paths.json","r+") as f:
        data = json.load(f)
        for link in lists_of_links:
            filename = f"{data['count']}_{hashlib.md5(link.encode()).hexdigest()}.svg"
            relative_filepath = "image_links/"+filename
            absolute_filepath = os.path.join("static",relative_filepath)
            lists_of_paths.append(relative_filepath)
            data['paths'].append(relative_filepath)
            data['count']+=1
            generate_qr_code(link,absolute_filepath)
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()
    return lists_of_paths

if __name__=="__main__":
    generate_qr_code('https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1#:~:text=Your%20PC%20will%20still%20work,recommend%20moving%20to%20Windows%2011.&text=Virtualization%20lets%20your%20Windows%20device,and%20install%20on%20your%20device.',"qrcode.svg")



