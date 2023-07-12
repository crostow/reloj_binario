def seg(self, s):
    apagar = (u"border: solid 3px;\n"
              "background-color: rgb(222, 221, 218);\n"
              "border-radius: 25;\n"
              "")

    prender = (u"border: solid 3px;\n"
               "background-color: rgb(240, 0, 0);\n"
               "border-radius: 25;\n"
               "")
    if int(s[0]) == 0:
        self.ui.l4.setStyleSheet(apagar)
        self.ui.l5.setStyleSheet(apagar)
        self.ui.l6.setStyleSheet(apagar)
        self.ui.l7.setStyleSheet(apagar)
        if int(s[1]) == 0:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 1:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 2:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 3:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 4:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 5:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 6:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 7:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 8:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(prender)
        elif int(s[1]) == 9:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(prender)
    if int(s[0]) == 1:
        self.ui.l4.setStyleSheet(prender)
        self.ui.l5.setStyleSheet(apagar)
        self.ui.l6.setStyleSheet(apagar)
        self.ui.l7.setStyleSheet(apagar)
        if int(s[1]) == 0:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 1:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 2:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 3:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 4:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 5:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 6:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 7:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(prender)
            self.ui.l2.setStyleSheet(prender)
            self.ui.l3.setStyleSheet(apagar)
        elif int(s[1]) == 8:
            self.ui.l0.setStyleSheet(apagar)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(prender)
        elif int(s[1]) == 9:
            self.ui.l0.setStyleSheet(prender)
            self.ui.l1.setStyleSheet(apagar)
            self.ui.l2.setStyleSheet(apagar)
            self.ui.l3.setStyleSheet(prender)
    if int(s[0]) == 2:
            self.ui.l4.setStyleSheet(apagar)
            self.ui.l5.setStyleSheet(prender)
            self.ui.l6.setStyleSheet(apagar)
            self.ui.l7.setStyleSheet(apagar)
            if int(s[1]) == 0:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 1:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 2:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 3:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 4:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 5:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 6:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 7:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 8:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
            elif int(s[1]) == 9:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
    if int(s[0]) == 3:
            self.ui.l4.setStyleSheet(prender)
            self.ui.l5.setStyleSheet(prender)
            self.ui.l6.setStyleSheet(apagar)
            self.ui.l7.setStyleSheet(apagar)
            if int(s[1]) == 0:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 1:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 2:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 3:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 4:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 5:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 6:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 7:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 8:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
            elif int(s[1]) == 9:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
    if int(s[0]) == 4:
            self.ui.l4.setStyleSheet(apagar)
            self.ui.l5.setStyleSheet(apagar)
            self.ui.l6.setStyleSheet(prender)
            self.ui.l7.setStyleSheet(apagar)
            if int(s[1]) == 0:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 1:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 2:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 3:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 4:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 5:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 6:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 7:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 8:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
            elif int(s[1]) == 9:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
    if int(s[0]) == 5:
            self.ui.l4.setStyleSheet(prender)
            self.ui.l5.setStyleSheet(apagar)
            self.ui.l6.setStyleSheet(prender)
            self.ui.l7.setStyleSheet(apagar)
            if int(s[1]) == 0:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 1:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 2:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 3:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 4:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 5:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 6:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 7:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(prender)
                self.ui.l2.setStyleSheet(prender)
                self.ui.l3.setStyleSheet(apagar)
            elif int(s[1]) == 8:
                self.ui.l0.setStyleSheet(apagar)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
            elif int(s[1]) == 9:
                self.ui.l0.setStyleSheet(prender)
                self.ui.l1.setStyleSheet(apagar)
                self.ui.l2.setStyleSheet(apagar)
                self.ui.l3.setStyleSheet(prender)
