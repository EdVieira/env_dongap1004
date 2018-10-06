#encoding: utf-8
import subprocess

print("""
Certifique-se de estar usando o python 3+ e executar o script como root.
Assim evitará problemas de permissão durante a configuração.

	sudo python3 script.py

""")
root = input('Está executando o script como root? Informe p(de python) para sim.')
if not root is "p":
	exit()

print("Adicionando repositórios e atualizando...")
subprocess.call("sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D",shell=True)
subprocess.call("sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'",shell=True)
subprocess.call("sudo apt-get update",shell=True)
#Instalando Nginx
print("Instalando Nginx...")
subprocess.call("sudo apt-get install -y nginx",shell=True)

# Ajustar o Firewall
print("Ajustando o Firewall...")
subprocess.call("sudo ufw allow 'Nginx HTTP'",shell=True)


# Instalar Docker
print("Instalando Docker...")
subprocess.call("sudo apt-get install -y docker-engine",shell=True)

# Baixando a imagem
print("Baixando Imagem...")
subprocess.call("sudo docker pull ubuntu",shell=True)



# Criando Container app1
print("Criando Container app1...")
subprocess.call("sudo docker run -d -ti --name app1 --hostname app1 ubuntu /bin/bash",shell=True)
subprocess.call("sudo docker start app1",shell=True)
subprocess.call("sudo docker exec app1 apt-get update",shell=True)
subprocess.call("sudo docker exec app1 apt-get install -y apache2",shell=True)
# Adicionar index.html
print("Adicionando index.html...")
subprocess.call("sudo docker exec app1 rm -rf /var/www/html/index.*",shell=True)
subprocess.call("sudo echo 'app1' > index.html",shell=True)
subprocess.call("sudo docker cp index.html app1:/var/www/html",shell=True)
# Adicionar servername
print("Copiando apache2.conf...")
subprocess.call("sudo docker cp app1:/etc/apache2/apache2.conf apache2.conf",shell=True)
print("Adicionando servername ao arquivo...")
subprocess.call("sudo echo 'ServerName app1.dexter.com.br' >> apache2.conf",shell=True)
print("Adicionando servername...")
subprocess.call("sudo docker cp apache2.conf app1:/etc/apache2/apache2.conf",shell=True)
subprocess.call("sudo rm apache2.conf",shell=True)
# Reinicia apache
print("Reinicia Apache...")
subprocess.call("sudo docker exec app1 apache2ctl restart",shell=True)



# Criando Container app2
print("Criando Container app2...")
subprocess.call("sudo docker run -d -ti --name app2 --hostname app2 ubuntu /bin/bash",shell=True)
subprocess.call("sudo docker start app2",shell=True)
subprocess.call("sudo docker exec app2 apt-get update",shell=True)
subprocess.call("sudo docker exec app2 apt-get install -y apache2",shell=True)
# Adicionar index.html
print("Adicionando index.html...")
subprocess.call("sudo docker exec app2 rm -rf /var/www/html/index.*",shell=True)
subprocess.call("sudo echo 'app2' > index.html",shell=True)
subprocess.call("sudo docker cp index.html app2:/var/www/html",shell=True)
# Adicionar servername
print("Copiando apache2.conf...")
subprocess.call("sudo docker cp app2:/etc/apache2/apache2.conf apache2.conf",shell=True)
print("Adicionando servername ao arquivo...")
subprocess.call("sudo echo 'ServerName app2.dexter.com.br' >> apache2.conf",shell=True)
print("Adicionando servername...")
subprocess.call("sudo docker cp apache2.conf app2:/etc/apache2/apache2.conf",shell=True)
subprocess.call("sudo rm apache2.conf",shell=True)
# Reinicia apache
print("Reinicia Apache...")
subprocess.call("sudo docker exec app2 apache2ctl restart",shell=True)



# Criando Container app3
print("Criando Container app3...")
subprocess.call("sudo docker run -d -ti --name app3 --hostname app3 ubuntu /bin/bash",shell=True)
subprocess.call("sudo docker start app3",shell=True)
subprocess.call("sudo docker exec app3 apt-get update",shell=True)
subprocess.call("sudo docker exec app3 apt-get install -y apache2",shell=True)
# Adicionar index.html
print("Adicionando index.html...")
subprocess.call("sudo docker exec app3 rm -rf /var/www/html/index.*",shell=True)
subprocess.call("sudo echo 'app3' > index.html",shell=True)
subprocess.call("sudo docker cp index.html app3:/var/www/html",shell=True)
# Adicionar servername
print("Copiando apache2.conf...")
subprocess.call("sudo docker cp app3:/etc/apache2/apache2.conf apache2.conf",shell=True)
print("Adicionando servername ao arquivo...")
subprocess.call("sudo echo 'ServerName app3.dexter.com.br' >> apache2.conf",shell=True)
print("Adicionando servername...")
subprocess.call("sudo docker cp apache2.conf app3:/etc/apache2/apache2.conf",shell=True)
subprocess.call("sudo rm apache2.conf",shell=True)
subprocess.call("sudo rm index.html",shell=True)
# Reinicia apache
print("Reinicia Apache...")
subprocess.call("sudo docker exec app3 apache2ctl restart",shell=True)



# Configurando proxy_pass Nginx
print("Configurando proxy_pass Nginx...")
#subprocess.call("sudo rm /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo 'server {listen 29290;listen [::]:29290;' > /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo 'location / {proxy_pass http://172.17.0.2:80/;}' >> /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo '}' >> /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo 'server {listen 29291;listen [::]:29291;' >> /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo 'location / {proxy_pass http://172.17.0.3:80/;}' >> /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo '}' >> /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo 'server {listen 29292;listen [::]:29292;' >> /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo 'location / {proxy_pass http://172.17.0.4:80/;}' >> /etc/nginx/conf.d/apps.conf",shell=True)
subprocess.call("sudo echo '}' >> /etc/nginx/conf.d/apps.conf",shell=True)

# Desativa pagina Welcome to nginx
print("Desativando Welcome")
subprocess.call("sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled",shell=True)

# Recarrega o nginx
print("Recarregando Nginx")
subprocess.call("sudo nginx -s reload",shell=True)
