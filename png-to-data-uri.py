from datauri import DataURI
from f_logging import f_initLog
from f_logging import f_log as f_l
import f_retIMG
# from shutil import copy as s_copy
from shutil import copyfileobj as s_copyfileobj
from shutil import copy as s_copy
from os import path as o_p
from os import makedirs as o_makedirs
from time import sleep as t_sleep

# png_uri=DataURI.from_file('Axelfall-MR240430-CorT20000.png')
# print(str(png_uri))
f_initLog()

def f_FOLDERdotSerialAppend(in_folder,in_appendfile,in_andelse=".png"):
    folder_img_list=f_retIMG.f_allimg_thisfolder(in_folder,in_andelse)
    f_l(folder_img_list)
    f=open(in_appendfile,'a')
    # f.write('const '+in_folder+' = {')
    f_len_img=len(folder_img_list)
    for i,this_image in enumerate(folder_img_list):
        f_l(str(i)+' : '+this_image)
        png_uri=DataURI.from_file(this_image)
        f.write('image'+str(i)+': \''+str(png_uri)+'\'')
        if (i<f_len_img):
            f.write(', \n')
        else:
            f.write('\n')
        # f_l('image'+str(i)+': \'-datauriremoved-\', ')
    f.write('};\n\n\n\n\n')
    f.close()

def f_init_datauri_file(in_folder,in_appendfile,in_casename="case",in_examname="exam",in_seriesname="series",sag=False,xres=512,yres=512):
    
    f=open(in_appendfile,'a')
    f.write("\n\n\n\n\nconst const_casename = \""+in_casename+"\"; \n ")
    f.write("const const_examname = \""+in_examname+"\"; \n ")
    f.write("const const_seriesname = \""+in_seriesname+"\"; \n ")
    f.write("const const_sag = \""+str(sag)+"\"; \n ")
    f.write("const const_xres = \""+str(xres)+"\"; \n ")
    f.write("const const_yres = \""+str(yres)+"\"; \n ")
    f.write("const stack1 = {")
    f.close()

def f_append_todatauri(in_append,out_html,pre_append="/config/workspace/slideshoe-MCQ/append_folder/beforeappend.html",post_append="/config/workspace/slideshoe-MCQ/append_folder/afterappend.html"):
    pre_append_file=open(pre_append)
    in_append_file=open(in_append)
    post_append_file=open(post_append)

    with open(out_html, 'a') as f:
        s_copyfileobj(pre_append_file, f)
        s_copyfileobj(in_append_file, f)
        s_copyfileobj(post_append_file, f)
    
    pre_append_file.close()
    in_append_file.close()
    post_append_file.close()

    
     
        



# def f_end_datauri_file(in_folder,in_appendfile):
curr_base_base="/config/workspace/slideshoe-MCQ/"
curr_casename="Neo1"
curr_casefolder=curr_casename+"/"
curr_examname="MR-Hjarna"
curr_examfolder=curr_examname+"/"
curr_seriesname='swi-jpg'
curr_imgtype='.jpg'
curr_isSag=False


curr_img_folder=curr_base_base+"cases/"+curr_casefolder+curr_examfolder+curr_seriesname+'/'
curr_appendfolder=curr_base_base+"appendfiles/"+curr_casefolder+curr_examfolder+curr_seriesname+'/'
if not o_p.exists(curr_appendfolder):
    o_makedirs(curr_appendfolder)

curr_htmlfolder=curr_base_base+"htmlfiles/"+curr_casefolder+curr_examfolder+'/'
if not o_p.exists(curr_htmlfolder):
    o_makedirs(curr_htmlfolder)
curr_htmlfile=curr_htmlfolder+curr_seriesname+".html"


curr_appendfile=curr_appendfolder+curr_seriesname+".in.txt"
curr_appendfile_copy=curr_appendfolder+curr_seriesname+".copy.txt" #create copy so update is obvious




f_init_datauri_file(curr_img_folder, curr_appendfile,curr_casename,curr_examname,curr_seriesname,curr_isSag)
while not o_p.exists(curr_appendfile):
    t_sleep(1)

f_FOLDERdotSerialAppend(curr_img_folder, curr_appendfile,curr_imgtype)
s_copy(curr_appendfile,curr_appendfile_copy)

while not o_p.exists(curr_appendfile_copy):
    t_sleep(1)
f_append_todatauri(curr_appendfile,curr_htmlfile)

