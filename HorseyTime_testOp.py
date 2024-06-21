import bpy
import mathutils
import random
from . HorseyTime_Launch import LaunchOperator
from . HorseyTime_op import HelloWorldOperator

class TestingButton(bpy.types.Operator):
    bl_idname = "wm.testing"
    bl_label = "Testing Operator"
    
    
    def launchy(objinSelected):
        from . HorseyTime_Settings import MyMaterialProps
        firstFrame = bpy.context.object.my_custom_props.value
        finalFrame = bpy.context.object.my_custom_props.Finalvalue
        findName = bpy.context.object.my_custom_props.SelectFieldName
        ###################################################################################
        ### bpy.context.scene.objects.get("NAME OF MESH") is how to grab objects by name #
        # bpy.context.object.my_custom_props.value is how to grab the property panels ####
        ####################################################################################
        #HelloWorldOperator.objList
        objList = []
        objList.clear()
        try:
            objList = HelloWorldOperator.select_name(findName)
        except:
                print(f"error here with objList{objList}")
        if objList[0]:
            oVertsList = []
            cvertList = []
            oVertsList.clear()
            cvertList.clear()
           # print("FirstFrame"+str(bpy.context.object.my_custom_props.value))
            #print("Selected object(s) " + str(bpy.context.view_layer.objects.active))
            
            #selected = HelloWorldOperator.justTheVerts()
            try:
                for mesh in objList:
                    currVerts = HelloWorldOperator.certainVertgetter(mesh)
                    oVertsList.append(currVerts)
            except:
                print(f"error here with currvets{currVerts}")
            try:
                for verts in oVertsList:
                    closestvert = HelloWorldOperator.getLocation(verts,objinSelected)
                    cvertList.append(closestvert)
            except:
                print(f"error here with closeestvert{closestvert}")

            # print(str(objinSelected) + "THE NEW VERISON YESSIR ID HAHA" + str(newobj))
            if MyMaterialProps.isNoise:
                FirstRand = random.randint(firstFrame-MyMaterialProps.Noise, firstFrame+MyMaterialProps.Noise)
                LastRand = random.randint(finalFrame-MyMaterialProps.Noise, finalFrame+MyMaterialProps.Noise)
                while LastRand < FirstRand:
                    FirstRand =  abs(random.randint(firstFrame-MyMaterialProps.Noise, firstFrame+MyMaterialProps.Noise))
                    LastRand =  abs(random.randint(finalFrame-MyMaterialProps.Noise, finalFrame+MyMaterialProps.Noise))
                    print(f"first rand = {FirstRand} last rand {LastRand}")
                HelloWorldOperator.keyframeObj(objinSelected, FirstRand, 
                                        LastRand,
                                            objList, cvertList)
            else:
                HelloWorldOperator.keyframeObj(objinSelected, firstFrame, 
                                        finalFrame,
                                            objList, cvertList)
    def Cloning(li1):
        li_copy = li1[:]
        return li_copy
    def execute(self, context):
        thelist = []
        thelist.clear()
        newList = []
        newList.clear()
        newList = TestingButton.Cloning(bpy.context.view_layer.objects.selected)
        thelist = bpy.context.view_layer.objects.selected
        for obj in newList:
            #print(f"obj {obj} + all the objs { newList}")
           
            TestingButton.launchy(obj)
        return {'FINISHED'}