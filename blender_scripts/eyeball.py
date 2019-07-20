import bpy

master_collection = bpy.context.collection

eyeballs_collection = bpy.data.collections.new(name='Eyeballs Collection')
master_collection.children.link(eyeballs_collection)

eyeballs_mesh = bpy.data.meshes.new(name='Eyeballs Mesh')
eyeballs_object = bpy.data.objects.new('Eyeballs Object', eyeballs_mesh)
eyeballs_collection.objects.link(eyeballs_object)