import bpy
import webbrowser

class OpenWebsiteOperator(bpy.types.Operator):
    bl_idname = "object.open_website"
    bl_label = "open website"
    
    def execute(self, context):
        confirmed = bpy.ops.wm.modal_confirm('INVOKE_AREA')
        if not confirmed:
            return {'CANCELLED'}
        return {'FINISHED'}
        
    
class ModalConfirmOperator(bpy.types.Operator):
    bl_idname = "wm.modal_confirm"
    bl_label = "Confirm"
    
    def execute(self, context):
        webbrowser.open("https://handf.us")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_confirm(self, event)
class ModalConfirmOperator1(bpy.types.Operator):
    bl_idname = "wm.modal_confirm1"
    bl_label = "Confirm 1"

    def execute(self, context):
        webbrowser.open("https://example1.com")
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_confirm(self, event)


class ModalConfirmOperator2(bpy.types.Operator):
    bl_idname = "wm.modal_confirm2"
    bl_label = "Confirm 2"

    def execute(self, context):
        webbrowser.open("https://example2.com")
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_confirm(self, event)

class OpenWebsitePanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_open_website_panel"
    bl_label = "Open Website Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator(OpenWebsiteOperator.bl_idname, text="Open Website")
        row = layout.row()
        row.operator(ModalConfirmOperator1.bl_idname, text="Example 1")
        row = layout.row()
        row.operator(ModalConfirmOperator2.bl_idname, text="Example 2")

def register():
    bpy.utils.register_class(OpenWebsiteOperator)
    bpy.utils.register_class(OpenWebsitePanel)
    bpy.utils.register_class(ModalConfirmOperator)
    bpy.utils.register_class(ModalConfirmOperator1) 
    bpy.utils.register_class(ModalConfirmOperator2) 

def unregister():
    bpy.utils.unregister_class(OpenWebsiteOperator)
    bpy.utils.unregister_class(OpenWebsitePanel)
    bpy.utils.unregister_class(ModalConfirmOperator)
    bpy.utils.register_class(ModalConfirmOperator1) 
    bpy.utils.register_class(ModalConfirmOperator2)  

if __name__ == "__main__":
    register()
