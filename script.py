#encoding: utf-8
import os, sys

print("""
Certifique-se de estar usando o python 3+ e executar o script como root.
Assim evitará problemas de permissão durante a configuração.

	sudo python3 script.py

""")
root = input('Está executando o script como root? Informe p(de python) para sim.')
if root is "p":
	# Para resolver permissows do apache2.conf
	#os.system("sudo python3 script.py a")
	#exit()
	pass
elif not root is "p":
	exit()

print("Adicionando repositórios e atualizando...")
os.system("sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D")
os.system("sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'")
os.system("sudo apt-get update")
#Instalando Nginx
print("Instalando Nginx...")
os.system("sudo apt-get install -y nginx")

# Ajustar o Firewall
print("Ajustando o Firewall...")
os.system("sudo ufw allow 'Nginx HTTP'")


# Instalar Docker
print("Instalando Docker...")
os.system("sudo apt-get install -y docker-engine")

# Baixando a imagem
print("Baixando Imagem...")
os.system("sudo docker pull ubuntu")



# Criando Container app1
print("Criando Container app1...")
os.system("sudo docker run -d -ti --name app1 --hostname app1 ubuntu /bin/bash")
os.system("sudo docker start app1")
os.system("sudo docker exec app1 apt-get update")
os.system("sudo docker exec app1 apt-get install -y apache2")
# Adicionar index.html
print("Adicionando index.html...")
os.system("sudo docker exec app1 rm -rf /var/www/html/index.*")
os.system("sudo echo 'app1' > index.html")
os.system("sudo docker cp index.html app1:/var/www/html")
# Adicionar servername
print("Copiando apache2.conf...")
os.system("sudo docker cp app1:/etc/apache2/apache2.conf apache2.conf")
print("Adicionando servername ao arquivo...")
os.system("sudo echo 'ServerName app1.dexter.com.br' >> apache2.conf")
print("Adicionando servername...")
os.system("sudo docker cp apache2.conf app1:/etc/apache2/apache2.conf")
os.system("sudo rm apache2.conf")
# Reinicia apache
print("Reinicia Apache...")
os.system("sudo docker exec app1 apache2ctl restart")



# Criando Container app2
print("Criando Container app2...")
os.system("sudo docker run -d -ti --name app2 --hostname app2 ubuntu /bin/bash")
os.system("sudo docker start app2")
os.system("sudo docker exec app2 apt-get update")
os.system("sudo docker exec app2 apt-get install -y apache2")
# Adicionar index.html
print("Adicionando index.html...")
os.system("sudo docker exec app2 rm -rf /var/www/html/index.*")
os.system("sudo echo 'app2' > index.html")
os.system("sudo docker cp index.html app2:/var/www/html")
# Adicionar servername
print("Copiando apache2.conf...")
os.system("sudo docker cp app2:/etc/apache2/apache2.conf apache2.conf")
print("Adicionando servername ao arquivo...")
os.system("sudo echo 'ServerName app2.dexter.com.br' >> apache2.conf")
print("Adicionando servername...")
os.system("sudo docker cp apache2.conf app2:/etc/apache2/apache2.conf")
os.system("sudo rm apache2.conf")
# Reinicia apache
print("Reinicia Apache...")
os.system("sudo docker exec app2 apache2ctl restart")



# Criando Container app3
print("Criando Container app3...")
os.system("sudo docker run -d -ti --name app3 --hostname app3 ubuntu /bin/bash")
os.system("sudo docker start app3")
os.system("sudo docker exec app3 apt-get update")
os.system("sudo docker exec app3 apt-get install -y apache2")
# Adicionar index.html
print("Adicionando index.html...")
os.system("sudo docker exec app3 rm -rf /var/www/html/index.*")
os.system("sudo echo 'app3' > index.html")
os.system("sudo docker cp index.html app3:/var/www/html")
# Adicionar servername
print("Copiando apache2.conf...")
os.system("sudo docker cp app3:/etc/apache2/apache2.conf apache2.conf")
print("Adicionando servername ao arquivo...")
os.system("sudo echo 'ServerName app3.dexter.com.br' >> apache2.conf")
print("Adicionando servername...")
os.system("sudo docker cp apache2.conf app3:/etc/apache2/apache2.conf")
os.system("sudo rm apache2.conf")
os.system("sudo rm index.html")
# Reinicia apache
print("Reinicia Apache...")
os.system("sudo docker exec app3 apache2ctl restart")



# Configurando proxy_pass Nginx
print("Configurando proxy_pass Nginx...")
#os.system("sudo rm /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'server {listen 80;listen [::]:80;' > /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'location /app1 {proxy_pass http://172.17.0.2:80/;}' >> /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'location /app2 {proxy_pass http://172.17.0.3:80/;}' >> /etc/nginx/conf.d/apps.conf")
os.system("sudo echo 'location /app3 {proxy_pass http://172.17.0.4:80/;}' >> /etc/nginx/conf.d/apps.conf")
os.system("sudo echo '}' >> /etc/nginx/conf.d/apps.conf")

# Desativa pagina Welcome to nginx
print("Desativando Welcome")
os.system("sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled")

# Recarrega o nginx
print("Recarregando Nginx")
os.system("sudo nginx -s reload")
