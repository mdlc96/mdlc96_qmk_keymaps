import shutil
import os

def copy_and_overwrite_keymap_folder(from_path, to_path):
    # check if it is the correct folder, containing keymap.c 
    # to avoid (very) possible utter messes
    assert os.path.exists(os.path.join(from_path,"keymap.c")), \
        "src folder does not contain keymap.c file!"  

    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

src_dir = 'C:/Users/matte/qmk_firmware/keyboards/redox/keymaps/mdlc96/'
dst_dir = 'D:/GIT_REPOS/mdlc96_qmk_keymaps/redox/keymaps/redox-work-keymap/'

copy_and_overwrite_keymap_folder(src_dir, dst_dir)

# copy rule.mk
src_file = 'C:/Users/matte/qmk_firmware/keyboards/redox/rules.mk'
dst_dir = 'D:/GIT_REPOS/mdlc96_qmk_keymaps/redox/'
shutil.copy2(src_file, dst_dir)

print("done")