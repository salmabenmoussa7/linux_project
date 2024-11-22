git clone https://github.com/salmabenmoussa7/linux_project.git
Si docker n'est pas installé, lancez les comandes suivantes:
sudo apt update
sudo apt install docker.io
docker build -t webapp:latest .
docker run -p 4567:4567 webapp
