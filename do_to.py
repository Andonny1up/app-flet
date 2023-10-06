import flet as ft


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="..//",width=250,expand=True)
        self.task_view = ft.Column()
        
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
            controls=[
                self.new_task,
                ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor="#EB4343",on_click=self.add_click)
            ]  
            ),
                self.task_view
            ]
        )
    
    
    def add_click(self,e):
        task = Task(self.new_task.value,self.task_delete)
        self.task_view.controls.append(task)
        self.new_task.value = ""
        self.task_view.update()
        self.new_task.update()
        
    def task_delete(self, task):
        self.task_view.controls.remove(task)
        self.update()


class Task(ft.UserControl):
    def __init__(self, task_name,task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        
        
    def build(self):
        self.display_task = ft.Checkbox(value=False,label=self.task_name)
        self.edit_name = ft.TextField(expand=1)
        
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Editar Tarea",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINED,
                            tooltip="Eliminar Tarea",
                            on_click=self.delete_clicked,
                        )
                    ]
                )
            ]
        )
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Actualizar Tarea",
                    on_click=self.save_clicked,
                )
            ]
        )
        
        return ft.Column(
            controls=[
                self.display_view,self.edit_view
            ]
        )
        
    def edit_clicked(self,e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()
        
    
    def save_clicked(self,e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
        
        
    def delete_clicked(self,e):
        self.task_delete(self)
        
              

def main(page: ft.Page):
    
    def sunnyMode(e):
        if(page.bgcolor == ft.colors.WHITE):
            page.bgcolor = "#0A0A22"
        else:
            page.bgcolor = ft.colors.WHITE
        
        page.update()
    
    
    
        
       
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TASK, color="#EB4343"),
        leading_width=40,
        title=ft.Text("To Do App",color=ft.colors.WHITE),
        bgcolor= "#0A0A22",
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click=sunnyMode)
        ]
    )
    page.bgcolor = "#0A0A22"
    
    
    view = TodoApp()
    view_2 = TodoApp()
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view,view_2)


ft.app(main)