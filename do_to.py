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
        self.task_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.task_view.update()
        self.new_task.update()
          

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