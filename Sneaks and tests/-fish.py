import random 

       if a[0] == "-fish":
            ranfish = random.randint(1,34)
            if ranfish<=5:
                self.__sendChat_delayed("%s reeled in some junk..." % self.sm.getUsernameColoured(source))
            elif ranfish>6 and ranfish<=10:
                self.__sendChat_delayed("%s reeled in a small tuna" % self.sm.getUsernameColoured(source))
            elif ranfish>11 and ranfish<=14:
                self.__sendChat_delayed("%s reeled in an squid" % self.sm.getUsernameColoured(source))
            elif ranfish>15 and ranfish<=18:
                self.__sendChat_delayed("%s reeled in an largemouth bass" % self.sm.getUsernameColoured(source))
            elif ranfish>19 and ranfish<=24:
                self.__sendChat_delayed("%s reeled in an rainbow trout" % self.sm.getUsernameColoured(source))
            elif ranfish>25 and ranfish<=28:
                self.__sendChat_delayed("%s reeled in a catfish" % self.sm.getUsernameColoured(source))
            elif ranfish>29 and ranfish<=31:
                self.__sendChat_delayed("%s reeled in an unknown fish!" % self.sm.getUsernameColoured(source))
            elif ranfish>32 and ranfish<=33:
                self.__sendChat_delayed("%s reeled in a fishing prize medal from the 60s!" % self.sm.getUsernameColoured(source))
            elif ranfish==34:
                self.__sendChat_delayed("%s reeled in a quest scroll!!!" % self.sm.getUsernameColoured(source))
                
            return



# a is the chat array. a[0] inital, a[1] first parameter and so on
# self.__sendChat_delayed("%s reeled in a quest scroll!!!" % self.sm.getUsernameColoured(source))
# [username] reeled [first word of loot] in:#bot during:[date of event]     this can be used to search the chat log after the event
