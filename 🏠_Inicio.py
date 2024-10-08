import streamlit as st
import os
import pandas as pd
from index_generator import generate_index_from_scratch
from file_utils import rename_files
from excel_handler import save_excel_file
import base64
import tempfile

# Configuración de Streamlit
st.set_page_config(
    page_title="Sistema de Gestión de Expedientes Electrónicos Judiciales",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state='expanded',    
    menu_items={
        'Get Help': 'https://alexander.oviedo.isabellaea.com/',
        'Report a bug': 'https://github.com/bladealex9848/GestionExpedienteElectronico/issues',
        'About': "El Sistema de Gestión de Expedientes Electrónicos Judiciales es una herramienta para generar índices electrónicos de expedientes judiciales, cumpliendo con los estándares establecidos por el Consejo Superior de la Judicatura."
    }
)

def mostrar_vision_general():
    st.header("Bienvenido al Sistema de Gestión de Expedientes Electrónicos Judiciales")
    
    st.write("""
    Este sistema integral está diseñado para optimizar y digitalizar la gestión de expedientes judiciales, 
    cumpliendo con los estándares establecidos por el Consejo Superior de la Judicatura de Colombia.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Objetivo")
        st.write("""
        - Facilitar la generación de índices electrónicos de expedientes judiciales.
        - Cumplir con las normativas y protocolos judiciales colombianos.
        - Mejorar la eficiencia y precisión en la gestión documental.
        - Ofrecer una solución adaptable a diferentes volúmenes de expedientes.
        """)
    with col1:
        st.subheader("🌟 Características Principales")
        st.write("""
        - Generación automatizada de índices electrónicos
        - Compatibilidad con múltiples formatos de archivo
        - Interfaz intuitiva y fácil de usar
        - Cumplimiento de normativas judiciales colombianas
        - Versiones para diferentes necesidades: Lite, Ultimate y Web
        """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📚 Recursos Adicionales")
        st.write("""
        - Plantilla Excel para índices electrónicos
        - Guía de uso detallada
        - Documentación técnica completa
        """)

        st.subheader("📋 Marco Normativo")
        st.write("""
        Acceso directo a documentos clave:
        - ACUERDO PCSJA20-11567
        - ACUERDO PCSJA23-12094
        - CIRCULAR PCSJC24-23
        - Plan Sectorial de Desarrollo Rama Judicial 2023-2026
        - Protocolo para la gestión de documentos electrónicos
        - ABC Expediente Judicial Electrónico
        """)

    with col2:
        st.subheader("💻 Versiones Disponibles")
        st.write("""
        1. **Versión Lite**: 
           - Ideal para volúmenes moderados
           - Procesamiento de una carpeta a la vez
           - Interfaz gráfica intuitiva

        2. **Versión Ultimate**:
           - Procesamiento masivo de expedientes
           - Manejo avanzado de metadatos
           - Compatibilidad con estructuras complejas

        3. **Versión Web**:
           - Acceso desde cualquier navegador
           - Ideal para pruebas y capacitación
           - No requiere instalación
        """)

    st.subheader("📊 Funcionalidades Adicionales")
    st.write("""
    - **Hoja de Ruta**: Visualiza el progreso de implementación del sistema.
    - **Experto en Expediente Electrónico**: Asistente virtual para resolver dudas.
    - **Informe Consolidado SIUGJ**: Análisis detallado de la alineación con el Sistema Integrado Único de Gestión Judicial.
    """)

    st.subheader("🚀 ¿Por qué elegir nuestro sistema?")
    st.write("""
    1. **Eficiencia**: Automatiza tareas repetitivas y reduce errores.
    2. **Cumplimiento**: Garantiza el seguimiento de normativas y protocolos judiciales.
    3. **Flexibilidad**: Adaptable a diferentes volúmenes y tipos de expedientes.
    4. **Soporte**: Documentación completa y asistencia técnica disponible.
    5. **Innovación**: Constantemente actualizado para satisfacer las necesidades cambiantes del sistema judicial.
    """)

    st.info("Explora las pestañas para acceder a cada funcionalidad y descubre cómo nuestro sistema puede transformar tu gestión de expedientes judiciales.")

def get_binary_file_downloader_html(url, file_label='File'):
    href = f'<a href="{url}" target="_blank">Descargar {file_label}</a>'
    return href

def main():
    # Sidebar
    st.sidebar.title("Recursos Adicionales")
    with st.sidebar.expander("Ver Recursos Adicionales", expanded=False):
        st.markdown(get_binary_file_downloader_html("https://enki.care/IndiceElectronicoC0", 'Plantilla Excel'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/GestionExpedienteElectronicoGuiaUso", 'Guía de Uso'), unsafe_allow_html=True)

    st.sidebar.title("Marco Normativo")
    with st.sidebar.expander("Ver Marco Normativo", expanded=False):
        st.markdown(get_binary_file_downloader_html("https://enki.care/PCSJA20-11567", 'ACUERDO PCSJA20-11567'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/PCSJA23-12094", 'ACUERDO PCSJA23-12094'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/PCSJC24-23", 'CIRCULAR PCSJC24-23'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/PlanSectorialDesarrolloRamaJudicial2023-2026", 'Plan Sectorial de Desarrollo Rama Judicial 2023-2026'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/seccion-de-gestion-documental", 'División de Gestión Documental'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/gestion-de-documentos-electronicos", 'Gestión de documentos electrónicos'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/ProtocoloGestionDocumentosElectronicos", 'Protocolo para la gestión de documentos electrónicos'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://enki.care/ABCExpedienteJudicialElectronicoV6", 'ABC Expediente Judicial Electrónico'), unsafe_allow_html=True)        

    st.sidebar.markdown("---")
    st.sidebar.image("assets/logo_CSJ_Sucre.png", width=200)
    st.sidebar.write("<div style='text-align: center;'>Desarrollado por Equipo Marduk</div>", unsafe_allow_html=True)
    st.sidebar.write("<div style='text-align: center;'>v.1.3.3 Lite | v.1.3.0 Ultimate</div>", unsafe_allow_html=True)
    st.sidebar.write("<div style='text-align: center;'><a href='https://github.com/bladealex9848'>GitHub Lite</a> | <a href='https://github.com/HammerDev99'>GitHub Ultimate</a> | <a href='https://marduk.pro/'>Website</a></div>", unsafe_allow_html=True)

    # Main content
    st.title("Sistema de Gestión de Expedientes Electrónicos Judiciales")
    
    st.write("""
    [![ver código fuente](https://img.shields.io/badge/Repositorio%20GitHub-gris?logo=github)](https://github.com/bladealex9848/GestionExpedienteElectronico)
    ![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgestionexpedienteelectronico.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)
    """)
    
    # Tabs para las diferentes versiones
    tab0, tab1, tab2, tab3 = st.tabs(["Visión General", "Versiones de Escritorio", "Versión Web", "Instrucciones de Uso"])

    with tab0:
        mostrar_vision_general()

    with tab1:
        st.header("Versión Lite")
        st.write("""
        Ideal para procesar una carpeta a la vez. Perfecta para usuarios que manejan volúmenes moderados de expedientes.
        
        **Características:**
        - Interfaz gráfica intuitiva
        - Procesamiento de una carpeta a la vez
        - Renombrado automático de archivos
        - Generación de índice electrónico en formato Excel
        - Compatible con Windows, macOS y Linux
        """)
        st.markdown(get_binary_file_downloader_html("https://enki.care/GestionExpedienteElectronicoWindows", 'Versión Lite'), unsafe_allow_html=True)
        
        with st.expander("Instrucciones de Uso - Versión Lite"):
            st.write("""
            1. Descargue la herramienta en versión portable desde el enlace proporcionado.
            2. Abra la herramienta.
            3. Seleccione la carpeta del expediente que contiene los archivos sin renombrar.
            4. Haga clic en "Generar Índice".
            5. Espere a que el proceso termine.
            6. Verifique la carpeta del expediente:
               - Compruebe que se ha creado el archivo "000IndiceElectronicoC01.xlsm"
               - Confirme que los archivos han sido renombrados según el protocolo.
            """)

    with tab2:
        st.header("Versión Ultimate")
        st.write("""
        Capacidad de procesamiento masivo. Diseñada para usuarios que necesitan manejar grandes volúmenes de expedientes simultáneamente.
        
        **Características:**
        - Procesamiento de múltiples carpetas y expedientes
        - Uso de plantillas predefinidas y macros para insertar filas
        - Manejo avanzado de metadatos
        - Compatibilidad con estructuras de carpetas complejas
        - Conteo de páginas para cualquier tipo de archivo
        - Ajustes para integración con Alfresco
        - Requiere Python 3.9 y bibliotecas específicas
        """)
        st.markdown(get_binary_file_downloader_html("https://enki.care/GestionExpedienteElectronicoUltimate", 'Versión Ultimate'), unsafe_allow_html=True)
        
        with st.expander("Instrucciones de Uso - Versión Ultimate"):
            st.write("""
            1. Descargue las carpetas que contienen los archivos, sin incluir ningún índice.
            2. Asegúrese de que cada carpeta de expediente esté nombrada con el radicado de 23 dígitos.
            3. Verifique que los metadatos de los archivos sean consistentes con los documentos originales.
            4. Cierre cualquier archivo de Excel abierto antes de ejecutar el programa.
            5. La estructura de carpetas debe ser: carpeta_seleccionada/subcarpeta/archivos_para_indice
            6. Ejecute el programa y seleccione la carpeta principal que contiene todos los expedientes.
            7. El procesamiento comenzará automáticamente.
            8. Verifique los resultados en cada carpeta de expediente procesada.
            """)

    with tab3:
        st.header("Versión Web de Entrenamiento")
        st.write("Esta versión en línea permite generar el índice electrónico de expedientes judiciales.")

        uploaded_files = st.file_uploader("Seleccione los archivos que contienen los documentos del expediente:", type=None, accept_multiple_files=True)

        if uploaded_files:
            with tempfile.TemporaryDirectory() as temp_folder:
                for uploaded_file in uploaded_files:
                    with open(os.path.join(temp_folder, uploaded_file.name), "wb") as f:
                        f.write(uploaded_file.getbuffer())
                
                st.success("Archivos seleccionados correctamente.")
                
                if st.button("Generar Índice Electrónico"):
                    progress_bar = st.progress(0)
                    try:
                        rename_files(temp_folder)
                        progress_bar.progress(33)
                        
                        df = generate_index_from_scratch(temp_folder)
                        if df is None:
                            raise ValueError("La generación del índice falló.")
                        
                        progress_bar.progress(66)
                        
                        index_file_path = os.path.join(temp_folder, "000IndiceElectronicoC0.xlsx")
                        save_excel_file(df, index_file_path, use_template=False)
                        
                        progress_bar.progress(100)
                        st.success("Índice electrónico generado con éxito.")
                        
                        with open(index_file_path, "rb") as f:
                            st.download_button(label='Descargar Índice Electrónico', data=f, file_name=os.path.basename(index_file_path), mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    
                    except Exception as e:
                        st.error(f"Ocurrió un error: {str(e)}")

        # Instrucciones de uso
        with st.expander("Instrucciones de Uso - Versión Web"):
            st.write("""
            1. Seleccione los archivos que contienen los documentos del expediente utilizando el botón de carga.
            2. Una vez cargados los archivos, haga clic en "Generar Índice Electrónico".
            3. Espere a que el proceso termine.
            4. Descargue el índice generado.
            5. Utilice el índice como guía para renombrar manualmente los archivos dentro de la carpeta del expediente en su computadora local.
            """)   

if __name__ == "__main__":
    main()
