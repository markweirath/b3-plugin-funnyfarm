#
# FunnyFarm Plugin for BigBrotherBot(B3) (www.bigbrotherbot.com)
# Copyright (C) 2005 www.xlr8or.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# Changelog:
# 
# 

__version__ = '1.0.0'
__author__  = 'xlr8or'

import b3, re, threading
import b3.events
from b3 import functions
from b3 import clients

#--------------------------------------------------------------------------------------------------
class FunnyfarmPlugin(b3.plugin.Plugin):
  _adminPlugin = None

  def startup(self):
    """\
    Initialize plugin settings
    """

    global var_speed, var_gravity

    # get the admin plugin so we can register commands
    self._adminPlugin = self.console.getPlugin('admin')
    if not self._adminPlugin:
      # something is wrong, can't start without admin plugin
      self.error('Could not find admin plugin')
      return False
    
    # register our commands
    if 'commands' in self.config.sections():
      for cmd in self.config.options('commands'):
        level = self.config.get('commands', cmd)
        sp = cmd.split('-')
        alias = None
        if len(sp) == 2:
          cmd, alias = sp

        func = self.getCmd(cmd)
        if func:
          self._adminPlugin.registerCommand(self, cmd, level, func, alias)

    # Get the standard values from our gameserver, so we know where to go back to.
    var_speed = self.console.getCvar('g_speed').getInt()
    var_gravity = self.console.getCvar('g_gravity').getInt()

    self.debug('Started: g_speed = %s, g_gravity = %s' % (var_speed, var_gravity))


  def getCmd(self, cmd):
    cmd = 'cmd_%s' % cmd
    if hasattr(self, cmd):
      func = getattr(self, cmd)
      return func

    return None


  def onEvent(self, event):
    """\
    Handle intercepted events
    """


  def cmd_ffreset(self, data, client, cmd=None):
    """\
    Reset funnyfarm commands
    """
    self.console.say('^1*** Back to normal again! ***')
    self.console.setCvar('g_speed','%s' % var_speed)
    self.console.setCvar('g_gravity','%s' % var_gravity)
    client.message('^7Resetting g_speed: %s, g_gravity: %s' % (var_speed, var_gravity) )


  def cmd_ffspeedup(self, data, client, cmd=None):
    """\
    <duration> - Give us a speedboost. (Max. 60 seconds allowed)
    """

    if re.match('^([0-9]+)\s*$', data, re.I):
      duration = int(data)
    else:
      client.message('^7Using 15 seconds timespan.')
      duration = 15

    if duration > 60:
      client.message('^7Using 60 seconds timespan.')
      duration = 60

    t = threading.Timer(duration, self.cmd_ffreset, (data, client,))

    self.console.setCvar( 'g_speed','500' )
    self.console.say('^1*** Adrenaline Injected! Use it wisely! ***')
    t.start()

    return True


  def cmd_ffjump(self, data, client, cmd=None):
    """\
    <duration> - Give us low gravity. (Max. 60 seconds allowed)
    """

    if re.match('^([0-9]+)\s*$', data, re.I):
      duration = int(data)
    else:
      client.message('^7Using 15 seconds timespan.')
      duration = 15

    if duration > 60:
      client.message('^7Using 60 seconds timespan.')
      duration = 60

    t = threading.Timer(duration, self.cmd_ffreset, (data, client,))

    self.console.setCvar( 'g_gravity','50' )
    self.console.say('^1*** Do not jump too high! ***')
    t.start()

    return True


  def cmd_ffberserk(self, data, client, cmd=None):
    """\
    <duration> - Give us low gravity and high speed. (Max. 60 seconds allowed)
    """

    if re.match('^([0-9]+)\s*$', data, re.I):
      duration = int(data)
    else:
      client.message('^7Using 15 seconds timespan.')
      duration = 15

    if duration > 60:
      client.message('^7Using 60 seconds timespan.')
      duration = 60

    t = threading.Timer(duration, self.cmd_ffreset, (data, client,))

    self.console.setCvar( 'g_gravity','50' )
    self.console.setCvar( 'g_speed','500' )
    self.console.say('^1*** Let\'s go crazy! ***')
    t.start()

    return True

if __name__ == '__main__':
  print '\nThis is version '+__version__+' by '+__author__+' for BigBrotherBot.\n'
