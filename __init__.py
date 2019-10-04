bl_info = {
    "name": "HRV Reader",
    "author": "theDevIsALie",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D View > Tools",
    "description": "Reader for the HRV (Human Readable Voxel) 3D file format.",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}


import bpy


from . operator import HRV_OT_Operator
from . panel import HRV_PT_Setup


classes = (HRV_OT_Operator,
           HRV_PT_Setup)


register, unregister = bpy.utils.register_classes_factory(classes)

