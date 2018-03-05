import os
from git import Repo
import shutil
import sys
import helper

java_repo = "https://github.com/ayoubensalem/docker-java.git"
tmp_path = "/tmp/docker/"
DESTINATION_EXIST_CODE = 128

def get_workflow(project_type):
    cwd = os.getcwd()
    if project_type == "java":
        if os.path.isdir(cwd + "/docker"):
            print("'docker' folder already exists !!")
        else :
            try :
                Repo.clone_from(java_repo, tmp_path + project_type )
                shutil.copytree(tmp_path + project_type, cwd + "/docker")
            except Exception as e:
                if e.status == DESTINATION_EXIST_CODE:
                    shutil.copytree(tmp_path + project_type, cwd + "/docker")
                else :
                    print("An error has occured, try later")
                    sys.exit(1)
    elif project_type == "php":
        pass
    elif project_type == "python":
        pass

def clean():
    pass

def destroy():
    pass

def get_infos():
    with open("info.txt") as f:
        content = f.read()
    pretty_content = helper.prettify(content)
    print(pretty_content)

def configure():
    pass
