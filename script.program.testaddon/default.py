import xbmc
import xbmcgui
import xbmcaddon

ADDON = xbmcaddon.Addon()
CWD = ADDON.getAddonInfo('path').decode('utf-8')


class GUI(xbmcgui.WindowXML):
    def onInit(self):
        xbmc.executebuiltin('Container.SetViewMode(50)')
        listitems = [xbmcgui.ListItem('Turn off TV')]
        listitems[0].setProperty(
            'action',
            'RunScript(/home/pi/bin/turn_off_tv.sh)'
        )
        self.addItems(listitems)
        xbmc.sleep(100)
        self.setFocusId(self.getCurrentContainerId())

    def onClick(self, controlId):
        xbmc.executebuiltin(
            'Notification(Test1, onclick1)'
        )
        if controlId == self.getCurrentContainerId():
            'Notification(Test2, onclick2)'
            listitem = self.getListItem(self.getCurrentListPosition())
            action = listitem.getProperty('action')
            xbmc.executebuiltin(action)


if (__name__ == '__main__'):
    ui = GUI('script-testaddon.xml', CWD, 'default', '1080i', True)
    ui.doModal()
    del ui
