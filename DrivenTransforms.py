# ***************WARNING****************
# Run this script at your own risk!!

# This is a proof of concept to show how expressions in object properties may be used 
# instead of or in addition to drivers for a faster workflow without the need of the many
# steps involved in setting up and maintiaining drivers. Any python expression that can be 
# put on one line will work.

# Press the "Run Script" button below and look at the bottom of the object tab in the 
# properties panel to see the myX, myY, and myZ fields. Use CTRL+Alt+Shift+C while hovering 
# use over any object property and paste this into a field in the Driven Transforms panel to  
# in an expression. Or simply try an expression like 1.5 * 3.14.
# Upvote this as a new Blender feature at rightclickselect.com - Dan Pool (dpdp) 



import bpy
import os

os.system('cls')

def update_func(self, context):
    obj = context.object
    obj.location[0] = eval(obj.myX)
    obj.location[1] = eval(obj.myY)
    obj.location[2] = eval(obj.myZ)
    
bpy.types.Object.myX = bpy.props.StringProperty(update=update_func, default="None")
bpy.types.Object.myY = bpy.props.StringProperty(update=update_func, default="None")
bpy.types.Object.myZ = bpy.props.StringProperty(update=update_func, default="None")

def my_handler(scene):
    for obs in bpy.context.scene.objects:
        if obs.myX != "None":
            obs.location[0] = eval(obs.myX)
        if obs.myY != "None":
            obs.location[1] = eval(obs.myY)
        if obs.myZ != "None":
            obs.location[2] = eval(obs.myZ)

bpy.app.handlers.scene_update_post.append(my_handler)
    
class DrivenPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_driven"
    bl_label = "Driven Transforms"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw_header(self, context):
        layout = self.layout
        obj = context.object
        layout.prop(obj, "select", text="")

    def draw(self, context):
        layout = self.layout

        obj = context.object
        
        row = layout.row()
        row.prop(obj, "myX")
        row = layout.row()
        row.prop(obj, "myY")
        row = layout.row()
        row.prop(obj, "myZ")
        row = layout.row()
        row.label(text = 
            "X: " + str(round(obj.location[0], 3)) + 
            "  Y: " + str(round(obj.location[1], 3)) + 
            "  Z: " + str(round(obj.location[2], 3)) )


bpy.utils.register_class(DrivenPanel)