import reflex as rx

config = rx.Config(
    app_name="Milestone_1",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)