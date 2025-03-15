import os
import git

def cloneRepo(gitUrl, repoDir="RepoCode"):
    try:
        if os.path.exists(repoDir):
            os.system(f"rm -rf {repoDir}")
        git.Repo.clone_from(gitUrl, repoDir)
    except Exception as e:
        raise RuntimeError(f"Failed to clone repository: {str(e)}")

def extractCodeFiles(repoDir="RepoCode"):
    codeFiles = []
    for root, _, files in os.walk(repoDir):
        for file in files:
            if file.endswith((".py", ".java", ".cpp")):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    codeFiles.append((file, f.read()))
    return codeFiles
