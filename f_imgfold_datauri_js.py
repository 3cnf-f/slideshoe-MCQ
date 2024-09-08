from datauri import DataURI
from f_logging import f_initLog
from f_logging import f_log as f_l
import f_retIMG

# png_uri=DataURI.from_file('Axelfall-MR240430-CorT20000.png')
# print(str(png_uri))

f_initLog()

# def f_FOLDERdotSerialAppend(in_folder,in_appendfile):
#     folder_img_list=f_retIMG.f_allimg_thisfolder(in_folder)
#     f_l(folder_img_list)
#     f=open(in_appendfile,'a')
#     f.write('const '+in_folder+' = {')
#     for i,this_image in enumerate(folder_img_list):
#         f_l(str(i)+' : '+this_image)
#         png_uri=DataURI.from_file(this_image)
#         f.write('image'+str(i)+': \''+str(png_uri)+'\', \n')
#         f_l('image'+str(i)+': \'-datauriremoved-\', ')
#     f.write('}')
#     f.close()

def f_imgFl_PathNnames(in_path):
    f_out=listdir(in_path)
    f_out.sort()
    ex_dirs, ex_files= f_retIMG.f_retDirsFiles(f_out)
    f_l(ex_dirs)

# f_FOLDERdotSerialAppend('CorT2','dumpit.txt')
f_imgFl_PathNnames('../../cases/test_axel')