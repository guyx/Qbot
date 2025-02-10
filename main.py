#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
from utils.configure.proxy_config import set_proxy
from qbot.gui.mainframe import MainFrame

if __name__ == "__main__":
    # 设置代理，如果你的clash端口不是7890，请修改这里的端口号
    set_proxy(proxy_host="127.0.0.1", proxy_port="7890")
    
    app = wx.App()
    frame = MainFrame(None, title="AI智能量化投研平台")
    frame.Show()

    app.MainLoop()
