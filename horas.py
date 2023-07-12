def hrs(self, h):
    apagar = (u"border: solid 3px;\n"
              "background-color: rgb(222, 221, 218);\n"
              "border-radius: 25;\n"
              "")

    prender = (u"border: solid 3px;\n"
               "background-color: rgb(240, 0, 0);\n"
               "border-radius: 25;\n"
               "")
    if int(h[0]) == 0:
        self.ui.l20.setStyleSheet(apagar)
        self.ui.l21.setStyleSheet(apagar)
        self.ui.l22.setStyleSheet(apagar)
        self.ui.l23.setStyleSheet(apagar)
        if int(h[1]) == 0:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 1:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 2:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 3:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 4:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 5:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 6:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 7:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 8:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
        elif int(h[1]) == 9:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
    if int(h[0]) == 1:
        self.ui.l20.setStyleSheet(prender)
        self.ui.l21.setStyleSheet(apagar)
        self.ui.l22.setStyleSheet(apagar)
        self.ui.l23.setStyleSheet(apagar)
        if int(h[1]) == 0:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 1:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 2:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 3:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 4:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 5:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 6:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 7:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 8:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
        elif int(h[1]) == 9:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
    if int(h[0]) == 2:
        self.ui.l20.setStyleSheet(apagar)
        self.ui.l21.setStyleSheet(prender)
        self.ui.l22.setStyleSheet(apagar)
        self.ui.l23.setStyleSheet(apagar)
        if int(h[1]) == 0:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 1:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 2:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 3:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 4:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 5:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 6:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 7:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 8:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
        elif int(h[1]) == 9:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
    if int(h[0]) == 3:
        self.ui.l20.setStyleSheet(prender)
        self.ui.l21.setStyleSheet(prender)
        self.ui.l22.setStyleSheet(apagar)
        self.ui.l23.setStyleSheet(apagar)
        if int(h[1]) == 0:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 1:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 2:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 3:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 4:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 5:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 6:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 7:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 8:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
        elif int(h[1]) == 9:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
    if int(h[0]) == 4:
        self.ui.l20.setStyleSheet(apagar)
        self.ui.l21.setStyleSheet(apagar)
        self.ui.l22.setStyleSheet(prender)
        self.ui.l23.setStyleSheet(apagar)
        if int(h[1]) == 0:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 1:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 2:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 3:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 4:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 5:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 6:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 7:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 8:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
        elif int(h[1]) == 9:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
    if int(h[0]) == 5:
        self.ui.l20.setStyleSheet(apagar)
        self.ui.l21.setStyleSheet(prender)
        self.ui.l22.setStyleSheet(prender)
        self.ui.l23.setStyleSheet(apagar)
        if int(h[1]) == 0:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 1:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 2:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 3:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 4:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 5:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 6:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 7:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(prender)
            self.ui.l18.setStyleSheet(prender)
            self.ui.l19.setStyleSheet(apagar)
        elif int(h[1]) == 8:
            self.ui.l16.setStyleSheet(apagar)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)
        elif int(h[1]) == 9:
            self.ui.l16.setStyleSheet(prender)
            self.ui.l17.setStyleSheet(apagar)
            self.ui.l18.setStyleSheet(apagar)
            self.ui.l19.setStyleSheet(prender)