import os
from git import Repo
import shutil
import sys
from frm import helper
repos = {
    "java": "https://github.com/ayoubensalem/docker-java.git",
    "default": "https://github.com/ayoubensalem/docker-java.git",
    "php" :"",
    "python": ""
}
tmp_path = "/tmp/docker/"
DESTINATION_EXIST_CODE = 128
PROJECT_TYPE = "default"

def get_workflow(project_type = "java"):
    PROJECT_TYPE = project_type
    cwd = os.getcwd()
    if os.path.isdir(cwd + "/docker"):
        print("'docker' folder already exists !!")
    else :
        try :
            Repo.clone_from(repos[project_type], tmp_path + project_type )
            shutil.copytree(tmp_path + project_type, cwd + "/docker")
        except Exception as e:
            if e.status == DESTINATION_EXIST_CODE:
                shutil.copytree(tmp_path + project_type, cwd + "/docker")
            else :
                print("An error has occured, try later")
                sys.exit(1)


def clean():
    cwd = os.getcwd()
    if os.path.isdir(cwd + "/docker"):
        shutil.rmtree(cwd + "/docker")
    try :
        Repo.clone_from(repos[PROJECT_TYPE], tmp_path + PROJECT_TYPE )
        shutil.copytree(tmp_path + PROJECT_TYPE, cwd + "/docker")
        print("Project was cleaned successfully !!")
    except Exception as e:
        if e.status == DESTINATION_EXIST_CODE:
            shutil.copytree(tmp_path + PROJECT_TYPE, cwd + "/docker")
            print("Project was cleaned successfully !!")
        else :
            print("An error has occured, try later")
            sys.exit(1)


def destroy():
    cwd = os.getcwd()
    if os.path.isdir(cwd + "/docker"):
        shutil.rmtree(cwd + "/docker")
        print("CD workflow was removed successfully !! ")


def get_infos():
    with open("info.txt") as f:
        content = f.read()
    pretty_content = helper.prettify(content)
    print(pretty_content)

def configure():
    pass
