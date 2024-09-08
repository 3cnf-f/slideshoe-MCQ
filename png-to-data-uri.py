from datauri import DataURI
import f_retIMG

# png_uri=DataURI.from_file('Axelfall-MR240430-CorT20000.png')
# print(str(png_uri))

def f_FOLDERdotSerialAppend(in_folder,in_appendfile):
    folder_img_list=f_retIMG.f_allimg_thisfolder(in_folder)
    f=open(in_appendfile,'a')
    f.write('const '+in_folder+' = {')
    for i,this_image in enumerate(folder_img_list):
        png_uri=DataURI.from_file(this_image)
        f.write('image'+i+': \''+str(png_uri)+'\', ')
    f.write('}')
    f.close()

f_FOLDERdotSerialAppend('CorT2','dumpit.txt')