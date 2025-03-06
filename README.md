# almenscorner-recipes

A set of recipes for use with the [IntuneAppUploader](https://github.com/almenscorner/intune-uploader) processor.

To use the recipes, add this repository to your autopkg repos and create overrides:

```bash
autopkg repo-add almenscorner-recipes
```

```bash
autopkg make-override Spotify.intune.recipe
```

## Dependencies

Most of the recipes in this repository have a dependency on a parent recipe for downloading the application. To find which recipe repos you need to add to use a specific recipe, look up the `ParentRecipe` key in the recipe. This gives you an idea of which recipe repos you need to add to your autopkg installation. Also, keep in mind that some recipes have dependencies on other recipes, so you might need to add more than one recipe repo.

The table below lists the recipes in this repository along with their respective parent recipes. It will be updated on a best-effort basis, so please validate the information before use.

|recipe                                                                                           |                                 dependency                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|[DevToys.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/DevToys/DevToys.intune.recipe)                                                                           |[almenscorner-recipes](https://github.com/autopkg/almenscorner-recipes)      |
|[Syncthing.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Syncthing/Syncthing.intune.recipe)                                                                     |[ctueck-recipes](https://github.com/autopkg/ctueck-recipes)                  |
|[Cakebrew.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Cakebrew/Cakebrew.intune.recipe)                                                                        |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[FirefoxSigned.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Mozilla/FirefoxSigned.intune.recipe)                                                               |[recipes](https://github.com/autopkg/recipes)                                |
|[DB Browser for SQLite.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/DB%20Browser%20for%20SQLite/DB%20Browser%20for%20SQLite.intune.recipe)                     |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[AutoDeskFusion360.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/AutoDesk%20Fusion%20360/AutoDeskFusion360.intune.recipe)                                       |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Alacritty.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Alacritty/Alacritty.intune.recipe)                                                                     |[apizz-recipes](https://github.com/autopkg/apizz-recipes)                    |
|[Sketch.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/BohemianCoding/Sketch.intune.recipe)                                                                      |[foigus-recipes](https://github.com/autopkg/foigus-recipes)                  |
|[Docker.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Docker/Docker.intune.recipe)                                                                              |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Discord.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Discord/Discord.intune.recipe)                                                                           |[joshua-d-miller-recipes](https://github.com/autopkg/joshua-d-miller-recipes)|
|[Snagit.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Snagit/Snagit.intune.recipe)                                                                              |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Gifox.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Gifox/Gifox.intune.recipe)                                                                                 |[apizz-recipes](https://github.com/autopkg/apizz-recipes)                    |
|[MicrosoftRemoteHelp.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/MicrosoftRemoteHelp/MicrosoftRemoteHelp.intune.recipe)                                       |[rtrouton-recipes](https://github.com/autopkg/rtrouton-recipes)              |
|[Bartender.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Bartender/Bartender.intune.recipe)                                                                     |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Cyberduck.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Cyberduck/Cyberduck.intune.recipe)                                                                     |[recipes](https://github.com/autopkg/recipes)                                |
|[DisplayLinkManager.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/DisplayLink%20Manager/DisplayLinkManager.intune.recipe)                                       |[smithjw-recipes](https://github.com/autopkg/smithjw-recipes)                |
|[Audacity.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Audacity/Audacity.intune.recipe)                                                                        |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[MongoDBCompass.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/MongoDB%20Compass/MongoDBCompass.intune.recipe)                                                   |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[LogiOptionsPlus.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/LogiOptionsPlus/LogiOptionsPlus.intune.recipe)                                                   |[rtrouton-recipes](https://github.com/autopkg/rtrouton-recipes)              |
|[Terraform.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/HashiCorp/Terraform.intune.recipe)                                                                     |[timsutton-recipes](https://github.com/autopkg/timsutton-recipes)            |
|[Evernote.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Evernote/Evernote.intune.recipe)                                                                        |[recipes](https://github.com/autopkg/recipes)                                |
|[AmazonQ.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Amazon%20Q/AmazonQ.intune.recipe)                                                                        |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Insomnia.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Insomnia/Insomnia.intune.recipe)                                                                        |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[AppCleaner.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/AppCleaner/AppCleaner.intune.recipe)                                                                  |[jleggat-recipes](https://github.com/autopkg/jleggat-recipes)                |
|[ClickShare.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/ClickShare/ClickShare.intune.recipe)                                                                  |[moofit-recipes](https://github.com/autopkg/moofit-recipes)                  |
|[iMazing.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/iMazing/iMazing.intune.recipe)                                                                           |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Caffeine.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Caffeine/Caffeine.intune.recipe)                                                                        |[peetinc-recipes](https://github.com/autopkg/peetinc-recipes)                |
|[ChefWorkstation.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Chef/ChefWorkstation.intune.recipe)                                                              |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[iMazingProfileEditor.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/iMazingProfileEditor/iMazingProfileEditor.intune.recipe)                                    |[rtrouton-recipes](https://github.com/autopkg/rtrouton-recipes)              |
|[GoogleChromePkg.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Google/GoogleChromePkg.intune.recipe)                                                            |[recipes](https://github.com/autopkg/recipes)                                |
|[AndroidStudio.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Google/AndroidStudio.intune.recipe)                                                                |[novaksam-recipes](https://github.com/autopkg/novaksam-recipes)              |
|[GoogleChrome.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Google/GoogleChrome.intune.recipe)                                                                  |[recipes](https://github.com/autopkg/recipes)                                |
|[Spotify.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Spotify/Spotify.intune.recipe)                                                                           |[recipes](https://github.com/autopkg/recipes)                                |
|[Tunnelblick.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Tunnelblick/Tunnelblick.intune.recipe)                                                               |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Canva.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Canva/Canva.intune.recipe)                                                                                 |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[BBEdit15.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/BBEdit%2015/BBEdit15.intune.recipe)                                                                     |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Krita.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Krita/Krita.intune.recipe)                                                                                 |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Airy.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Airy/Airy.intune.recipe)                                                                                    |[almenscorner-recipes](https://github.com/autopkg/almenscorner-recipes)      |
|[Postman.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Postman/Postman.intune.recipe)                                                                           |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Anki.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Anki/Anki.intune.recipe)                                                                                    |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Code.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Code/Code.intune.recipe)                                                                                    |[valdore86-recipes](https://github.com/autopkg/valdore86-recipes)            |
|[AltTab.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/AltTab/AltTab.intune.recipe)                                                                              |[apizz-recipes](https://github.com/autopkg/apizz-recipes)                    |
|[yubioath-desktop.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Yubico/yubioath-desktop.intune.recipe)                                                          |[n8felton-recipes](https://github.com/autopkg/n8felton-recipes)              |
|[Elgato Stream Deck.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Elgato%20Stream%20Deck/Elgato%20Stream%20Deck.intune.recipe)                                  |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Brave.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Brave/Brave.intune.recipe)                                                                                 |[apettinen-recipes](https://github.com/autopkg/apettinen-recipes)            |
|[Inkscape.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Inkscape/Inkscape.intune.recipe)                                                                        |[hansen-m-recipes](https://github.com/autopkg/hansen-m-recipes)              |
|[VirtualBox.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/VirtualBox/VirtualBox.intune.recipe)                                                                  |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[BetterDisplay.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/BetterDisplay/BetterDisplay.intune.recipe)                                                         |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[PyCharm-CE.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/JetBrains/PyCharm-CE.intune.recipe)                                                                   |[bnpl-recipes](https://github.com/autopkg/bnpl-recipes)                      |
|[IntelliJ-IDEA-UE.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/JetBrains/IntelliJ-IDEA-UE.intune.recipe)                                                       |[bnpl-recipes](https://github.com/autopkg/bnpl-recipes)                      |
|[Webstorm.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/JetBrains/Webstorm.intune.recipe)                                                                       |[bnpl-recipes](https://github.com/autopkg/bnpl-recipes)                      |
|[Rider.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/JetBrains/Rider.intune.recipe)                                                                             |[bnpl-recipes](https://github.com/autopkg/bnpl-recipes)                      |
|[IntelliJ-IDEA-CE.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/JetBrains/IntelliJ-IDEA-CE.intune.recipe)                                                       |[bnpl-recipes](https://github.com/autopkg/bnpl-recipes)                      |
|[PyCharm-PE.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/JetBrains/PyCharm-PE.intune.recipe)                                                                   |[bnpl-recipes](https://github.com/autopkg/bnpl-recipes)                      |
|[CarbonCopyCloner.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Carbon%20Copy%20Cloner/CarbonCopyCloner.intune.recipe)                                          |[keeleysam-recipes](https://github.com/autopkg/keeleysam-recipes)            |
|[Privileges.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Privileges/Privileges.intune.recipe)                                                                  |[rtrouton-recipes](https://github.com/autopkg/rtrouton-recipes)              |
|[WindowsApp.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/WindowsApp/WindowsApp.intune.recipe)                                                                  |[jc0b-recipes](https://github.com/autopkg/jc0b-recipes)                      |
|[Notion.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Notion/Notion.intune.recipe)                                                                              |[swy-recipes](https://github.com/autopkg/swy-recipes)                        |
|[Rectangle.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Rectangle/Rectangle.intune.recipe)                                                                     |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[AirFoil.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/RougueAmoeba/AirFoil.intune.recipe)                                                                      |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[EscrowBuddy.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Escrow%20Buddy/EscrowBuddy.intune.recipe)                                                            |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[OBS.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/OBS/OBS.intune.recipe)                                                                                       |[nstrauss-recipes](https://github.com/autopkg/nstrauss-recipes)              |
|[VLC.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/VLC/VLC.intune.recipe)                                                                                       |[recipes](https://github.com/autopkg/recipes)                                |
|[AdobeReader.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Adobe/AdobeReader.intune.recipe)                                                                     |[recipes](https://github.com/autopkg/recipes)                                |
|[AdobeCreativeCloudUniversal.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Adobe/AdobeCreativeCloudUniversal.intune.recipe)                                     |[rtrouton-recipes](https://github.com/autopkg/rtrouton-recipes)              |
|[Onyx15.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Onyx/Onyx15.intune.recipe)                                                                                |[peshay-recipes](https://github.com/autopkg/peshay-recipes)                  |
|[Onyx13.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Onyx/Onyx13.intune.recipe)                                                                                |[peshay-recipes](https://github.com/autopkg/peshay-recipes)                  |
|[Onyx14.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Onyx/Onyx14.intune.recipe)                                                                                |[peshay-recipes](https://github.com/autopkg/peshay-recipes)                  |
|[TeamViewer.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/TeamViewer/TeamViewer.intune.recipe)                                                                  |[hjuutilainen-recipes](https://github.com/autopkg/hjuutilainen-recipes)      |
|[TeamViewerQS.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/TeamViewer/TeamViewerQS.intune.recipe)                                                              |[hjuutilainen-recipes](https://github.com/autopkg/hjuutilainen-recipes)      |
|[GitHubDesktop.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/GitHub/GitHubDesktop.intune.recipe)                                                                |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Figma.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Figma/Figma.intune.recipe)                                                                                 |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Santa.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Santa/Santa.intune.recipe)                                                                                 |[autopkg-recipes](https://github.com/autopkg/autopkg-recipes)                |
|[SplashtopBusiness.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Splashtop/SplashtopBusiness.intune.recipe)                                                     |[peetinc-recipes](https://github.com/autopkg/peetinc-recipes)                |
|[Tor.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Tor/Tor.intune.recipe)                                                                                       |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[SuperDuper.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/SuperDuper/SuperDuper.intune.recipe)                                                                  |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[GitKraken.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Axosoft/GitKraken.intune.recipe)                                                                       |[hjuutilainen-recipes](https://github.com/autopkg/hjuutilainen-recipes)      |
|[CodeWhisperer.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/CodeWhisperer/CodeWhisperer.intune.recipe)                                                         |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[iTerm2.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/iTerm2/iTerm2.intune.recipe)                                                                              |[hjuutilainen-recipes](https://github.com/autopkg/hjuutilainen-recipes)      |
|[Bitwarden.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Bitwarden/Bitwarden.intune.recipe)                                                                     |[grumpydrew-recipes](https://github.com/autopkg/grumpydrew-recipes)          |
|[TheUnarchiver.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/The%20Unarchiver/TheUnarchiver.intune.recipe)                                                      |[recipes](https://github.com/autopkg/recipes)                                |
|[Handbrake.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Handbrake/Handbrake.intune.recipe)                                                                     |[recipes](https://github.com/autopkg/recipes)                                |
|[HiddenBar.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Hidden%20Bar/HiddenBar.intune.recipe)                                                                  |[autopkg-recipes](https://github.com/autopkg/autopkg-recipes)                |
|[Tailscale.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Tailscale/Tailscale.intune.recipe)                                                                     |[macprince-recipes](https://github.com/autopkg/macprince-recipes)            |
|[CloudflareWARP.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Cloudflare%20WARP/CloudflareWARP.intune.recipe)                                                   |[mikestechshop-recipes](https://github.com/autopkg/mikestechshop-recipes)    |
|[JumpDesktopConnect.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Jump%20Desktop/JumpDesktopConnect.recipe)                                                            |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[JumpDesktop.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Jump%20Desktop/JumpDesktop.intune.recipe)                                                            |[autopkg-recipes](https://github.com/autopkg/autopkg-recipes)                |
|[Zoom.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Zoom/Zoom.intune.recipe)                                                                                    |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[AmazonCorretto.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Amazon%20Corretto/AmazonCorretto.intune.recipe)                                                   |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[AmazonCLI.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Amazon%20CLI/AmazonCLI.intune.recipe)                                                                  |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Azul Zulu OpenJDK 11 LTS.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Azul%20Zulu%20OpenJDK%2011%20LTS/Azul%20Zulu%20OpenJDK%2011%20LTS.intune.recipe)        |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Claude.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Anthropic/Claude.intune.recipe)                                                                           |[almenscorner-recipes](https://github.com/autopkg/almenscorner-recipes)      |
|[Slack.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Slack/Slack.intune.recipe)                                                                                 |[kevinmcox-recipes](https://github.com/autopkg/kevinmcox-recipes)            |
|[LibreOffice.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/LibreOffice/LibreOffice.intune.recipe)                                                               |[hjuutilainen-recipes](https://github.com/autopkg/hjuutilainen-recipes)      |
|[Grammarly.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Grammarly/Grammarly.intune.recipe)                                                                     |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[SupportCompanion.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/SupportCompanion/SupportCompanion.intune.recipe)                                                |[almenscorner-recipes](https://github.com/autopkg/almenscorner-recipes)      |
|[SupportCompanion.munki.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/SupportCompanion/SupportCompanion.munki.recipe)                                                  |[almenscorner-recipes](https://github.com/autopkg/almenscorner-recipes)      |
|[AmazonChime.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Amazon%20Chime/AmazonChime.intune.recipe)                                                            |[moofit-recipes](https://github.com/autopkg/moofit-recipes)                  |
|[Kitty.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Kitty/Kitty.intune.recipe)                                                                                 |[apizz-recipes](https://github.com/autopkg/apizz-recipes)                    |
|[LittleSnitch.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Little%20Snitch/LittleSnitch.intune.recipe)                                                         |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Azure Data Studio.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Azure%20Data%20Studio/Azure%20Data%20Studio.intune.recipe)                                     |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Arc.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Arc/Arc.intune.recipe)                                                                                       |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Kubectl.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Kubernetes/Kubectl.intune.recipe)                                                                        |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[NordVPN.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/NordVPN/NordVPN.intune.recipe)                                                                           |[ahousseini-recipes](https://github.com/autopkg/ahousseini-recipes)          |
|[Ollama.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Ollama/Ollama.intune.recipe)                                                                              |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Vivaldi.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Vivaldi/Vivaldi.intune.recipe)                                                                           |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[FileZilla.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/FileZilla/FileZilla.intune.recipe)                                                                     |[keeleysam-recipes](https://github.com/autopkg/keeleysam-recipes)            |
|[Alfred5.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Alfred/Alfred5.intune.recipe)                                                                            |[hjuutilainen-recipes](https://github.com/autopkg/hjuutilainen-recipes)      |
|[Anydesk.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Anydesk/Anydesk.intune.recipe)                                                                           |[jpiel-recipes](https://github.com/autopkg/jpiel-recipes)                    |
|[Blender.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Blender/Blender.intune.recipe)                                                                           |[hjuutilainen-recipes](https://github.com/autopkg/hjuutilainen-recipes)      |
|[ExpressVPN.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/ExpressVPN/ExpressVPN.intune.recipe)                                                                  |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[BetterTouchTool.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/BetterTouchTool/BetterTouchTool.intune.recipe)                                                   |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Acorn.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/FlyingMeat/Acorn.intune.recipe)                                                                            |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Asana.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Asana/Asana.intune.recipe)                                                                                 |[mikestechshop-recipes](https://github.com/autopkg/mikestechshop-recipes)    |
|[AirParrot3.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/AirParrot%203/AirParrot3.intune.recipe)                                                               |[ahousseini-recipes](https://github.com/autopkg/ahousseini-recipes)          |
|[Godot 3.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Godot%203/Godot%203.intune.recipe)                                                                       |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Maven.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Apache/Maven.intune.recipe)                                                                                |[n8felton-recipes](https://github.com/autopkg/n8felton-recipes)              |
|[Godot 4.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Godot%204/Godot%204.intune.recipe)                                                                       |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[Wireshark.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Wireshark/Wireshark.intune.recipe)                                                                     |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[Git.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Git/Git.intune.recipe)                                                                                       |[jleggat-recipes](https://github.com/autopkg/jleggat-recipes)                |
|[CleanMyMac3.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/MacPaw/CleanMyMac3.intune.recipe)                                                                    |[homebysix-recipes](https://github.com/autopkg/homebysix-recipes)            |
|[1password.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/1password/1password.intune.recipe)                                                                     |[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[ChatGPT.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/OpenAI/ChatGPT.intune.recipe)                                                                            |[rtrouton-recipes](https://github.com/autopkg/rtrouton-recipes)              |
|[MicrosoftAzureStorageExplorer.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Microsoft%20Azure%20Storage%20Explorer/MicrosoftAzureStorageExplorer.intune.recipe)|[dataJAR-recipes](https://github.com/autopkg/dataJAR-recipes)                |
|[CitrixWorkspace.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Citrix/CitrixWorkspace.intune.recipe)                                                            |[rtrouton-recipes](https://github.com/autopkg/rtrouton-recipes)              |
|[Parsec.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/Parsec/Parsec.intune.recipe)                                                                              |[macprince-recipes](https://github.com/autopkg/macprince-recipes)            |
|[UTM.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/UTM/UTM.intune.recipe)                                                                                       |[ahousseini-recipes](https://github.com/autopkg/ahousseini-recipes)          |
|[KeePassXC.intune.recipe](https://github.com/autopkg/almenscorner-recipes/blob/main/KeePassXC/KeePassXC.intune.recipe)                                                                     |[n8felton-recipes](https://github.com/autopkg/n8felton-recipes)              |