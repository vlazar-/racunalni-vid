"""
    Korak 9. Spoji palac i kaziprst
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

# Postavi pomocne funkcije za crtanje
mp_crtanje = mp.solutions.drawing_utils

# Boje
zeleno = (0, 255, 0)
plavo = (255, 0, 0)

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
            #print(obiljezje)
            for id, o in enumerate(obiljezje.landmark):
                # Izracunaj stvarnu poziciju na ekranu
                visina, sirina, dubina = slicica.shape
                x = int(o.x * sirina)
                y = int(o.y * visina)
                print(id, x, y)
                # vrh palca
                if(id == 4):
                    palac_x = x
                    palac_y = y
                    cv2.circle(slicica, (palac_x, palac_y), 10, plavo, cv2.FILLED)
                # vrh kaziprsta
                if (id == 8):
                    kaziprst_x = x
                    kaziprst_y = y
                    cv2.circle(slicica, (kaziprst_x, kaziprst_y), 10, plavo, cv2.FILLED)
                    # spoji palac i kaziprst
                    cv2.line(slicica, (palac_x, palac_y), (kaziprst_x, kaziprst_y), plavo, 10)
                #cv2.circle(slicica, (x,y), 5, zeleno, cv2.FILLED)
                mp_crtanje.draw_landmarks(slicica, obiljezje, mp_hands.HAND_CONNECTIONS)
    # Prikzi video na ekranu
    cv2.imshow("Kamera", slicica)
    # Sprijeci zatvaranje prozora
    cv2. waitKey(1)