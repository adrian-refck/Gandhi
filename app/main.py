import streamlit as st

st.title("Willkommen zu Gandhis Leben")
 
col1, col2, col3 = st.columns(3)

with col1:
    auswhal1 = st.bottom("Audioinformation", type="primary" , width="stretch")

with col2:
    auswahl2 = st.bottom("Testinformationen" , type="primary" , width="stretch")

with col3:
    auswahl3 = st.bottom("Quiz" , type="primary" , width="stretch")

if auswhal1:
    st.write("Lade Audioinformationen...")
    st.audio("audio/gandhi.mp3")

if auswahl2:
    st.write("Lade Testinformationen...")
    st.header("Stationen seines Lebens")
    st.subheader("Kindheit + Studium")
    st.write("Mohandas Karamchand Gandhi, geboren am 2. Oktober 1869 in Porbandar im heutigen Bundesstaat Gujarat (Westindien), stammte aus einer wohlhabenden Familie, die im Dienst eines Lokalfürsten stand. Seine Mutter war tief religiös und prägte ihn stark. Nach einer wenig erfolgreichen Schulzeit ging er 1888 nach London, um Jura zu studieren. Dort versuchte er vergeblich, sich dem Lebensstil der britischen Oberschicht anzupassen. 1891 kehrte er nach dem Examen nach Indien zurück, konnte sich jedoch in Bombay wegen seiner Schüchternheit und Nervosität nicht als Anwalt etablieren.")
    st.image("https://www.bpb.de/cache/images/0/327610_galerie_lightbox_box_1000x666.jpg?93070")
    st.subheader("Zeit in Afrika")
    st.write("1893 erhielt er durch seinen Bruder den Auftrag, einen Rechtsfall in Südafrika zu übernehmen. Dort erlebte er massive Diskriminierung gegenüber Indern und blieb insgesamt 21 Jahre. Er beschäftigte sich mit den Schriften von Thoreau, Ruskin und Tolstoi, was seine Philosophie der Wahrheit und Gewaltfreiheit beeinflusste. 1904 gründete er die Phoenix-Siedlung bei Durban, die später in die Tolstoi-Farm überging – beides kommunitäre Gemeinschaften mit einfachem, selbstversorgendem Leben. Gandhis gewaltfreie Protestaktionen gegen diskriminierende Gesetze waren erfolgreich, z. B. bei der Abschaffung der Kopfsteuer")
    st.image("https://www.bpb.de/cache/images/3/227933_original.jpg?5837F")