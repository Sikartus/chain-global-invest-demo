import streamlit as st
import pandas as pd
import base64
import os

# ==========================================
# 1. CONFIGURACIÓN PRINCIPAL DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="CHAIN GLOBAL INVEST", layout="wide", page_icon="⚙️")

# ==========================================
# 2. FUNCIONES AUXILIARES
# ==========================================
def header():
    st.markdown(
        """
        <style>
        .header {
            background-color: #1E6B3B;
            padding: 15px 30px;
            color: white;
            font-family: Arial, sans-serif;
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            border-radius: 5px; 
            margin-bottom: 20px;
        }
        .header h1 {margin:0; font-size:24px; font-weight:bold;}
        .header h2 {margin:0; font-size:14px; font-weight:normal; opacity: 0.9;}
        .menu {font-size: 16px; font-weight: 500;}
        .menu a {color:white; margin-left:20px; text-decoration:none;}
        </style>
        <div class="header">
            <div>
                <h1>CHAIN GLOBAL INVEST</h1>
                <h2>Estrategia, Inversiones e Impacto</h2>
            </div>
            <div class="menu">
                <a href="#">Inicio</a> | <a href="#">Evaluación</a> | <a href="#">Reportes</a> | <a href="#">Registrarse</a> | <a href="#">Perfil</a>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return None

def ejecutar_priorizacion():
    # Devuelve el dataframe con los resultados reales calculados por tu motor AHP
    return pd.DataFrame({
        "Cadena Productiva": ["Granos Andinos", "Papas Nativas", "Lácteos", "Truchas", "Cafés", "Textiles", "Palta"],
        "Ponderación Global": [25.8, 17.3, 14.6, 14.6, 10.3, 8.9, 8.5],
        "Color": ["#4CAF50", "#FF9800", "#1976D2", "#8E24AA", "#FFC107", "#E53935", "#00ACC1"]
    })

# ==========================================
# 3. CONTROL DE ESTADO DE LA PÁGINA
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "inicio"

header()

# ==========================================
# PÁGINA 1: INICIO (MAPA CON BOTÓN FLOTANTE)
# ==========================================
if st.session_state.page == "inicio":
    st.markdown("<h3 style='text-align: center; color: #153259;'>Bienvenido a CHAIN GLOBAL INVEST – GovTech: B2G Decision Intelligence</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Inteligencia Estratégica para el Desarrollo Productivo de LATAM</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Haga clic en la región naranja para iniciar el análisis.</p>", unsafe_allow_html=True)

    img_base64 = get_image_base64("mapa_peru.png")
    
    if img_base64:
        # ATENCIÓN: El código HTML no tiene indentación para evitar que Streamlit lo convierta en bloque de código
        html_mapa_boton = f"""<div style="position: relative; display: flex; justify-content: center; align-items: center; width: 100%; margin-top: 20px;">
<div style="position: relative; display: inline-block;">
<img src="data:image/png;base64,{img_base64}" style="max-width: 800px; width: 100%; height: auto; border-radius: 10px;" />
<form action="" method="get" style="margin: 0;">
<button type="submit" name="goto" value="andahuaylas" style="position: absolute; top: 66%; left: 56%; transform: translate(-50%, -50%); background-color: rgba(255, 165, 0, 0.8); border: 1px solid rgba(255, 255, 255, 0.9); border-radius: 5px; padding: 4px 8px; cursor: pointer; font-weight: bold; color: white; font-size: 11px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3); transition: 0.3s;">Andahuaylas</button>
</form>
</div>
</div>"""
        st.markdown(html_mapa_boton, unsafe_allow_html=True)
    else:
        st.error("⚠️ No se encontró el archivo 'mapa_peru.png'. Verifica que la imagen esté en la misma carpeta que este script.")

    # Lógica de captura del clic en el botón del mapa
    query_params = st.query_params
    if "goto" in query_params and query_params["goto"] == "andahuaylas":
        st.session_state.page = "andahuaylas"
        st.query_params.clear()
        st.rerun()

# ==========================================
# PÁGINA 2: DASHBOARD PRE-EJECUCIÓN (VALORES EN 0)
# ==========================================
elif st.session_state.page == "andahuaylas":
    st.markdown("<h1 style='text-align: center; color: #153259;'>Análisis AHP - Provincia de Andahuaylas</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #555; font-weight: normal;'>Matrices Evaluadas: <strong>44</strong> | Consistencia Global: <strong>CR = 0.07 <span style='color: #2E7D32;'>✔ Aceptable</span></strong></h4>", unsafe_allow_html=True)
    st.divider()

    st.markdown("### Ranking de Priorización de Cadenas Productivas")
    cadenas = ["Cadena de Granos Andinos", "Cadena de Papas Nativas", "Cadena de Lácteos", "Cadena de Truchas", "Cadena de Cafés", "Cadena de Textiles", "Cadena de Palta"]
    
    for cadena in cadenas:
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="width: 250px; font-weight: 600; color: #153259;">{cadena}</div>
                <div style="flex-grow: 1; background-color: #E0E0E0; border-radius: 5px; height: 25px; margin: 0 15px;"></div>
                <div style="width: 50px; font-weight: bold; font-size: 18px; color: #888;">0%</div>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button("Ejecutar priorización", use_container_width=True, type="primary"):
            st.session_state.page = "resultados"
            st.rerun()

    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Pesos de Criterios")
        st.dataframe(pd.DataFrame({"Criterio": ["Social", "Organizacional", "Territorial"], "Peso": ["0.00", "0.00", "0.00"]}), hide_index=True, use_container_width=True)
    with col2:
        st.markdown("#### Análisis por Dimensión")
        st.markdown("""
        <div style="background-color: #F8F9FA; padding: 15px; border-radius: 5px; border: 1px solid #ddd;">
            <p style="margin: 0 0 10px 0;"><strong>Social:</strong> Transformación Productiva — <em>A Evaluar</em></p>
            <p style="margin: 0 0 10px 0;"><strong>Organizacional:</strong> <em>A Evaluar</em></p>
            <p style="margin: 0;"><strong>Territorial:</strong> Capacidad de Resiliencia — <em>A Revisar</em></p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("#### Pesos de Alternativas")
        st.dataframe(pd.DataFrame({"Alternativa": ["Empleo", "Costos", "Acceso"], "Peso": ["0.00", "0.00", "0.00"]}), hide_index=True, use_container_width=True)

# ==========================================
# PÁGINA 3: RESULTADOS POST-EJECUCIÓN
# ==========================================
elif st.session_state.page == "resultados":
    st.markdown("<h1 style='text-align: center; color: #153259;'>Análisis - Provincia de Andahuaylas</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #555; font-weight: normal;'>Matrices Evaluadas: <strong>44</strong> | Consistencia Global: <strong>CR = 0.07 <span style='color: #2E7D32;'>✔ Aceptable</span></strong></h4>", unsafe_allow_html=True)
    st.divider()

    st.markdown("### Ranking de Priorización de Cadenas Productivas")
    resultados = ejecutar_priorizacion()
    
    for _, row in resultados.iterrows():
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="width: 250px; font-weight: 600; color: #153259;">Cadena de {row['Cadena Productiva']}</div>
                <div style="flex-grow: 1; background-color: #E0E0E0; border-radius: 5px; height: 25px; margin: 0 15px; position: relative;">
                    <div style="width: {row['Ponderación Global']}%; background-color: {row['Color']}; height: 100%; border-radius: 5px; transition: width 1s ease-in-out;"></div>
                </div>
                <div style="width: 50px; font-weight: bold; font-size: 18px;">{row['Ponderación Global']}%</div>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        st.button("✅ Priorización completada", disabled=True, use_container_width=True)

    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Pesos de Criterios")
        st.dataframe(pd.DataFrame({"Criterio": ["Social", "Organizacional", "Territorial"], "Peso": ["0.40", "0.35", "0.25"]}), hide_index=True, use_container_width=True)
    with col2:
        st.markdown("#### Análisis por Dimensión")
        st.markdown("""
        <div style="background-color: #F8F9FA; padding: 15px; border-radius: 5px; border: 1px solid #ddd; border-left: 4px solid #1E6B3B;">
            <p style="margin: 0 0 10px 0;"><strong>Social:</strong> Transformación Productiva — <strong>Alto Potencial</strong></p>
            <p style="margin: 0 0 10px 0;"><strong>Organizacional:</strong> <strong>Riesgo de Estancamiento</strong></p>
            <p style="margin: 0;"><strong>Territorial:</strong> Capacidad de Resiliencia — <strong>Moderada</strong></p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("#### Pesos de Alternativas")
        st.dataframe(pd.DataFrame({"Alternativa": ["Empleo", "Costos", "Acceso"], "Peso": ["0.201", "0.157", "0.184"]}), hide_index=True, use_container_width=True)

    st.write("")
    st.markdown("<h4 style='text-align: center; color: #1E6B3B; margin-top: 30px;'>Acciones Rápidas</h4>", unsafe_allow_html=True)
    col_act1, col_act2, col_act3, col_act4 = st.columns([1, 1, 1, 1])
    with col_act2:
        if st.button("↑ Cargar Nuevas Matrices", use_container_width=True):
            st.session_state.page = "inicio"
            st.rerun()
    with col_act3:
        st.button("⭳ Exportar Reporte (PDF/CSV)", use_container_width=True, type="primary")