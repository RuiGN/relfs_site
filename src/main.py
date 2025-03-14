import flet as ft


def main(page: ft.Page):
    page.title = "Relf's Recife Moda Fitness"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    def create_app_bar():
        return ft.AppBar(
            title=ft.Text(
                value="Relf's Recife Moda Fitness",
                color=ft.Colors.BLUE_100,
                weight=ft.FontWeight.BOLD,
                size=16,
            ),
            center_title=True,
            bgcolor='#972486',
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text='Nossas Roupas', on_click=lambda _: page.go('/')),
                        ft.PopupMenuItem(text='APP para Android', on_click=lambda _: page.go('/app')),
                        ft.PopupMenuItem(text='Contato', on_click=lambda _: page.go('/contato'))
                    ],
                    tooltip='Menu',
                ),
            ]
        )

    def create_bottom_app_bar():
        return ft.BottomAppBar(
            content=ft.Row(
                [
                    ft.Text(
                        value="Copyright © 2025 Relf's Recife Moda Fitness",
                        color=ft.Colors.BLUE_100,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor='#972486',
            height=50,
            elevation=50,
            shadow_color=ft.Colors.BLUE_100,
        )

    def create_home_gridview():
        grid_view_images_home = ft.GridView(
            runs_count=5,
            max_extent=250,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
            expand=True,
        )

        for i in range(1, 50):
            grid_view_images_home.controls.append(
                ft.Image(
                    src=f'images/{i}.png',
                    fit=ft.ImageFit.FIT_WIDTH,
                    height=200,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                ),
            )
        return grid_view_images_home

    def create_info_text():
        return ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(
                                    src='icon.png',
                                    fit=ft.ImageFit.FIT_WIDTH,
                                    height=300,
                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                ),
                                padding=10,
                                margin=5,
                                expand=True,
                            ),
                            ft.Text(
                                value="Relf's Recife Moda Fitness",
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.BODY_LARGE,
                                color=ft.Colors.BLUE_100,
                            ),
                            ft.Text(
                                value='@relfsmodarecife',
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.BODY_LARGE,
                                color=ft.Colors.BLUE_100
                            ),
                            ft.Text(
                                value='(81) 98851-8601',
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.BODY_LARGE,
                                color=ft.Colors.BLUE_100
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.AUTO,
                    ),
                ],
            ),
            padding=10,
            margin=5,
        )

    def create_app_tab():

        def download_apk(e):
            apk_url = 'https://www.relfsmodafitness.com.br/relfsmodafitness.apk'
            page.launch_url(apk_url)

        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.ResponsiveRow(
                            [
                                ft.Container(
                                    ft.Image(
                                        src='images/android_app.jpeg',
                                        fit=ft.ImageFit.FIT_WIDTH,
                                        height=200,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                        border_radius=ft.border_radius.all(10),
                                    ),
                                    alignment=ft.alignment.center,
                                    border=ft.border_radius.all(10),
                                    margin=10,
                                    padding=5,
                                ),
                                ft.Container(
                                    ft.Text(
                                        value='Acesse nosso catálogo de produtos e faça seu pedido através do nosso APP para Android',
                                        text_align=ft.TextAlign.CENTER,
                                        theme_style=ft.TextThemeStyle.BODY_LARGE,
                                        color=ft.Colors.BLUE_100,
                                    ),
                                    alignment=ft.alignment.center,
                                    margin=5,
                                    padding=10,
                                ),
                                ft.Container(
                                    ft.ElevatedButton(
                                        text='Download do APP para Android',
                                        icon=ft.Icons.DOWNLOAD,
                                        icon_color=ft.Colors.BLUE_100,
                                        bgcolor='#972486',
                                        on_click=download_apk,
                                    ),
                                    alignment=ft.alignment.center,
                                ),
                            ]
                        ),
                        padding=5,
                        expand=True,
                        adaptive=True,
                        alignment=ft.alignment.center,
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=10,
            margin=5,
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                '/',
                [
                    create_app_bar(),
                    create_home_gridview(),
                    create_bottom_app_bar()
                ],
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                scroll=ft.ScrollMode.ALWAYS,
            )
        )
        if page.route == '/app':
            page.views.append(
                ft.View(
                    '/app',
                    [
                        create_app_bar(),
                        create_app_tab(),
                        create_bottom_app_bar()
                    ],
                    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                    scroll=ft.ScrollMode.ALWAYS,
                )
            )
        if page.route == '/contato':
            page.views.append(
                ft.View(
                    '/contato',
                    [
                        create_app_bar(),
                        create_info_text(),
                        create_bottom_app_bar()
                    ],
                    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                    scroll=ft.ScrollMode.ALWAYS,
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir='assets', view=ft.AppView.FLET_APP_WEB)
