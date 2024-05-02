import os
import shutil
import sys


def remove_unused_files(project_folder, main_filename):
    unused_folder = os.path.join(project_folder, "unused")

    log_file_path = os.path.join(project_folder, f"{main_filename}.log")
    with open(log_file_path, "r") as log_file:
        log_content = log_file.read()

    for root, dirs, files in os.walk(project_folder):
        print(f"Processing folder: {root}")

        for file in files:
            file_path = os.path.join(root, file)

            if file in log_content:
                print(f"- File {file} is in use.")
            else:
                print(f"+ File {file} is not in use.")

                unused_subfolder = os.path.join(
                    unused_folder, os.path.relpath(root, project_folder)
                )
                os.makedirs(unused_subfolder, exist_ok=True)

                shutil.move(file_path, os.path.join(unused_subfolder, file))

    print("Script finished.")


if __name__ == "__main__":
    project_folder = sys.argv[1]
    main_filename = sys.argv[2]
    remove_unused_files(project_folder, main_filename)
