git clone https://github.com/salmabenmoussa7/linux_project.git
Si docker n'est pas installé, lancez les comandes suivantes:
sudo apt update
sudo apt install docker.io
docker build -t webapp:latest .
docker run -p 4567:4567 webapp


# Installation et Lancement du Projet
1. Clonez ce projet sur votre machine locale en exécutant la commande suivante :
   ```bash
   git clone https://github.com/salmabenmoussa7/linux_project.git
   ```
2. Installation de Docker
Si Docker n'est pas encore installé sur votre machine, suivez ces étapes pour l'installer :
   ```bash
   sudo apt update
   sudo apt install docker.io
   ```
3. Construction de l'image Docker
Accédez au répertoire cloné, puis construisez l'image Docker en exécutant la commande suivante :
   ```bash
   docker build -t webapp:latest .
   ```
4. Lancer le conteneur
Exécutez l'application dans un conteneur Docker avec cette commande :
   ```bash
   docker run -p 4567:4567 webapp
   ```
