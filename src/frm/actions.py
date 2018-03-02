import os
from git import Repo



def get_workflow(project_type):
    if project_type == "java":
        repo = Repo(self.rorepo.working_tree_dir)
        cloned_repo = repo.clone(join(rw_dir, 'to/this/path'))
    elif project_type == "php":
        pass
    elif project_type == "python":
        pass

