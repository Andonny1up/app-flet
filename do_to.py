import flet as ft


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="..//",width=250,expand=True)
        self.task_view = ft.Column()
        self.items_left = ft.Text("0 Articulos restantes")
        
        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.task_changed,
            tabs=[ft.Tab(text='Todo'),ft.Tab(text='Activa'),ft.Tab(text='Completada')]
        )
        
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor="#EB4343",on_click=self.add_click)
                    ]
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.task_view,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                ft.OutlinedButton(
                                    text="Borrar completadas",
                                    on_click=self.clear_clicked
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    
    
    def add_click(self,e):
        task = Task(self.new_task.value,self.task_changed,self.task_delete)
        self.task_view.controls.append(task)
        self.new_task.value = ""
        self.update()
        
    def task_delete(self, task):
        self.task_view.controls.remove(task)
        self.update()
        
    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.task_view.controls:
            task.visible=(
                status == 'Todo'
                or (status == "Activa" and not(task.completed) )
                or (status == "Completada" and task.completed )
            )
            if not task.completed:
                count += 1
        
        self.items_left.value = f"{count} Articulo(s) restantes"
        super().update()
        
    def task_changed(self,e):
        self.update()
        
    def clear_clicked(self,e):
        for task in self.task_view.controls:
            if task.completed:
                self.task_delete(task)


class Task(ft.UserControl):
    def __init__(self, task_name,task_status_change,task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
        
        
    def build(self):
        self.display_task = ft.Checkbox(value=False,label=self.task_name,on_change=self.status_changed)
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
        
    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)
        
              

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
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(main)