import flet as ft


class MainContent(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        banner = ft.Container(
            shadow=ft.BoxShadow(
                color=ft.colors.ON_BACKGROUND,
                offset=ft.Offset(x=0, y=60),
                spread_radius = -30
            ),
            image_src= 'images/bg.jpg',
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_opacity=0.5,
            bgcolor=ft.colors.BACKGROUND,
            margin=ft.margin.only(top=30),
            content=ft.Container(
                content=ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    controls=[
                        ft.Container(
                            padding=ft.padding.all(50),
                            content=ft.Column(
                                controls=[
                                    ft.Text(value='Descubra meu incrivel portfolio', theme_style=ft.TextThemeStyle.HEADLINE_LARGE),
                                    ft.Text(
                                        spans=[
                                            ft.TextSpan(text='<'),
                                            ft.TextSpan(text='code', style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                            ft.TextSpan(text='> '),

                                            ft.TextSpan(
                                                text='Eu desenvolvo aplicativos ios e Android',
                                                style=ft.TextStyle(color=ft.colors.WHITE),
                                            ),
                                            ft.TextSpan(text='</'),
                                            ft.TextSpan(text='code', style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                            ft.TextSpan(text='> '),
                                        ],
                                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                                    ),
                                    ft.ElevatedButton(
                                        bgcolor=ft.colors.PRIMARY,
                                        content=ft.Text(value='Explore agora', color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                        url='#',
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                                    )
                                ],
                                spacing=30,
                                alignment=ft.MainAxisAlignment.CENTER,
                            )
                        ),
                        ft.Container(
                            col={'md': 12, 'lg': 4},
                            content=ft.Image(
                                src='images/face-2.png',
                                width=20,
                                # scale=ft.Scale(scale=1.8, alignment=ft.alignment.bottom_center)
                            )
                        )
                    ]
                )
            ),
            
        )

        experience = ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text='15 + ',
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight=ft.FontWeight.W_900,
                                    size=20
                                )
                            ),
                            ft.TextSpan(
                                text=' Anos de experiência',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text='500 + ',
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight=ft.FontWeight.W_900,
                                    size=20
                                )
                            ),
                            ft.TextSpan(
                                text=' Projetos concluidos',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text='3k + ',
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight=ft.FontWeight.W_900,
                                    size=20
                                )
                            ),
                            ft.TextSpan(
                                text=' Clientes satisfeitos',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text='7 + ',
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight=ft.FontWeight.W_900,
                                    size=20
                                )
                            ),
                            ft.TextSpan(
                                text=' Linguagens de domínio',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    )
                ]
            )
        )

        projects = ft.Container()
        prices = ft.Container()
        testimonials = ft.Container()
        logos = ft.Container()
        footer = ft.Container()

        return ft.Container(
            content=ft.Column(
                controls=[
                    banner,
                    experience,
                    projects,
                    prices,
                    testimonials,
                    logos,
                    footer
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
            padding=ft.padding.all(30)
        )