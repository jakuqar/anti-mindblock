# Anti Mindblock tool
I remade Shikkesora's osu! Anti Mindblock tool for Linux.

Known issues:
- All monitors flip on multi-monitor setups
- Bad UI

Installation:
- Download the .zip file from Releases
- Unzip the archive
- Run Anti_Mindblock/main.dist/main.bin

Implementation:
- Create a new .desktop file
  ![image](https://github.com/kinaterme/anti-mindblock/assets/61877280/421b45ce-a7d2-4906-847a-4cacbf360a2e)
- Open it in your text editor of choice
  ```[Desktop Entry]
  Type=Application
  Name=Anti Mindblock
  Comment=Tool for removing mindblock in osu!
  Exec=/home/jakub/Documents/github/anti-mindblock/main.dist/main.bin
  Categories=Games;```


To select your skin, select your skin folder.
Example: /home/USER/.local/share/osu-wine/osu!/Skins/RafisHDDT
