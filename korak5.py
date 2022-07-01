"""
    Korak 5. Izracunaj poziciju tocaka
"""

# ukljuci biblioteke
import cv2
import mediapipe as mp

# Postavi web kameru kao video ulaz i velicinu videa
video = cv2.VideoCapture(0)
video.set(3, 960)

# Postavi mp hands algoritam
mp_hands = mp.solutions.hands
ruka = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6)

while True:
    # Obradi ulazni video
    status, slicica = video.read()
    rezultat = ruka.process(slicica)
    # Ispisi rezultat u konzolu
    # print(rezultat)

    # Ako je ruka nadena
    if rezultat.multi_hand_landmarks:
        # print("Vidim ruku")
        for obiljezje in rezultat.multi_hand_landmarks:
            # print(obiljezje)
            for id, o in enumerate(obiljezje.landmark):
                # Izracunaj stvarnu poziciju na ekranu
                visina, sirina, dubina = slicica.shape
                x = int(o.x * sirina)
                y = int(o.y * visina)
                print(id, x, y)

    # Prikzi video na ekranu
    cv2.imshow("Kamera", slicica)
    # Sprijeci zatvaranje prozora
    cv2. waitKey(1)