# remixer/remix_generator.py

import os
import shutil

def remix_repos(repo1_path, repo2_path, output_path):
    os.makedirs(output_path, exist_ok=True)
    for src in [repo1_path, repo2_path]:
        for file in os.listdir(src):
            src_file = os.path.join(src, file)
            dst_file = os.path.join(output_path, file)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dst_file)
    with open(os.path.join(output_path, "README.md"), "w") as f:
        f.write(f"# Remix Project\n\nIncludes code from:\n- {repo1_path}\n- {repo2_path}\n")
    return output_path
