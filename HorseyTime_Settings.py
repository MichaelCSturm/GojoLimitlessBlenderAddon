import bpy

from . HorseyTime_op import HelloWorldOperator
from . HorseyTime_Launch import LaunchOperator
from . HorseyTime_testOp import TestingButton
class panelFunc():
   pass
##
##IGNORE THIS
##
class MyMaterialProps(bpy.types.PropertyGroup):
    Myfunnframediff = 360
    finalsmallCircSize = 0.525
    myfieldName = "GojoMesh"
    FindfieldName = "GojoMesh"
    isNoise = False
    Noise = 0
    def update_func(self, context):
        #(1+ FactorSmallest)/(i + FactorSmallest)
        MyMaterialProps.Noise =  bpy.context.object.my_custom_props.noise
        MyMaterialProps.isNoise = bpy.context.object.my_custom_props.isMoving
        MyMaterialProps.myfieldName = bpy.context.object.my_custom_props.FieldName
        MyMaterialProps.FindfieldName = bpy.context.object.my_custom_props.SelectFieldName
        numOfCirc = bpy.context.object.my_custom_props.NumOfCirc
        FactorSmallest = bpy.context.object.my_custom_props.FactorSmallest
        sizeOfCirc = bpy.context.object.my_custom_props.sizeOfCirc
        MyMaterialProps.finalsmallCircSize = (1+ FactorSmallest)/(numOfCirc + FactorSmallest)
        MyMaterialProps.finalsmallCircSize = MyMaterialProps.finalsmallCircSize* sizeOfCirc
        #print("my test function" + str(MyMaterialProps.finalsmallCircSize))
        i = 1
        j = 0
        framediff = bpy.context.object.my_custom_props.Finalvalue -bpy.context.object.my_custom_props.value
        while j< numOfCirc: 
            if i==1:
                funnframediff = framediff
            else:
                funnframediff = funnframediff+funnframediff+framediff/i
            funnframediff = round(funnframediff)
            j+=1
            i+=1
        MyMaterialProps.Myfunnframediff = funnframediff
        print(f"FunFrame diff {funnframediff}")
    
    value: bpy.props.IntProperty(name="value", default=0,update=update_func )
    Finalvalue: bpy.props.IntProperty(name="value", default=10,update=update_func )
    NumOfCirc: bpy.props.IntProperty(name="value", default=4, min=1, update=update_func )
    sizeOfCirc: bpy.props.FloatProperty(name="value", default=5, update=update_func )
    FactorSmallest: bpy.props.FloatProperty(name="value", default= 10, update=update_func)
    FieldName: bpy.props.StringProperty(name="value", default="GojoMesh", update=update_func)
    SelectFieldName: bpy.props.StringProperty(name="value", default="GojoMesh", update=update_func)
    isMoving: bpy.props.BoolProperty(name="value",default=False, update=update_func)
    noise: bpy.props.IntProperty(name= "value", default=0, min= 0,update=update_func)

class TESTADDON_PT_TestPanel(bpy.types.Panel):
   
        
    bl_idname = "TESTADDON_PT_TestPanel"
    bl_label = "Gojo Slowdown"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Gojo Slowdown"
    bl_context = "objectmode"
    
    def draw(self, context):
        
        layout = self.layout
        obj = context.object
        
        
        
        row = layout.row()
        row.label(text="Make Your Gojo anim dreams come true!")
        row = layout.row()
        row.operator(HelloWorldOperator.bl_idname, text="Create field!")
        row = layout.row()
        row.operator(LaunchOperator.bl_idname, text="Launch one")
        row.operator(TestingButton.bl_idname, text="Launch Multiple")
        
        row = layout.row()
        column = layout.column()
        
        column.prop(obj.my_custom_props, "value",text="Launching frame!")
        column.prop(obj.my_custom_props, "Finalvalue",text="Frame hitting outer shell")
        column = layout.column()
        column.prop(obj.my_custom_props, "NumOfCirc", text="Number of slowdowns")
        column.prop(obj.my_custom_props, "sizeOfCirc", text="size of circs" )
        column.prop(obj.my_custom_props, "FactorSmallest",  text="SmallestCircle size")
        row.prop(obj.my_custom_props, "FieldName", text="Create field")
        column.prop(obj.my_custom_props, "SelectFieldName", text="Select field")
        layout.label(text="Smallest size"+ str( MyMaterialProps.finalsmallCircSize))
        layout.label(text="Final hitting frame" + str(MyMaterialProps.Myfunnframediff))
        row.prop(obj.my_custom_props, "isMoving", text="frame noise")
        row.prop(obj.my_custom_props,"noise", text="noise")
        #layout.label(text="if moving much less calcuation time")
        #= (1+ FactorSmallest)/(i + FactorSmallest)
        
        
        
        