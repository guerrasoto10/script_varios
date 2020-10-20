echo "Users (Regular only):" #imprimimos solo los usuarios regulares
awk -F: '$3 >= 1000 {print $1}' /etc/passwd
echo "Services:[+] for running services, [–] for stopped services and [?] for services without a ‘status’"
service --status-all  #imprimimos todos los servivcios disponibles en el equipo.