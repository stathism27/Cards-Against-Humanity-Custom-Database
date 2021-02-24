# Cards Against Humanity Custom Database
Expandable custom database for the Cards Against Humanity, in JSON format.

# The goal
The goal is to create an **easily adaptable and full customable** database for our favorite game 

# Authors
* **StathisM27** - *Initial work* - [StathisM27](https://github.com/stathism27)

# Technical explanation 
_The project consists of 3 files and 2 directories:_

**Cards Against Humanity Database.json** : The core database of the game (**must not be changed unless official changes are made**)<br><br>
**Cards Against Humanity Database Expanded.json** : Community's custom database, must contain all the packs <br><br>
**expansion.py** : A simple python script to add the custom cards from txt files to the original database and create the new *Cards Against Humanity Database Expanded.json*<br>
Add your pack by adding it in the array,along with the other packs:
```
names_of_packs = ["YourPack"]
```
**whites** and **blacks** : Directories to have the pure text of custom packs that a user adds. For instance if a user wants to add _X_ pack must upload also _X_whites.txt_ and _X_blacks.txt_ under the proper directory   <br><br>

# About update
You can upload whatever you want, there will be no censorship at all, but bear in mind that the txt files must contain text only in **English** language!<br>

# About copyrights
Cards against Humanity runs under [Creative Commons BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/) **No commercial use is allowed!** <br>
[Cards Against Humanity Original Site](https://cardsagainsthumanity.com/)
