                                                                        README

A continuación, daremos una breve explicación de como desplegar automáticamente el servicio que consume datos de la SIATA.

PRELIMINARES:
-	Verificar la instalación del servicio Docker en su máquina.

PASOS:
1.	Para este proceso es necesario ubicar el archivo ‘script.sh’ y las carpetas ‘DB’, ‘FRONT’, ‘API’. El archivo script y las carpetas pueden están ubicados en cualquier directorio, sin embargo, es necesario tener el archivo ‘script.sh’ en el mismo directorio de las carpetas ‘DB’ ,‘FRONT’, ‘API’ .
2.	Es necesario dar permisos para la ejecución del archivo ‘script.sh’. Por consiguiente, para otorgarle los permisos se utiliza el comando <chmod +x script.sh>.
3.	Una vez otorgado los permisos al archivo ‘script.sh’ se ejecuta el archivo ‘script.sh’ con el comando <sh script.sh>.
4.	El ‘script.sh’ va a ingresar al directorio DB/ y ejecutará el comando que creará una imagen a partir de su archivo Dockerfile y posterior a ello, construye el contenedor con dicha imagen. Este procedimiento se realizará entrando a la carpeta FRONT/ y API/ donde ejecutará su propio contenedor.
5.	Para verificar que todo el servicio se haya desplegado automáticamente en su máquina, ejecute el comando <docker ps> el cual deberá mostrar una lista de tres contenedores, siendo cada uno de ellos para el front, api y db.
Cada uno de estos contenedores estará ejecutando un archivo Python que consumirá los Frameworks de lenguaje para el desarrollo web (Dash y Flask).
Si desea verificar el funcionamiento individual de los servicios db y api puede hacerlo con:
Db: http://ip_address:500/users
Api: http://ip_address:5000/mostrar_estacionesnivel?psw=12345678
6.	Para este punto toda la ejecución del ‘script.sh’ ya habrá desplegado el servicio que permitirá consumir los datos en la SIATA. Para dar verificación a ello, se deberá buscar la dirección IP pública de su máquina personal por el puerto 5010.
Para verificar el servicio, ingrese el siguiente enlace en su navegador:
Ejemplo: http://ip_address:5010/mostrar_estacionesnivel?psw=12345678 





7.	Los usuarios y contraseñas están quemados en el servicio de base de datos, por ello, a continuación, se proporcionan los usuarios con sus contraseñas correspondientes:
Usuario:        Contraseña:
Chucho          1234
Benju           abcd
Mafe            Mafe1234
Ferney          el_mejor



IMPORTANTE: Si tuvo algún problema o falla contacte a nuestro correo personal: johan.choles@upb.edu.co o jesus.diaz@upb.edu.co. 

Mayo, 2023.
