import flet as ft

def main(page: ft.Page):
    page.title = "Counter 🧮"
    
    input_number = ft.TextField(label="Number", value=0, width=100)
    
    def add(e):
        input_number.value = str(int(input_number.value) + 1) 
        page.update()
        
    def remove(e):
        input_number.value = str(int(input_number.value) - 1) 
        # input_number -= 1
        page.update()
    
    page.appbar = ft.AppBar(
        title=ft.Text("Clicks counter", size=50), 
        center_title=True, 
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_GREY_200,
        elevation=20
    )
    page.add(
        ft.Row(
            expand=True,
            alignment="center",
            controls=[
                ft.Container(
                    border_radius= 100,
                    content=ft.IconButton(icon=ft.icons.EXPOSURE_MINUS_1_ROUNDED,
                    icon_color="red900",
                    icon_size=40,
                    tooltip="Remove 1 from counter", on_click=remove),
                    bgcolor=ft.colors.WHITE,
                ),
                input_number,
                ft.Container(
                    border_radius= 100,
                    content=ft.FloatingActionButton(icon=ft.icons.PLUS_ONE_OUTLINED, on_click=add, tooltip="Adds 1 to counter"),
                ),
            ],
        ),
    )

ft.app(target=main, assets_dir="assets")
    
    
