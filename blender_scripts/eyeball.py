from mathutils import *
from math import *
import bpy

bpy.ops.mesh.primitive_uv_sphere_add(radius=1,
                        view_align=False,
                        enter_editmode=False,
                        location=(0, 0, 0))
bpy.ops.transform.rotate(value=1.5708,
                        orient_axis='Y',
                        orient_type='GLOBAL',
                        orient_matrix=((1, 0, 0),
                        (0, 1, 0), (0, 0, 1)),
                        orient_matrix_type='GLOBAL',
                        constraint_axis=(False, True, False),
                        mirror=True, proportional='DISABLED',
                        proportional_edit_falloff='SMOOTH',
                        proportional_size=1,
                        release_confirm=True)
