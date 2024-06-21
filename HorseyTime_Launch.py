import bpy
from . HorseyTime_Functions import ExtraFunction
from . HorseyTime_op import HelloWorldOperator
import copy
class LaunchOperator(bpy.types.Operator):
        
    bl_idname = "wm.launch"
    bl_label = "Launch Operator"
    def get_id_type(obj):
        id_type = obj.name
        return id_type
    
    def execute(self, context):
        firstFrame = bpy.context.object.my_custom_props.value
        finalFrame = bpy.context.object.my_custom_props.Finalvalue
        findName = bpy.context.object.my_custom_props.SelectFieldName
        objinSelected = bpy.context.view_layer.objects.active
        newobj = LaunchOperator.get_id_type(objinSelected)
        ###################################################################################
        ### bpy.context.scene.objects.get("NAME OF MESH") is how to grab objects by name #
        # bpy.context.object.my_custom_props.value is how to grab the property panels ####
        ####################################################################################
        #HelloWorldOperator.objList
        
        objList = HelloWorldOperator.select_name(findName)
        if objList[0]:
            oVertsList = []
            cvertList = []
            oVertsList.clear()
            cvertList.clear()
            print("FirstFrame"+str(bpy.context.object.my_custom_props.value))
            print("Selected object(s) " + str(bpy.context.view_layer.objects.active))
            
            #selected = HelloWorldOperator.justTheVerts()
            for mesh in objList:
                currVerts = HelloWorldOperator.certainVertgetter(mesh)
                oVertsList.append(currVerts)
            for verts in oVertsList:
                closestvert = HelloWorldOperator.getLocation(verts,objinSelected)
                cvertList.append(closestvert)

            # print(str(objinSelected) + "THE NEW VERISON YESSIR ID HAHA" + str(newobj))
            HelloWorldOperator.keyframeObj(objinSelected, firstFrame, 
                                           finalFrame,
                                            objList, cvertList)
            # print("omesh verts: "+str(len(Overts)) + "\nselectmeshverts: " +str(len(selected))+ "\nNumber of selected objects: "+str(len(bpy.context.selected_objects)))
        return {'FINISHED'}