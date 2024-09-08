import shutil,f_logging
import pprint
from os import getcwd, path, listdir
from pathlib import Path as pathlib_path
from sys import exit


# def f_retIMG_initlog():








      
def f_retDirsFiles(inlist,inpath):
    f_files=[]
    f_dirs=[]
    
    for i,f_thisfile in enumerate(inlist):
        f_thisfile=inpath+'/'+f_thisfile
        # logger.debug(f_thisfile)
        # logger.debug(path.isfile(f_thisfile))
        
        if path.isfile(f_thisfile):
            f_files.append(f_thisfile)
        else:
            f_dirs.append(f_thisfile)
    return f_dirs, f_files

def f_retEnumImg(infilnames,in_andelse='.png',in_digits=4):
    outfilenames=[]
    discarded_filenames=[]
    for i,this_fn in enumerate(infilnames):
        andelse=this_fn[-4:]
        siffrelse=this_fn[-8:-4]
        if andelse==in_andelse and siffrelse.isnumeric():
            outfilenames.append(this_fn)
        else:
            discarded_filenames.append(this_fn)

    return outfilenames,discarded_filenames

     

def f_allimg_thisfolder(inpath='EMPTY',in_andelse='.png',in_digits=4):
    
    #get all images in thisfolder

    #get all files  and sort
    if (inpath!="EMPTY"):
        thispath=inpath
    else:
        thispath=pathlib_path.cwd()
    
    # logger.debug(thispath)
    f_out=listdir(thispath)
    f_out.sort()
    # logger.debug(f_out)

    #check keep only files not folders
    outdirs,outfiles=f_retDirsFiles(f_out,thispath)

    # logger.debug(outfiles)
    outfiles,disc_files=f_retEnumImg(outfiles,in_andelse,in_digits)

    # logging:
    
    # logger.debug("\n\n pattern: *"+in_andelse+" \n\n # digits: "+str(in_digits)+"\n")
    # logger.debug("\n\n working directory: \n")
    # logger.debug(thispath)
    # logger.debug("\n\n discarded folders: \n")
    # logger.debug(outdirs)
    # logger.debug("\n\n discarded files: \n")
    # logger.debug(disc_files)
    # logger.debug("\n\n kept files: \n")
    # logger.debug(outfiles)
    f_logging.f_log('wohoo')


    return outfiles


# def f_anyFileInList():
#     for a in range(len(f_filesinthisfolder)-1):
#         f_currfile=f_filesinthisfolder[a]
#         # f_isfile=path.isfile(f_currfile)
#         # print(f_currfile," is a file?",f_isfile)
#         if (f_currfile in f_stopIfFileorFolderExists): #agnostic to file or folder

#             print(f_currfile,' ; possible of target of this operation all ready exists. rename as backup')
#             print('quitting')
#             exit()


# filin,dirin=f_lsFilesDirs("static/img/testfall-axel/MRAXEL-240430/SAGT2")
# f_retNumberedImgList(filin)

# f_allimg_thisfolder('static/img/testfall-axel/MRAXEL-240430/SAGT2','.png')
