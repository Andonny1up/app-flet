import flet as ft

def main(page: ft.Page):
    
    def sunnyMode(e):
        if(page.bgcolor == ft.colors.WHITE):
            page.bgcolor = "#0A0A22"
        else:
            page.bgcolor = ft.colors.WHITE
        
        page.update()
    
    
    def add_click(e):
        task_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        task_view.update()
        new_task.update()
        
       
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
    task_view = ft.Column()
    new_task = ft.TextField(hint_text="..//",width=250,expand=True)
    
    view = ft.Column(
        controls=[
            ft.Row(
          controls=[
              new_task,
              ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor="#EB4343",on_click=add_click)
          ]  
        ),
            task_view
        ]
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(main)