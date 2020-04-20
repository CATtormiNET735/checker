# Checker
Es un checker de tarjetas de credito hecho en python3 por comandator estudios.
El metodo de checkeo es simple va a una pagina de donaciones y pone datos falso a esepcion de los datos de las tarjetas para proteger tu identidad,
despues simplemente el script se fija si acepto el pago o lo rechaso y si lo acepta tarjeta viva si lo rechasa tarjeta muerta

# metodo de instalacion:

*- sudo apt-get install update && sudo apt-get install upgrade*

*- sudo apt-get install git && sudo apt-get install python3*

*- sudo apt-get install python3-pip*

*- sudo pip3 install colorama*

*- sudo pip3 install requests*

*- git clone https://github.com/comandator/cc-checker/*

*- cd cc-checker*

- chmod +x *


# como usar?

es simple hay 2 archivos, checker.py y tarjetas.txt en tarjetas.txt tiene que pones las tarjetas que quieren checkear
de esta forma:

ejemplo:

Numero|mes|Ano|cvc

4915735028731500|06|24|663

se tiene que poner el numero de la tarjeta a checkear el mes de 2 digitos y el ano de 2 digitos logicamente tambien el codigo de seguridad, haci se tienen que poner las tarjetas en el archivo tarjetas.txt.

Para Ejecutarlo es simple solo pongan en la terminal

*python3 checker.py*

y listo 

Suerte.
