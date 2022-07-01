"""
    Korak 1. Postavi program i video ulaz
"""

# ukljuci biblioteke
import cv2

# Postavi web kameru kao video ulaz i velicinu videa
video = cv2.VideoCapture(0)
video.set(3, 960)

while True:
    # Obradi ulazni video
    status, slicica = video.read()

    # Prikzi video na ekranu
    cv2.imshow("Kamera", slicica)
    # Sprijeci zatvaranje prozora
    cv2. waitKey(1)