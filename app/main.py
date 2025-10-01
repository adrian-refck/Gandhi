import streamlit as st


with st.sidebar:
    st.title("Quellen")
    st.markdown("https://www.bpb.de/themen/asien/indien \[...\] 24.9.2025")



st.title("Willkommen zu Gandhis Leben")
 
col1, col2, col3 = st.columns(3)

with col1:
    auswahl1 = st.bottom("Audioinformation", type="primary" , width="stretch")

with col2:
    auswahl2 = st.bottom("Testinformationen" , type="primary" , width="stretch")

with col3:
    auswahl3 = st.bottom("Quiz" , type="primary" , width="stretch")

if auswahl1:
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
    st.subheader("Zurück in Indien")
    st.write("1915 kehrte Gandhi nach Indien zurück und wurde bald zur zentralen Figur der Unabhängigkeitsbewegung, die unter seiner Führung zu einer Massenbewegung wurde. Am 15. August 1947 wurde Indien unter dramatischen Umständen unabhängig, allerdings verbunden mit der Teilung in Indien und Pakistan. Am 30. Januar 1948 wurde Gandhi von dem Hindufanatiker Nathuram Godse erschossen.")
    st.image("https://www.bpb.de/cache/images/3/227933_original.jpg?5837F")
    
    st.header("Politisches Wirken")
    st.write("Mahatma Gandhi war eine bedeutende Persönlichkeit im Kampf für die Unabhängigkeit Indiens vom Britischen Empire. Seine politischen Prinzipien basierten auf Gewaltlosigkeit (Ahimsa) und zivilem Ungehorsam (Satyagraha). Nach seiner juristischen Ausbildung in London lebte er in Südafrika, wo er gegen die Diskriminierung der indischen Minderheit kämpfte und seine Philosophie des gewaltfreien Widerstands entwickelte. 1915 kehrte er nach Indien zurück und brachte diese Ideen in den Unabhängigkeitskampf ein.Gandhi organisierte zahlreiche Kampagnen gegen soziale Ungerechtigkeit, wirtschaftliche Ausbeutung und die britische Kolonialherrschaft, darunter den Salzmarsch von 1930 als Symbol des gewaltfreien Widerstands. Er setzte sich auch für soziale Reformen ein, kämpfte gegen das Kastensystem und für die Rechte von Frauen, ländliches Leben sowie religiöse Toleranz.Trotz mehrerer Inhaftierungen blieb Gandhi seinen Prinzipien treu und trug maßgeblich zur indischen Unabhängigkeit am 15. August 1947 bei. Die anschließende Teilung Indiens und Pakistans, begleitet von blutigen Konflikten, enttäuschte ihn sehr. Er versuchte bis zu seiner Ermordung 1948, zwischen den Religionen zu vermitteln. Gandhis politisches Wirken beeinflusste weltweit viele Bewegungen und Persönlichkeiten und gilt bis heute als Symbol für friedlichen Widerstand und den Glauben an Wahrheit und Gerechtigkeit.")
    st.image("https://www.hanisauland.de/system/files/17705.jpg")
    
    st.header("Denkweise")
    st.subheader("Herkunft der Phylosophie")
    st.write("Gandhis Denken wurzelt tief in der hinduistischen Tradition, wurde aber stark von europäischen Einflüssen geprägt, insbesondere durch christliche und liberale Ideen – vor allem deren Aufforderung, Feinde zu lieben und Gewalt nicht zu erwidern. Gandhi übernahm dabei nur die für ihn sinnvollen Elemente und betrachtete sich nicht als Urheber einer neuen Lehre.")
    st.image("https://media04.meinbezirk.at/article/2013/11/27/8/4543038_XXL.jpg")
    st.subheader("Prinzip der Wahrheit")
    st.write("1. Zentral für Gandhi ist das Prinzip der Wahrheit , die als ewiges, einzig reales Sein und als Name Gottes verstanden wird. Wahrheit ist die Grundlage allen Lebens, und Gott durchdringt alles – Mensch, Natur, Materie und Geist bilden eine untrennbare göttliche Einheit. Leben ist göttliches Leben, über das Menschen nicht beliebig verfügen können. Hingabe an die Wahrheit ist für Gandhi die Rechtfertigung der menschlichen Existenz.")
    
    st.header("Wirkund und Vermächtnis")
    st.subheader("Das Constructive Programm")
    st.write("Gandhi verfasste 1941 und 1945 sein „Constructive Programme“, in dem er konkrete Vorstellungen für den Aufbau der Dörfer formulierte. Dazu gehörten Achtung und Toleranz gegenüber anderen, die Abschaffung der Unberührbarkeit, Förderung des dörflichen Handwerks, Bildung, sanitäre Einrichtungen, Gleichstellung der Frau und wirtschaftliche Gleichheit. Für Gandhi war dieses Programm der gewaltfreie und wahre Weg zur vollständigen Unabhängigkeit Indiens.")
    st.image("https://www.bpb.de/cache/images/2/327612_galerie_lightbox_box_1000x666.jpg?83411")
    st.subheader("Probleme")
    st.write("Die Unabhängigkeit führte jedoch zur Teilung Indiens in die Indische Union und das muslimische Pakistan, begleitet von schweren Unruhen, bei denen etwa eine Million Menschen starben und über 15 Millionen zu Flüchtlingen wurden. Gandhi erlebte dies als persönliche Tragödie. Trotz aller Bemühungen, besonders in den gewaltgeprägten Zentren wie Kalkutta, konnte er die Gewalt nicht stoppen. Er wertete dieses Scheitern als persönliches Versagen, glaubte aber weiterhin an die unveränderliche Gültigkeit der Prinzipien von Wahrheit (satya) und Gewaltfreiheit (ahimsa), da die Wahrheit ewig und unzerstörbar sei.")

