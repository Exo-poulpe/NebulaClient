# Nebula Client Script

Voici les scripts client pour le VPN Nebula
---

## Requirements

Install dependances :
```console
sudo apt install git python3 python3-pip openssl 
pip3 install -r requirements.txt
```
---

## Step

cloné le repo
```console
git clone https://github.com/Exo-poulpe/NebulaClient.git
cd NebulaClient
```

Lancé l'installation et créations des clé
```console
python3 install.py --user <user_id>
```

Ensuite le program nebula et les clés privée et publique seront créer il faudra obtenir un certificat pour ce faire 
```console
python3 client.py --user <user_id> --passw <password> --ip <ip>
```