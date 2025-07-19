import streamlit as st
from PIL import Image

# Seiteneinstellungen
st.set_page_config(page_title="Singen in Friedenau", page_icon="🎶", layout="centered")

# ✅ CSS: Hintergrundfarbe für Hauptbereich
st.markdown("""
    <style>
    .stApp {
        background-color: #fffaf0;
    }
    </style>
    """, unsafe_allow_html=True)



# Logo anzeigen
logo = Image.open("logo.png")
st.image(logo, width=250)

# Titel & Einführung
st.title("Gemeinsam singen in Friedenau")
st.write("Willkommen! Hier findest du alle Termine unserer Veranstaltung sowie die Kontaktdaten zur Anmeldung.")

# ❓ Beschreibung der Veranstaltung
st.subheader("🎶 Sing Dein Herz- Singen verbindet, heilt und öffnet")
st.write("""
Wir singen gemeinsam deutsche Lieder, Mantren, spirituelle Lieder und Herzenslieder aus aller Welt.
Die Lieder haben einfache, meist kurze Texte und eingängige Melodien, die zum Mitsingen einladen. 
Es sind keine besonderen Vorkenntnisse nötig. Im Mittelpunkt steht die Freude am Singen, das Ankommen bei uns selbst 
und das Erfahren von Verbindung zueinander durch den gemeinsam erzeugten Klang.
Begleitet werden wir dabei von Gitarre oder Harmonium. Zwischendurch lauschen wir den sanften Klängen einer Handpan.
Bitte bring eine verschließbare Wasserflasche mit, extra Socken (der Raum darf nur ohne Schuhe betreten werden)
und – wenn du lieber auf dem Boden sitzt – eine Sitzunterlage.

Da die Plätze im schönen, hellen Raum im TAYOME in Friedenau begrenzt sind, bitten wir um eine kurze Anmeldung per E-Mail. 
Natürlich sind auch spontane Besucher herzlich willkommen, solange noch Plätze frei sind.

Wir freuen uns auf eine schöne gemeinsame Zeit voller Musik und Verbundenheit!

Herzliche Grüße !

Kati und Thomas
""")



# Veranstaltungsinformationen
st.subheader("📍 Ort")
st.markdown("**TAYOME**, Stierstraße 1, 12159 Berlin Friedenau (www.tayome.de)")

st.subheader("🌿 Termine - Singen in Friedenau ")
termine = [
    "So 27. Juli 2025              / 18:00h-19:30h (noch 4 Plätze)",
    "So 10. August 2025            / 18:00h-19:30h",
    "So 07. September 2025         / 18:00h-19:30h"
]

for datum in termine:
    st.markdown(f"**{datum}** ")
    
# Preisvorstellung
#st.subheader("💰 Preis")
st.write("**Preis:** Empfehlung 12 Euro, du zahlst, was du kannst.")

# Kontakt
st.subheader("📧 Anmeldung & Kontakt")
st.write("Melde dich einfach per E-Mail an oder stell uns deine Fragen:")
st.markdown("**[kontakt@singdeinherz.de]**")

# Fußzeile
st.markdown("---")
st.caption("© 2025 singdeinherz / Singen im TAYOME in Friedenau")
