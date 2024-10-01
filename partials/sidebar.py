import flet as ft

from components.skills import SkillRing

class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/face-1.jpg',
                            border_radius=ft.border_radius.all(100),
                            width=100
                        ),
                        alignment=ft.alignment.bottom_right,
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20
                    ),
                    ft.Text(value='Dalton Peixoto', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Desenvolvedor Fullstack', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.padding.symmetric(vertical=20, horizontal=40),
            alignment=ft.alignment.center
        )
    
class SidebarContent(ft.UserControl):
   def build(self):
       location = ft.Column(
           controls=[
               ft.Row(
                   controls=[
                       ft.Text(value='Residência', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                   ],
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN
               ),
               ft.Row(
                   controls=[
                       ft.Text(value='Cidade', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Sao Paulo', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                   ],
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN
               ),
               ft.Row(
                   controls=[
                       ft.Text(value='Idade', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='32', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                   ],
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN
               )
           ]
       )

       languages = ft.Row(
           controls=[
               SkillRing(title='Portugues', value=1),
               SkillRing(title='Ingles', value=1),
               SkillRing(title='Espalhol', value=0.5)
           ]
       )

       skills = ft.Container()
       technologies = ft.Container()
       cv = ft.Container()

       return ft.Container(
           bgcolor=ft.colors.BLACK12,
           padding=ft.padding.all(20),
           content=ft.Column(
               controls=[
                   location,
                   ft.Divider(height=30),
                   languages,
                   ft.Divider(height=30),
                   skills,
                   ft.Divider(height=30),
                   technologies,
                   ft.Divider(height=30),
                   cv
               ]
           )
       )

class SidebarFooter(ft.UserControl):
     def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src='icons/001-instagram.png', height=15, color='white'),
                        url='https://instagram.com'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png', height=15, color='white'),
                        url='https://instagram.com'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/003-github.png', height=15, color='white'),
                        url='https://instagram.com'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/004-youtube.png', height=15, color='white'),
                        url='https://instagram.com'
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    

class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter()
                ]
            ),
            bgcolor=ft.colors.BACKGROUND
        )