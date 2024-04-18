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
- Open it in your text editor of choice and paste this text:
  ```
  [Desktop Entry]
  Type=Application
  Name=Anti Mindblock
  Comment=Tool for removing mindblock in osu!
  Exec=/home/jakub/Documents/github/anti-mindblock/main.dist/main.bin
  Categories=Games;
  ```
- After saving, make sure to make the file executable

  ![image](https://github.com/kinaterme/anti-mindblock/assets/61877280/389fac36-2327-4bf8-b65d-35d68c971a34)
- Save the file and move it to /usr/share/applications/
  ```
  cd /path/to/main.bin
  sudo mv main.bin /usr/share/applications/
  ```

To select your skin, select your skin folder.
Example: /home/USER/.local/share/osu-wine/osu!/Skins/RafisHDDT
