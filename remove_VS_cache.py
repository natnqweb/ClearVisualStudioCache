import os
import fnmatch
import shutil


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
                return result
    return result


# example find('*.txt', '/path/to/dir')
USER_PROFILE = os.environ['USERPROFILE']


def remove_files_in_dir(dir: str):
    dir_exist = os.path.exists(dir)
    if (dir_exist == True):
        answer = str(input(f"do you want to remove directory: {dir}\n[y/n]\n"))
        if (answer == 'y' or answer == 'Y'):
            try:
                shutil.rmtree(dir)
            except:
                print(f"could not remove some file from: {dir}")
            else:
                print(f"removed: {dir}")
    else:
        print(f"{dir} : can't be removed\nbecouse dir does not exist!")


def vs_remove_component_cache(version: str):
    vs_path = str.format(
        "{}\AppData\Local\Microsoft\VisualStudio", USER_PROFILE)

    print(f"searching version:{version}\nin {vs_path}")
    pattern = str.format("{}.*", version)
    print(f"pattern: {pattern}")
    vs_folder_found = find(pattern, vs_path)
    if (len(vs_folder_found) > 0):
        print(f"\nfound: {vs_folder_found[0]}")
        component_cache = vs_folder_found[0]
        remove_files_in_dir(component_cache)
    else:
        print("not found")


def vs_remove_user_temp_folder():
    remove_files_in_dir(str.format("{}\AppData\Local\Temp", USER_PROFILE))


def vs_clear_cache():
    remove_files_in_dir(str.format(
        "{}\AppData\Local\Microsoft\Team Foundation", USER_PROFILE))
    remove_files_in_dir(str.format(
        "{}\AppData\Local\Microsoft\VisualStudio", USER_PROFILE))
    remove_files_in_dir(str.format(
        "{}\AppData\Local\Microsoft\VSCommon", USER_PROFILE))


def main():

    vs_version = str(input(
        "enter version of visual studio\n example: if VS2022:\n version is: 17\nso you input 17\n:"))
    if (len(vs_version) > 1):
        vs_remove_component_cache(vs_version)
    vs_remove_user_temp_folder()
    vs_clear_cache()


if __name__ == "__main__":
    main()
