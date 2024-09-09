from datauri import DataURI
from f_logging import f_initLog
from f_logging import f_log as f_l
import f_retIMG
from os import getcwd, path, listdir

# png_uri=DataURI.from_file('Axelfall-MR240430-CorT20000.png')
# print(str(png_uri))

f_initLog()

def f_foldername(ins_path):
    slash_array=ins_path.rsplit('/')
    foldername=slash_array[-1]
    return foldername


def f_FOLDERdotSerialAppend(in_folder,in_appendfile):
    folder_img_list=f_retIMG.f_allimg_thisfolder(in_folder)
    f_l(folder_img_list)
    f=open(in_appendfile,'a')
    f.write('{')
    f.write('name: \"'+f_foldername(in_folder)+'\", \n')
    for i,this_image in enumerate(folder_img_list):
        f_l(str(i)+' : '+this_image)
        png_uri=DataURI.from_file(this_image)
        f.write('image'+str(i)+': \''+str(png_uri)+'\', \n')
        f_l('image'+str(i)+': \'-datauriremoved-\', ')
    f.write('}, \n \n \n')
    f.close()

def f_imgFl_PathNnames(in_path,my_appendfile):
    f_out=listdir(in_path)
    f_out.sort()
    ex_dirs, ex_files= f_retIMG.f_retDirsFiles(f_out,in_path)
    f_l(ex_dirs)
    for i,thisdir in enumerate(ex_dirs):
        f_l(f_foldername(thisdir))
        f_FOLDERdotSerialAppend(thisdir,my_appendfile)
# f_FOLDERdotSerialAppend('CorT2','dumpit.txt')
f_imgFl_PathNnames('cases/test_axel','boys2poop.txt')