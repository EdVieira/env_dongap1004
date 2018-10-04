import os

# Instalar Nginx
os.system("sudo apt-get update")
os.system("sudo apt-get install -y nginx")

# Ajustar o Firewall
os.system("sudo ufw allow 'Nginx HTTP'")


# Instalar Docker
os.system("sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D")
os.system("sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'")
os.system("sudo apt-get update")
os.system("sudo apt-get install -y docker-engine")

# Baixando a imagem
os.system("sudo docker pull ubuntu")

# Criando Container app1
os.system("sudo docker run -ti --name app1 --hostname app1 ubuntu /bin/bash")
os.system("sudo apt-get update")
os.system("apt-get install -y apache2")
os.system("rm /var/www/html/index.html")
os.system("app1 >> /var/www/html/index.html")
os.system("exit")
os.system("sudo docker start app1")

# Criando Container app2
os.system("sudo docker run -ti --name app2 --hostname app2 ubuntu /bin/bash")
os.system("sudo apt-get update")
os.system("apt-get install -y apache2")
os.system("rm /var/www/html/index.html")
os.system("app2 >> /var/www/html/index.html")
os.system("exit")
os.system("sudo docker start app2")

# Criando Container app3
os.system("sudo docker run -ti --name app3 --hostname app3 ubuntu /bin/bash")
os.system("sudo apt-get update")
os.system("apt-get install -y apache2")
os.system("rm /var/www/html/index.html")
os.system("app3 >> /var/www/html/index.html")
os.system("exit")
os.system("sudo docker start app3")

# Configurando /etc/hosts
# 172.17.0.0/17 Ordem de IPs de máquinas iniciadas no Docker
os.system("echo '172.17.0.2	app1.dexter.com.br' >> /etc/hosts")
os.system("echo '172.17.0.3	app2.dexter.com.br' >> /etc/hosts")
os.system("echo '172.17.0.4	app3.dexter.com.br' >> /etc/hosts")


# Configurando proxy_pass Nginx
os.system("echo 'server {listen 80;listen [::]:80;' >> /etc/nginx/conf.d/apps.conf")
os.system("echo 'location /app1 {proxy_pass http://app1.dexter.com.br:80/;}' >> /etc/nginx/conf.d/apps.conf")
os.system("echo 'location /app2 {proxy_pass http://app2.dexter.com.br:80/;}' >> /etc/nginx/conf.d/apps.conf")
os.system("echo 'location /app3 {proxy_pass http://app3.dexter.com.br:80/;}' >> /etc/nginx/conf.d/apps.conf")
os.system("echo '}' >> /etc/nginx/conf.d/apps.conf")

# Desativa pagina Welcome to nginx
os.system("mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled")

# Recarrega o nginx
os.system("nginx -s reload")