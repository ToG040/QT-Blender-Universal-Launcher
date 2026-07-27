import sys
import subprocess
import os


BLENDER = r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"


if len(sys.argv) < 2:
    sys.exit()


file_path = sys.argv[1]

extension = os.path.splitext(file_path)[1].lower()


# Escape path for Blender Python
file_path = file_path.replace("\\", "\\\\")


if extension == ".fbx":

    import_command = f"""
bpy.ops.import_scene.fbx(
    filepath=r'{file_path}'
)
"""


elif extension == ".obj":

    import_command = f"""
bpy.ops.wm.obj_import(
    filepath=r'{file_path}'
)
"""


elif extension == ".stl":

    import_command = f"""
bpy.ops.wm.stl_import(
    filepath=r'{file_path}'
)
"""


elif extension in [".gltf", ".glb"]:

    import_command = f"""
bpy.ops.import_scene.gltf(
    filepath=r'{file_path}'
)
"""


elif extension == ".dae":

    import_command = f"""
bpy.ops.wm.collada_import(
    filepath=r'{file_path}'
)
"""


elif extension == ".ply":

    import_command = f"""
bpy.ops.wm.ply_import(
    filepath=r'{file_path}'
)
"""


elif extension == ".abc":

    import_command = f"""
bpy.ops.wm.alembic_import(
    filepath=r'{file_path}'
)
"""


else:

    sys.exit(
        "Unsupported file type: " + extension
    )



script = f"""
import bpy

# clear startup scene

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()


{import_command}
"""



subprocess.Popen(
    [
        BLENDER,
        "--python-expr",
        script
    ],
    creationflags=subprocess.CREATE_NO_WINDOW
)