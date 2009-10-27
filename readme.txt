###################################################################################
#
# FunnyFarm (due to lack of inspiration)
# Plugin for B3 (www.bigbrotherbot.com)
# (c) 2006 www.xlr8or.com (mailto:xlr8or@xlr8or.com)
#
# This program is free software and licensed under the terms of
# the GNU General Public License (GPL), version 2.
#
# http://www.gnu.org/copyleft/gpl.html
###################################################################################

FunnyFarm (v1.0.0) for B3
###################################################################################

With this nifty little plugin you'll be able to alter gamespeed and gravity for
a short period of time and thus make your playercrowd goof around for a few.

 !ffjump <seconds> - Low Gravity
 !ffspeedup <seconds> - High Gamespeed
 !ffberserk <seconds> - High Gamespeed and Low Gravity
 !ffreset - Stop effect early, all effects are timed so you wont need this much

Each command can be leveled in the config file.


Requirements:
###################################################################################

- B3 version 1.1.0 or higher


Installation:
###################################################################################

1. Unzip the contents of this package into your B3 folder. It will
place the .py file in b3/extplugins and the config file .xml in
your b3/extplugins/conf folder.

2. Open the .xml file with your favorit editor and modify the
levels if you want them different. Do not edit the command-names
for they will not function under a different name.

3. Open your B3.xml file (in b3/conf) and add the next line in the
<plugins> section of the file:

<plugin name="funnyfarm" priority="12" config="@b3/extplugins/conf/funnyfarm.xml"/>

The numer 12 in this just an example. Make sure it fits your
plugin list.


Changelog
###################################################################################
v1.0.0         : Initial release


###################################################################################
xlr8or - 25 jan 2006 - www.bigbrotherbot.com // www.xlr8or.com