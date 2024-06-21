import bpy
class ExtraFunction():
    def other_select_one_object(obj):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects[obj].select_set(True)
    def select_one_object(obj):
        
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            
# ob = bpy.context.scene.objects["Cube"]       # Get the object
# bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
# bpy.context.view_layer.objects.active = ob   # Make the cube the active object 
# ob.select_set(True)                          # Select the cube#
