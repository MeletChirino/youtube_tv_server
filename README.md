# Reproductor de musica basado en un servidor de youtubeTV

Este script en pyhton es muy util para usar un reproductor de musica tipo servidor de youtube y poder controlarlo desde un dispositivo movil. Confieso que lo uso en fiestas y para entretenimiento en el hogar.
# Instrucciones
Primero se deben tener los paquetes de Selenium y un chromedriver. Las instrucciones de instalacion pueden variar dependiendo de tu sistema operativo y plataforma. Estas funcionan para raspberry pi y ubuntu.
1 Instalar pip y Selenium
sudo apt update
sudo apt install python-pip
sudo pip install selenium
2 Luego hay que instalar el chromedriver desde la pag
https://launchpad.net/ubuntu/trusty/+package/chromium-chromedriver
3 Hay se escoge el que mas se ajuste a tu arquitectura. Probablemente debas instalar el paquete de chromium-browser si usas una raspberry. Si usas algun servidor de escritorio puedes buscar como instalar chromedriver.
sudo apt-get install chromium-browser
4 Finalmente actualiza todo para que se instale la version correcta del chromium-chromedriver
sudo apt update && sudo apt upgrade
