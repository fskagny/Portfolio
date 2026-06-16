import streamlit as st
st.header("Fa Seny Kagny")
st.write("**Geographe spéciialisé en Climatologie et Technicien Supérieur en Geomatique**")

st.divider()

#Formation
st.header("Formation")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Diplomes")
    st.success("**Master** en Geographie option Climatologie")
    st.write("Université: UCAD")
    st.success("**BTS Géomatique** ")
    st.write("Centre de Formation: CEDT Le G15")
    st.success("**Licence en géographie**")
    st.write("Université: UCAD")
    st.success("**Baccalauréat**")
    st.write("Etablissement: Lycée Samba Dione de Gandiaye")

with col2:
    st.subheader("Cértification")
    st.success("**Cértificat en Commerce digital**")
    
    


with st.sidebar:
    
    #Informations personnelles
    st.header("Information personnelles")
    st.write("**Email**: fskagny@gmail.com")
    st.write("**Addresse**: Rue 10/Pikine")
    
    st.write("**Nationalité**: Sénégalaise")
    st.write("**Réseau Sociaux**: Fa Seny Kagny")
   
    st.divider()

    #Compétences
    st.header("Compétences")
    st.progress(90, text="Analyse Climatique")
    st.progress(65, text="Cobo Collecte")
    st.progress(75, text="Numérisation")
    st.progress(85, text="Outils SIG(Qgis, Arcgis)")
    st.progress(80, text="Aménagement du Territoire")
    st.progress(75, text="Outils Collaboratif microsoft")
    st.progress(75, text="Dessin de plan avec Auto Cad")
    
   
    
    st.divider()

    #Langues
    st.header("Langues")
    st.markdown("""
    * Francais: Avancé """)
    st.markdown("""
    * Anglais: Intermédiaire """)
    
    
    st.divider()

    #Centre d'Interet
    st.header("Centre d'interet")
    st.markdown("""
    * L'environnement""")
