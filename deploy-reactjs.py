import shutil
import os
REACTJS_APP_SOURCE = "/Volumes/T9/workspace/reactjs-workspace/haru-app-reactjs/dist/assets"
REACTJS_APP_TARGET = "/Volumes/T9/workspace/python-workspace/haru-app/public/assets"
def find_copy():
    print("Copying reactjs app source to reactjs app target")
    for root, dirs, files in os.walk(REACTJS_APP_SOURCE):
        for file in files:
            print(f"Copying {file}...")
            if file.endswith(".js"):
                shutil.copy(os.path.join(root, file), os.path.join(REACTJS_APP_TARGET, "reactjs_app.js"))
            elif file.endswith(".css"):
                shutil.copy(os.path.join(root, file), os.path.join(REACTJS_APP_TARGET, "reactjs_app.css"))
            else:
                shutil.copy(os.path.join(root, file), os.path.join(REACTJS_APP_TARGET, file))

if __name__ == '__main__':
    print("Deploy reactjs to Python Flask")
    find_copy()