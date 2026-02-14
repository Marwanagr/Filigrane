from WatermarkingModule import Watermarker
import os

"""
API Watermarker 

Usage :
    1. Instancier le moteur avec les paramètres de robustesse.
    2. Utiliser .encode() pour marquer une image.
    3. Utiliser .decode() pour vérifier l'authenticité et extraire l'ID.


from WatermarkingModule import Watermarker

# --- ÉTAPE 1 : Initialisation des paramètres ---
# alpha : Force du tatouage (0.1 = invisible, 1.0 = très fort)
# nsym  : Nombre d'octets de correction d'erreurs (plus c'est haut, plus c'est robuste)
api = Watermarker(alpha=0.25, nsym=10)

# --- ÉTAPE 2 : Tatouage ---
# Utile lors de l'upload d'une image sur un serveur.
# Paramètres : (chemin_original, message_id, chemin_sortie)
api.encode("source.webp", "USER_ID_8874", "protected_image.png")

# --- ÉTAPE 3 : Vérification (Optionnel) ---
# Utile pour vérifier si une image trouvée sur le web vous appartient.
# Paramètres : (chemin_original_stocké_sur_serveur, image_suspecte)
# Retourne : Le message caché (string) ou None/Erreur si corrompue.
resultat = api.decode("source.webp", "image_telechargee_quelque_part.png")

if resultat:
    print(f"Propriétaire identifié : {resultat}") """

def test_complet():
    # 1. Configuration des chemins
    # à adapter pour chaque image dans le répertoire filigrane
    image_originale = "images_non_tatouee/image_non_tatouee_1.jpg"
    image_tatouee = "images_tatouee/image_tatouee.png"
    message_a_cacher = "Projet d'option 2025-2026 :D"

    # Vérification de l'existence de l'image
    if not os.path.exists(image_originale):
        print(f"L'image '{image_originale}' est introuvable.")
        return

    # 2. Initialisation du module
    # alpha=0.3 permet un bon compromis entre invisibilité et détection (après une série de test)
    wm = Watermarker(alpha=0.3, repetitions=3)
    print("Initialisation du module Watermarking")

    # 3. Application de tatouage (Encodage)
    print(f"Insertion du message : '{message_a_cacher}'...")
    wm.encode(image_originale, message_a_cacher, image_tatouee)
    print(f"Image tatouée sauvegardée sous : {image_tatouee}")

    # 4. Extraction du message (Décodage)
    print("Tentative d'extraction du message")
    message_extrait = wm.decode(image_originale, image_tatouee)

    if message_extrait:
        print(f"SUCCÈS ! Message retrouvé : {message_extrait}")
    else:
        print("ÉCHEC : Le message n'a pas pu être extrait.")

if __name__ == "__main__":
    test_complet()