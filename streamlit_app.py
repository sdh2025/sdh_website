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
st.title("Veranstaltungsreihe 2025 - Gemeinsam singen in Friedenau")
st.write("Willkommen! Hier findest du alle Termine unserer Veranstaltung sowie die Kontaktdaten zur Anmeldung.")

# ❓ Beschreibung der Veranstaltung
st.subheader("🎶 Was erwartet dich?")
st.write("""
Wir singen gemeinsam Herzenslieder aus aller Welt – Mantren, Gospel und mehr.
Die Lieder haben kurze Texte, einfache Melodien und laden zum Mitsingen ein – ganz ohne Leistungsdruck.
Begleitet werden wir dabei von Gitarre oder Harmonium – und manchmal lauschen wir auch einfach den sanften Klängen einer Handpan.
Bitte bring eine verschließbare Wasserflasche mit, extra Socken (der Raum darf nur ohne Schuhe betreten werden)
und – wenn du lieber auf dem Boden sitzt – eine Sitzunterlage.

Die Plätze im schönen hellen Raum im TAYOME in Friedenau sind begrenzt, daher freuen wir uns über eine kurze Anmeldung per E-Mail.
Wenn du ganz in der Nähe wohnst, kannst du aber auch gerne spontan vorbeikommen und schauen, ob noch ein Platz frei ist.
""")



# Veranstaltungsinformationen
st.subheader("📍 Ort")
st.markdown("**TAYOME**, Stierstraße 1, 12159 Berlin Friedenau")

st.subheader("📆 Termine - Singen in Friedenau ")
termine = [
    "So 27. Juli 2025              / 18:00h-19:30h",
    "So 10. August 2025            / 18:00h-19:30h",
    "So 07. September 2025         / 18:00h-19:30h"
]

for datum in termine:
    st.markdown(f"**{datum}** ")

# Kontakt
st.subheader("📧 Anmeldung & Kontakt")
st.write("Melde dich einfach per E-Mail an oder stell uns deine Fragen:")
st.markdown("**[kontakt@singdeinherz.de]**")

# Fußzeile
st.markdown("---")
st.caption("© 2025 singdeinherz / Singen im TAYOME in Friedenau")
