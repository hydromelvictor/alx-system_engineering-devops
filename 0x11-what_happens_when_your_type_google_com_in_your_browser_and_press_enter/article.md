What happens when you type google.com in your browser and press Enter
======================================================================

etrange question n'est pas? vous n'y avez jamais pensée? ok c'est maintenant le moment, alors que se passe-t-il lorsque vous saisissez https://www.google.com dans votre navigateur et que vous appuyez sur Entrée ?

tout d'abord commençons par dire que "https://www.google.com" est ce que nous appelons une **url**(*Uniform Resource Locator*). essayons d'etre un peut plus clair en lui donnant une definition plus simple

## URL

comme mentionné, **url** est l'acronyme de *Uniform Resource Locator*, de facon global c'est le nom d'une ressource sur le web dont le type pourrait etre (une page html, une video, ....).

considerons la comme etant le nom d'une institution dans laquelle nous devons nous rendre pour une reunion d'affaire.

helas nous n'avons pas l'adresse de cette institution seulement le nom, aucun soucis nous iront consulter l'annuaire. ici notre annuaire est le **DNS**

## le DNS

le **DNS**, *Domain Name System* est le server sur lequel est heberger les adresses **IP** c'est a dire l'adresse du server web sur lequel reside notre www.google.com.

c'est donc notre annuaire auquel nous devons adressé une requete dns.

### une requete DNS

une requete dns est un code informatique indiquant au server **DNS** la nature de notre requete, et dans notre situation une reunion d'affaire.

alors ayant reçu l'adresse exact de notre intitution il nous faudra nous rendre. en ce moment intervient le protocole **TCP/IP** en d'autre terme notre moyen de transport ou de deplacement pour ceux qui prefere.

## TCP/IP

**TCP** (*Transmission Control Protocol*) est le protocol permettant d'acheminer les informations de notre navigateur au server web situé sur le reseaux a l'adresse **IP** (*Internet Protocol*). pour simplement dire le TCP est le vehicule qui nous conduira au server situé au coordonnées geographique **IP**.

l'acces aux information sur le server est regis par un reglement etablir par un **Par-feu** et accessible via **HTTPS/SSL**.

pour simplement dire l'entrée de l'institution ou se deroulera notre reunion d'affaire et gardé par des agents de securité (**pare-feu**) et dont l'acces est jsur la verification d'une carte electronique (**HTTPS/SSL**).

## Firewall?

c'est un programme informatique ou logiciel physique responsable de la securité du reseau, il s'assure du respect effectif des reglements etablit pour une communication reussi.

## HTTPS/SSL

de son nom *HyperText Transfert Protocol Secure*, **HTTPS** assure l'echange entre notre navigateur et le server hebergeant "https://www.google.com" au moyen d'une technologie standard destiné a la securité et la protection des données sensible le **SSL** (*Secure Sockets Layer*).

felicitation nous somme desormais au sein de l'institution il nous reste a trouvez la salle de notre reunion d'affaire et la intervient **l'Equilibreur de charge** dont le role est de nous conduire a notre reunion (au server web chargé des requetes nous consernant)

## Load Balancer

l'equilibreur de charge est un programme ou un logiciel informatique chargé de la repartition des charges de travail entre les servers web. c'est notre reunion d'affaires

## Servers Web

c'est un logiciel hebergeur de ressource sur le web qui repond a des requestes sur le reseaux public. il stocke, traite et livre des fichiers aux server d'application web.

## Application server

c'est l'outil permettant de construire a partir des composants logiciels du server web des applications de toute sorte a delivré a l'utilisateur selon la demande.

en d'autre terme c'est la secretaire chargé du resumé de la reunion et n'y incluant les information importante. 

## Database

c'est l'entroid ou reside les données importantes, c'est le systeme de stockage.

