## Le Filigrane en deux mots
Le filigrane numérique (ou watermarking) est une technique qui consiste à cacher une information invisible et permanente au cœur des données d'une image. Contrairement à un simple texte superposé, ce tatouage est mathématiquement intégré dans les fréquences de l'image via la DCT (Discrete Cosine Transform), ce qui le rend difficile à supprimer sans détériorer la qualité visuelle de l'original.

### Structure du Projet
L'organisation est pensée pour séparer les données du moteur de calcul :

- WatermarkingModule/
Le cerveau du projet. Il contient la logique de calcul de la Transformée en Cosinus Discrète (DCT) et les algorithmes de correction d'erreurs Reed-Solomon.

- image_non_tatouee/
Le répertoire source. C'est ici que vous devez placer vos images originales que vous souhaitez protéger.

- image_tatouee/
Le répertoire de sortie. Le code y générera automatiquement les images une fois marquées par le processus de tatouage.

- main.py
Le script principal. Il sert d'interface pour orchestrer l'encodage du message et la vérification automatique de son intégrité.

- requirements.txt
Le fichier de configuration des dépendances. Il liste les bibliothèques nécessaires au fonctionnement du projet (OpenCV, NumPy, Scipy, ReedSolo).

### Comment lancer le projet
#### Création de l'environnement virtuel
Ouvrez un terminal dans le dossier du projet et créez un environnement isolé :
```bash
python -m venv venv
```    

        
#### Activation de l'environnement
##### Windows :
    .\venv\Scripts\activate

##### Mac / Linux :
    source venv/bin/activat
#### Installation des dépendances
Avant de commencer, vous devez installer les bibliothèques Python requises en lançant la commande suivante dans votre terminal :

    pip install -r requirements.txt
#### 1- Préparation
Placez votre image (format .jpg, .png ou .webp) dans le dossier nommé image_non_tatouee/.

#### 2- Configuration
Ouvrez le fichier main.py et modifiez les variables de chemin pour qu'elles correspondent à votre fichier :

    image_originale = "images_non_tatouee/image_non_tatouee_1.jpg"
    image_tatouee = "images_tatouee/image_tatouee.png"
    message_a_cacher = "Projet d'option 2025-2026 :D"
    
#### 3- Exécution
Une fois la configuration terminée, lancez le script avec la commande :
python main.py

#### 4- Test automatique d'intégrité
Le code effectue immédiatement un test de vérification après la création de l'image marquée :

#### 5- Simulation d'extraction
Le script recharge l'image qui vient d'être créée dans le dossier image_tatouee/ et tente d'en extraire le message caché en le comparant à l'original.

#### 6- Validation du résultat
Si le message extrait est identique au message initial, le système confirme que le tatouage est conforme et robuste.

Si le message est corrompu ou illisible, le script affiche un avertissement. Dans ce cas, il est conseillé d'augmenter la valeur du paramètre alpha dans le code pour renforcer l'empreinte numérique.
## API :
Le module est conçu pour être utilisé comme une bibliothèque indépendante. L'utilisateur peut l'intégrer directement dans un serveur web ou un outil d'automatisation en important la classe Watermarker. Cette approche permet d'automatiser la protection des images dès leur importation (upload) et de simplifier leur vérification ultérieure sans avoir à manipuler la logique interne du traitement de signal. Un exemple d'implémentation est fourni en commentaire dans le fichier main.py.
