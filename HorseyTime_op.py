import bpy
import math
import mathutils
import copy
from . HorseyTime_Functions import ExtraFunction

class HelloWorldOperator(bpy.types.Operator):
    
    objList = []
    emptyList = []
    bl_idname = "wm.hello_world"
    bl_label = "Minimal Operator"
    def select_name( name = ""):
            bpy.ops.object.select_all(action='DESELECT')
            select_nameList = []
            select_nameList.clear()
            ogname = name + "."
            current_state = bpy.data.objects[name].select_get()
            cube = bpy.context.scene.objects.get(name)
            cube= bpy.data.objects.get(name)
            print("Curr state = " + str(current_state) + "cube" + str(cube))
            if cube:
                bpy.data.objects[name].select_set(True)
                select_nameList.append(cube)
                i = 0
                j = 0
                k = 1
                name = ogname + str(i)+str(j) + str(k)
                cube= bpy.data.objects.get(name)
                while cube:
                    select_nameList.append(cube)
                    bpy.data.objects[name].select_set(True)
                    if k< 9:
                        k+=1
                    elif j <9:
                        j+=1
                        k=0
                    else:
                        i+=1
                        j = 0
                        k = 0
                    name = ogname + str(i)+str(j) + str(k)
                    #print(f"Current name {name} Current cube {cube}")
                    cube= bpy.data.objects.get(name)
                
            print(f"Select names list {len(select_nameList)}")
            return select_nameList
    def getLocation(oMeshVerts, SentObjloc):
        olddistance = 9999
        location = SentObjloc.location
        objToEdit = SentObjloc
        wmtx = objToEdit.matrix_world
        gLoc = wmtx @location
        #print("location!!!!!!!!!!!!!:" + str(location)+ str(objToEdit) + "gLOC" + str(gLoc))
        
        closest = object
        if len(oMeshVerts) == 0:
            print("AYO NO FUCKING WAY DOG")
            return 2
        for v in oMeshVerts:
            #print("VertexPos"+str(v.co)+ "Select OBJ local"+str(location))
            #print(type(v.co[1]))
            distance = math.sqrt((location[0]- v[0])**2+(location[1]- v[1])**2+(location[2]- v[2])**2)
            #print(str(distance))
            if distance<= olddistance:
                #print("Old distance is longer by" +str(distance-olddistance) +"that new new distance =" +str(distance))
                olddistance = distance
                closest = v
        #print("shortest distance is" + str(olddistance) + "at " + str(closest)+ "LOCATION :"+str(location))
        return closest
                
            
    def justTheVerts():
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        return selectedVerts
    def soloVertgetter(objname):
        ExtraFunction.other_select_one_object(objname)
        bpy.ops.object.mode_set(mode='EDIT')
       
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        
        
        return selectedVerts
    def certainVertgetter(objToEdit):
        ExtraFunction.select_one_object(objToEdit)
        bpy.ops.object.mode_set(mode='EDIT')
        wmtx = objToEdit.matrix_world
        vertList = [(wmtx @ vertex.co) for vertex in objToEdit.data.vertices if vertex.select]
        bpy.ops.object.mode_set(mode='OBJECT')
        return vertList
    
    def keyframeObj(objSent, startFrame, hitframe, omeshList,cvertList):
        
        
        #omeshobject_matrix = copy.copy(omesh.matrix_world)
        #vertex_0 = cvert
        #vertex_0_global = omeshobject_matrix @ vertex_0
        
        ################################################################################
        #print("overt coordinates"+str(overt) + "cvert coordinates" + str(cvert))
        objSent.keyframe_insert("location", frame = startFrame)
        #objSent.location = overt
        #objSent.keyframe_insert("location", frame = hitframe)
        framediff = hitframe - startFrame
        print(f"Frame diff {framediff}")
        
       
        i = 1
        for cVerty in cvertList:
            if i==1:
                funnframediff = framediff
            else:
                funnframediff = funnframediff+funnframediff+framediff/i
            funnframediff = round(funnframediff)
            #print(f"FunFrame diff {funnframediff}")
            
            i+=1
            #print(f"cVerty {cVerty.location}")
            objSent.location = cVerty
            objSent.keyframe_insert("location", frame = funnframediff)
            
            

    def execute(self, context):
        
        ## This button creates an empty then the object parented to that empty.
        ##
        
        i = 1
        numOfCirc = bpy.context.object.my_custom_props.NumOfCirc
        FactorSmallest = bpy.context.object.my_custom_props.FactorSmallest
        sizeOfCirc = bpy.context.object.my_custom_props.sizeOfCirc
        nameOfCreation = bpy.context.object.my_custom_props.FieldName
        earlynum = (1+ FactorSmallest)/(i + FactorSmallest)
        earlynum = earlynum * sizeOfCirc
        objList= []
        emptyList = []
        print(numOfCirc)
        while i<= numOfCirc:
            
            num = (1+ FactorSmallest)/(i + FactorSmallest)
            num = num * sizeOfCirc
            #print(str(num) + " NUM NUM NUM NUM NUM NUM NUM, EARLY NUM:         " + str(earlynum) + "num - early num" + str(earlynum-num))
            bpy.ops.object.empty_add(type='SPHERE', align='WORLD', location=(0, 0, 0), scale=(1.0, 1.0, 1.0))
            bpy.ops.transform.resize(value=(num,num,num), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            center= bpy.context.object
            center.name = nameOfCreation + " empty"
            emptyList.append(center)
            bpy.context.active_object.select_set(False)
            
            bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.ops.transform.resize(value=(num,num,num), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            outerMesh= bpy.context.object
            outerMesh.name = nameOfCreation
            #outerMesh.parent = center
            objList.append(outerMesh)
            bpy.context.active_object.select_set(False)
            
            
            if i > 1:
                #num = (num-(1+ FactorSmallest)/(i + FactorSmallest))
                #print(str(num) + " Trial num")
                #HelloWorldOperator.emptyList[i-2].parent = HelloWorldOperator.emptyList[i-1]
                pass
                #print(i)
            
            i+=1
        bpy.ops.object.empty_add(type='SPHERE', align='WORLD', location=(0, 0, 0), scale=(1.0, 1.0, 1.0))
        bpy.ops.transform.resize(value=(num,num,num), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
        center= bpy.context.object
        center.name = nameOfCreation + " controler"
        HelloWorldOperator.emptyList.append(center)
        bpy.context.active_object.select_set(False)
        for obj in objList:
            obj.parent = center
        for empty in emptyList:
            empty.parent = center
        return {'FINISHED'}
