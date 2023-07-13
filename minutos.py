def min (self, m):
    apagar = (u"border: solid 3px;\n"
              "background-color: rgb(222, 221, 218);\n"
              "border-radius: 25;\n"
              "")

    prender = (u"border: solid 3px;\n"
               "background-color: rgb(240, 0, 0);\n"
               "border-radius: 25;\n"
               "")
    
    if int(m[0]) == 0:
        self.ui.l12.setStyleSheet(apagar)
        self.ui.l13.setStyleSheet(apagar)
        self.ui.l14.setStyleSheet(apagar)
        self.ui.l15.setStyleSheet(apagar)
        if int(m[1]) == 0:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 1:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 2:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 3:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 4:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 5:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 6:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 7:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 8:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
        elif int(m[1]) == 9:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
    if int(m[0]) == 1:
        self.ui.l12.setStyleSheet(prender)
        self.ui.l13.setStyleSheet(apagar)
        self.ui.l14.setStyleSheet(apagar)
        self.ui.l15.setStyleSheet(apagar)
        if int(m[1]) == 0:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 1:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 2:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 3:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 4:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 5:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 6:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 7:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 8:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
        elif int(m[1]) == 9:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
    if int(m[0]) == 2:
        self.ui.l12.setStyleSheet(apagar)
        self.ui.l13.setStyleSheet(prender)
        self.ui.l14.setStyleSheet(apagar)
        self.ui.l15.setStyleSheet(apagar)
        if int(m[1]) == 0:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 1:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 2:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 3:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 4:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 5:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 6:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 7:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 8:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
        elif int(m[1]) == 9:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
    if int(m[0]) == 3:
        self.ui.l12.setStyleSheet(prender)
        self.ui.l13.setStyleSheet(prender)
        self.ui.l14.setStyleSheet(apagar)
        self.ui.l15.setStyleSheet(apagar)
        if int(m[1]) == 0:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 1:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 2:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 3:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 4:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 5:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 6:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 7:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 8:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
        elif int(m[1]) == 9:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
    if int(m[0]) == 4:
        self.ui.l12.setStyleSheet(apagar)
        self.ui.l13.setStyleSheet(apagar)
        self.ui.l14.setStyleSheet(prender)
        self.ui.l15.setStyleSheet(apagar)
        if int(m[1]) == 0:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 1:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 2:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 3:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 4:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 5:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 6:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 7:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 8:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
        elif int(m[1]) == 9:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
    if int(m[0]) == 5:
        self.ui.l12.setStyleSheet(prender)
        self.ui.l13.setStyleSheet(apagar)
        self.ui.l14.setStyleSheet(prender)
        self.ui.l15.setStyleSheet(apagar)
        if int(m[1]) == 0:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 1:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 2:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 3:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 4:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 5:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 6:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 7:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(prender)
            self.ui.l10.setStyleSheet(prender)
            self.ui.l11.setStyleSheet(apagar)
        elif int(m[1]) == 8:
            self.ui.l8.setStyleSheet(apagar)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
        elif int(m[1]) == 9:
            self.ui.l8.setStyleSheet(prender)
            self.ui.l9.setStyleSheet(apagar)
            self.ui.l10.setStyleSheet(apagar)
            self.ui.l11.setStyleSheet(prender)
