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
from glob import glob

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

    
     
def f_jpg_folder_to_html(in_basename,in_casename,in_examname,in_seriesname,in_isSag=False,in_imgtype=".jpg"):
    curr_casefolder=in_casename+"/"
    curr_examfolder=in_examname+"/"
    curr_img_folder=in_basename+"cases/"+curr_casefolder+curr_examfolder+in_seriesname+'/'
    curr_appendfolder=in_basename+"appendfiles/"+in_imgtype+"/"+curr_casefolder+curr_examfolder+'/'

    if not o_p.exists(curr_appendfolder):
        o_makedirs(curr_appendfolder)
    curr_htmlfolder=in_basename+"htmlfiles/"+in_imgtype+"/"+curr_casefolder+curr_examfolder+'/'

    if not o_p.exists(curr_htmlfolder):
        o_makedirs(curr_htmlfolder)
    curr_htmlfile=curr_htmlfolder+in_seriesname+".html"

    curr_appendfile=curr_appendfolder+in_seriesname+".in.txt"
    curr_appendfile_copy=curr_appendfolder+in_seriesname+".copy.txt" #create copy so update is obvious
    f_init_datauri_file(curr_img_folder, curr_appendfile,in_casename,in_examname,in_seriesname,in_isSag)
    
    while not o_p.exists(curr_appendfile):
        t_sleep(1)

    f_FOLDERdotSerialAppend(curr_img_folder, curr_appendfile,in_imgtype)
    s_copy(curr_appendfile,curr_appendfile_copy)

    while not o_p.exists(curr_appendfile_copy):
        t_sleep(1)
    f_append_todatauri(curr_appendfile,curr_htmlfile)

def f_name_X_Ys_back(inin_instr,Xs=0,Ys="/"):
    inin_instr=inin_instr.replace("/","\n")
    outout_outstr_lines=inin_instr.splitlines(False)
    boop_X=-1*(Xs+1)
    return outout_outstr_lines[boop_X]

def f_path_X_Ys_back(inin_instr,Xs=0,Ys="/"):
    inin_instr=inin_instr.replace("/","\n")
    outout_outstr_lines=inin_instr.splitlines(False)
    boop_X=-1*(Xs+1)
    return "/".join(outout_outstr_lines[:boop_X])

def f_SaG_in_seriesname(in_name):
    now_isSag=("sag" in in_name.lower())
    return now_isSag

def f_foldername_to_parts(instr_ing):
    pars_series=f_name_X_Ys_back(instr_ing,0)
    pars_exam=f_name_X_Ys_back(instr_ing,1)
    pars_case=f_name_X_Ys_back(instr_ing,2)
    pars_basename=f_path_X_Ys_back(instr_ing,3)
    return pars_basename, pars_case,pars_exam, pars_series, f_SaG_in_seriesname(pars_series), 

# def f_slasherlist_t_html()





import sys
def f_getargs(dummy='dummy'):
    lenargs=len(sys.argv)
    if (lenargs==2):
        outarg=sys.argv[1]
    else:
        outarg='EMPTY'
    return outarg

def f_list_cMeS_folders(inpath):
    max_slash=0
    max_slasher_list=[] 
    firstlist=[]
    path_es = glob(inpath+"/**", recursive=True)
    for iii,one_path in enumerate(path_es):
        # f_l("eval: "+one_path)
        if o_p.isdir(one_path):
            firstlist.append(one_path)            
            print(one_path+" - is a dir")
            if (one_path.count("/")>max_slash):
                max_slash=one_path.count("/")
                print(max_slash,"  :max_slash")
    for hhh,fromlist in enumerate(firstlist):
        if (fromlist.count("/")==max_slash):
            print(fromlist+ "  :   ---------Max Slasher")
            max_slasher_list.append(fromlist)
    return max_slasher_list
        
def f_pars_it(in_list_cmes):
    for i_cmes in in_list_cmes:
        print(f_foldername_to_parts(i_cmes))
 

f_pars_it(f_list_cMeS_folders(f_getargs()))
 
# # # # def f_end_datauri_file(in_folder,in_appendfile):
# out_base="/config/workspace/slideshoe-MCQ/"
# out_casename="missb1"
# out_examname="MR190912"
# out_seriesname='t2-tse-sag'
# #out_isSag=False     
# out_imgtype='.jpg'

# f_jpg_folder_to_html(out_base,out_casename,out_examname,out_seriesname,f_SaG_in_seriesname(out_seriesname),out_imgtype)


# # curr_img_folder=curr_base_base+"cases/"+curr_casefolder+curr_examfolder+curr_seriesname+'/'
# # curr_appendfolder=curr_base_base+"appendfiles/"+curr_imgtype+"/"+curr_casefolder+curr_examfolder+'/'
# # if not o_p.exists(curr_appendfolder):
# #     o_makedirs(curr_appendfolder)

# curr_htmlfolder=curr_base_base+"htmlfiles/"+curr_imgtype+"/"+curr_casefolder+curr_examfolder+'/'
# if not o_p.exists(curr_htmlfolder):
#     o_makedirs(curr_htmlfolder)
# curr_htmlfile=curr_htmlfolder+curr_seriesname+".html"


# curr_appendfile=curr_appendfolder+curr_seriesname+".in.txt"
# curr_appendfile_copy=curr_appendfolder+curr_seriesname+".copy.txt" #create copy so update is obvious




# f_init_datauri_file(curr_img_folder, curr_appendfile,curr_casename,curr_examname,curr_seriesname,curr_isSag)
# while not o_p.exists(curr_appendfile):
#     t_sleep(1)

# f_FOLDERdotSerialAppend(curr_img_folder, curr_appendfile,curr_imgtype)
# s_copy(curr_appendfile,curr_appendfile_copy)

# while not o_p.exists(curr_appendfile_copy):
#     t_sleep(1)
# f_append_todatauri(curr_appendfile,curr_htmlfile)

