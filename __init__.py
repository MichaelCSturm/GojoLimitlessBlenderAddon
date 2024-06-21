import bpy


bl_info = {
 "name": "Gojo",
 "description": "Addon for testing",
 "author": "Tester",
 "blender": (2, 80, 0),
 "version": (1, 0, 0),
 "category": "Test",
 "location": "View3D > UI > Unity Batch FBX Export",
}



def changeFunc(self, context):
        print("The value changed", self)
        #fakenum = exporty.getFirst(get_float(self))


# def get_First_int(self):
#         return self


# def set_First_int(self, value):
#         self = value
    
# def get_Final_int(self):
#         return self


# def set_Final_int(self, value):
#         self = value



from . HorseyTime_op import HelloWorldOperator
from . HorseyTime_Launch import LaunchOperator
from . HorseyTime_Settings import  TESTADDON_PT_TestPanel
from . HorseyTime_Settings import panelFunc
from . HorseyTime_Settings import MyMaterialProps
from . HorseyTime_testOp import TestingButton

        
        


        
 
classes = (TESTADDON_PT_TestPanel, HelloWorldOperator, LaunchOperator, TestingButton)
 
def register():
   
    bpy.utils.register_class(MyMaterialProps)
    bpy.types.Object.my_custom_props= bpy.props.PointerProperty(type=MyMaterialProps)
    
    for c in classes:
        bpy.utils.register_class(c)
    
    
    
    
    
#bpy.types.Scene.PerspectiveSettings = bpy.props.PointerProperty(type=PerspectiveSettings)
    

def unregister():
    
    for c in classes:
        bpy.utils.unregister_class(c)
        
    del bpy.types.Object.my_custom_props
    bpy.utils.unregister_class(MyMaterialProps)

   
    
    
    


if __name__ == "__main__":
    register()