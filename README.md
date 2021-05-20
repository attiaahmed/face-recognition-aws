![d7e12b6d-5891-42c4-ae8d-63a1fa508005](https://user-images.githubusercontent.com/36500926/119038044-975d8700-b9aa-11eb-86ab-274aaf0dc1ec.jpg)
# face-recognition-aws
Face recognition using Amazon Web Service 
Construction d'un miroir intelligent basé sur la reconnaissance faciale avec AWS Face recognition qui consiste a contrôler une maison et d'afficher plusieurs module comme les email et votre agenda etc
mais ce miroir a une grande position dans les industrie tell que elle affiche le bilan de chaque employée et le fonctionnement des automates en temp reel
il augmente la productivité et le contrôle de l'usine

Hardware : raspberry 
git clone https://github.com/HaarigerHarald/omxiv
sudo apt-get install libjpeg8-dev libpng12-dev
cd omxiv
make ilclient
make
sudo make install

-the graphic design was in JavaScript HTML CSS
-to pass from python code to html i used an eel library
-i didn't use multiple html pages i just used a unic page containing four themes and i used this method to keep raspberry processor fast because when i use four html pages the python code will open a new one each time to change the theme instead of updating the same page and to use this method w call it
document.getElementById ("content"). style.display = "block";
document.getElementById ("content"). style.display = "none";

-To display Saudi holidays i used a json file which contains all holidays
-To display the weather, i used a free open weather map API
-To show corona statistics and money converter, i also used a free api
-about facial recognition, i used amazon aws instead of opencv
because after a big research i found out that aws is 4 times faster and easier than opencv and there is a library in opencv colled cv2, it is difficult to download it
-the mirror only works when there is a somone in front so i used this commond os.system ("xset -display: 0.0 dpms force off")
to disconnect the signal between hdmi and raspberry and os.system ("xset -display: 0.0 dpms force on") to connect it
-to change position of widget you have to change a class in css

![c9c00002-f55c-482f-b287-237c89822b2f](https://user-images.githubusercontent.com/36500926/119037530-fe2e7080-b9a9-11eb-9196-fc54463f88d5.jpg)

![d7e12b6d-5891-42c4-ae8d-63a1fa508005](https://user-images.githubusercontent.com/36500926/119038101-a3e1df80-b9aa-11eb-9479-58442794c593.jpg)
