import os

#Instalando Nginx
print("Instalando Nginx...")
os.system("sudo apt-get update")
os.system("sudo apt-get install -y nginx")

# Ajustar o Firewall
print("Ajustando o Firewall...")
os.system("sudo ufw allow 'Nginx HTTP'")


# Instalar Docker
print("Instalando Docker...")
os.system("sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D")
os.system("sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'")
os.system("sudo apt-get update")
os.system("sudo apt-get install -y docker-engine")

# Baixando a imagem
print("Baixando Imagem...")
os.system("sudo docker pull ubuntu")

# Criando Container app1
print("Criando Container app1...")
os.system("sudo docker run -d -ti --name app1 --hostname app1 ubuntu /bin/bash")
os.system("sudo docker exec -d app1 apt-get update")
os.system("sudo docker exec -d app1 apt-get install -y apache2")
os.system("sudo docker exec -d app1 rm /var/www/html/index.html")
os.system("sudo docker exec -d app1 app1 >> sudo /var/www/html/index.html")
os.system("sudo docker start app1")

# Criando Container app2
print("Criando Container app2...")
os.system("sudo docker run -d -ti --name app2 --hostname app2 ubuntu /bin/bash")
os.system("sudo docker exec -d app2 apt-get update")
os.system("sudo docker exec -d app2 apt-get install -y apache2")
os.system("sudo docker exec -d app2 rm /var/www/html/index.html")
os.system("sudo docker exec -d app2 app2 >> sudo /var/www/html/index.html")
os.system("sudo docker start app2")

# Criando Container app3
print("Criando Container app3...")
os.system("sudo docker run -d -ti --name app3 --hostname app3 ubuntu /bin/bash")
os.system("sudo docker exec -d app3 apt-get update")
os.system("sudo docker exec -d app3 apt-get install -y apache2")
os.system("sudo docker exec -d app3 rm /var/www/html/index.html")
os.system("sudo docker exec -d app3 app3 >> sudo /var/www/html/index.html")
os.system("sudo docker start app3")

# Configurando /etc/hosts
print("Configurando /etc/hosts...")
# 172.17.0.0/17 Ordem de IPs de máquinas iniciadas no Docker
os.system("sudo echo '172.17.0.2	app1.dexter.com.br' >> sudo /etc/hosts")
os.system("sudo echo '172.17.0.3	app2.dexter.com.br' >> sudo /etc/hosts")
os.system("sudo echo '172.17.0.4	app3.dexter.com.br' >> sudo /etc/hosts")


# Configurando proxy_pass Nginx
print("Configurando proxy_pass Nginx...")
os.system("sudo rm /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'server {listen 80;listen [::]:80;' >> sudo /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'location /app1 {proxy_pass http://app1.dexter.com.br:80/;}' >> sudo /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'location /app2 {proxy_pass http://app2.dexter.com.br:80/;}' >> sudo /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'location /app3 {proxy_pass http://app3.dexter.com.br:80/;}' >> sudo /etc/nginx/conf.d/apps.conf")
os.system("sudo echo '}' >> sudo /etc/nginx/conf.d/apps.conf")

# Desativa pagina Welcome to nginx
print("Desativando Welcome")
os.system("sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled")

# Recarrega o nginx
print("Recarregando Nginx")
os.system("sudo nginx -s reload")
