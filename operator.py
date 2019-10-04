import bpy
import os

from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper


class HRV_OT_Operator(bpy.types.Operator, ImportHelper):
    bl_idname = "hrv.select_file"
    bl_label = "Import HRV"
    bl_description = "Read a HRV file"

    filter_glob = StringProperty(
        default='*.hrv',
        options={'HIDDEN'}
    )

    active_file = BoolProperty(
        name='Active File',
        description='Use the file content',
        default=True
    )

    def execute(self, context):

        filename, extension = os.path.splitext(self.filepath)

        # Print selected file informations
        print('')
        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)
        print('Some Boolean:', self.active_file)
        print('File Path:', self.filepath)
        print('')

        # Print line by line the content of the file
        with open(self.filepath, "r") as f:
            crt_line_num = 0
            for line in f:
                crt_line = line.split(" ")
                if crt_line[0] == "voxel_at":
                    # Positions of the voxel
                    from .utilities import get_xyz

                    x, y, z = get_xyz(crt_line, crt_line_num, index=1, op=self)

                    # Color of the voxel
                    if crt_line[4] == "with_rgba":
                        from . utilities import get_rgba

                        # note: index is 5 (because line 4 content the keyword, and 5 starts with the r value)
                        # r value is the index
                        red, green, blue, alpha = get_rgba(crt_line, crt_line_num, index=5, op=self)

                    import secrets

                    # create voxel
                    mat_name = f"voxel.mat.{crt_line_num}.{secrets.token_urlsafe(16)}"
                    mat = bpy.data.materials.get(mat_name)
                    if mat is None:
                        mat = bpy.data.materials.new(mat_name)
                        mat.diffuse_color = (red, green, blue, alpha)

                    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
                    ob = bpy.context.active_object
                    ob.scale = (0.5, 0.5, 0.5)

                    if ob.data.materials:
                        ob.data.materials[0] = mat
                    else:
                        ob.data.materials.append(mat)

                # not 'voxel_at' line
                else:
                    print("unknow detected !")

                crt_line_num += 1
            f.close()

        return {'FINISHED'}