if auswahl3:
    st.write("Lade Quiz...")
    st.header("Quiz zu Gandhis Leben")
    frage1 = st.radio(
        "In welchem Jahr wurde Mahatma Gandhi geboren?",
        ("1869", "1879", "1889", "1899")
    )
    if frage1 == "1869":
        st.write("Richtig! Gandhi wurde 1869 geboren.")
    else:
        st.write("Falsch. Die richtige Antwort ist 1869.")

    frage2 = st.radio(
        "Wo studierte Gandhi Jura?",
        ("Oxford", "Cambridge", "Harvard", "London")
    )
    if frage2 == "London":
        st.write("Richtig! Gandhi studierte in London.")
    else:
        st.write("Falsch. Die richtige Antwort ist London.")

    frage3 = st.radio(
        "In welchem Land erlebte Gandhi Diskriminierung, die seine Philosophie prägte?",
        ("Indien", "Südafrika", "USA", "Australien")
    )
    if frage3 == "Südafrika":
        st.write("Richtig! Gandhi erlebte Diskriminierung in Südafrika.")
    else:
        st.write("Falsch. Die richtige Antwort ist Südafrika.")

    frage4 = st.radio(
        "Welches Prinzip war zentral für Gandhis Philosophie?",
        ("Gewaltlosigkeit", "Reichtum", "Macht", "Krieg")
    )
    if frage4 == "Gewaltlosigkeit":
        st.write("Richtig! Gewaltlosigkeit war zentral für Gandhis Philosophie.")
    else:
        st.write("Falsch. Die richtige Antwort ist Gewaltlosigkeit.")

    frage5 = st.radio(
        "Wann wurde Indien unabhängig?",
        ("1945", "1946", "1947", "1948")
    )
    if frage5 == "1947":
        st.write("Richtig! Indien wurde 1947 unabhängig.")
    else:
        st.write("Falsch. Die richtige Antwort ist 1947.")