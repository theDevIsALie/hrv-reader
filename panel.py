import bpy


class HRV_PT_Setup(bpy.types.Panel):
    bl_label = "HRV"
    bl_idname = "HRV_PT_Setup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HRV"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('HRV.select_file', text="Import HRV")