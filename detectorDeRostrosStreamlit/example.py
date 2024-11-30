import flet as ft

def main(page: ft.Page):
    page.title = "Detección de rostros"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def detectar_en_tiempo_real(e):
        result.value = "Detectando rostros en tiempo real..."
        page.update()
        # Aquí iría la lógica de detección en tiempo real
        # Implementar con librerías como OpenCV o similar
        result.value = "¡Detección en tiempo real completada!"
        page.update()

    def detectar_por_imagen(e):
        result.value = "Cargando imagen para detección..."
        page.update()
        # Aquí se implementa la detección a partir de imágenes cargadas
        result.value = "¡Detección completada desde la imagen!"
        page.update()

    def crear_set_datos(e):
        result.value = "Creando un nuevo set de datos..."
        page.update()
        # Aquí puedes implementar la lógica para generar un dataset
        result.value = "¡Set de datos creado exitosamente!"
        page.update()

    # Etiqueta principal
    title = ft.Text("Selecciona una opción:", size=30, weight=ft.FontWeight.BOLD)

    # Botones de opción
    option_real_time = ft.Radio(value="real_time", label="Detectar rostros en tiempo real")
    option_from_image = ft.Radio(value="from_image", label="Detectar rostros subiendo una imagen")
    option_dataset = ft.Radio(value="dataset", label="Crear nuevo set de datos")
    options_group = ft.RadioGroup(content=[option_real_time, option_from_image, option_dataset])

    # Botón para ejecutar según selección
    execute_button = ft.ElevatedButton(
        "Ejecutar",
        on_click=lambda e: detectar_en_tiempo_real(e) if options_group.value == "real_time" else
                           detectar_por_imagen(e) if options_group.value == "from_image" else
                           crear_set_datos(e)
    )

    # Etiqueta para mostrar el resultado
    result = ft.Text("", size=18, weight=ft.FontWeight.NORMAL)

    # Agregar componentes a la página
    page.add(
        title,
        options_group,
        execute_button,
        result
    )

# Corre la aplicación
if __name__ == "__main__":
    ft.app(target=main)
