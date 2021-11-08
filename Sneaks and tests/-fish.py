import random 


# Get user input and split it into array "a", similar to the ror_client script
inp = input(": ")
a = inp.split(" ", 1)   # This array has only the initial command and the rest as "a[1]" (parameters)
                        # We don't actually need to do this but let's add this for future commands :D (we are not using parameters in this command)

if a[0] == "-fish":
    if len(a) > 1: # Check if the user tried to use this command like "-rip"
        print("You don't need any parameters for this command...")
    else:
        ranfish = random.randint(1,300) # Get one from 300 possible results
        
        # Here comes the main decision
        print(ranfish) # Debug
        if ranfish <= 30: pass # Short-hand-if because we are cool
        #common
        if ranfish >= 31 and ranfish <= 70: pass
        #well-known
        if ranfish >= 71 and ranfish <= 100: pass
        if ranfish >= 101 and ranfish <= 130: pass
        #known
        if ranfish >= 131 and ranfish <= 150: pass
        if ranfish >= 151 and ranfish <= 170: pass
        #fancy
        if ranfish >= 171 and ranfish <= 180: pass
        if ranfish >= 181 and ranfish <= 190: pass
        if ranfish >= 191 and ranfish <= 200: pass
        if ranfish >= 201 and ranfish <= 210: pass
        if ranfish >= 211 and ranfish <= 220: pass
        if ranfish >= 221 and ranfish <= 230: pass
        if ranfish >= 231 and ranfish <= 240: pass
        if ranfish >= 241 and ranfish <= 250: pass
        #rare
        if ranfish >= 251 and ranfish <= 255: pass
        if ranfish >= 256 and ranfish <= 260: pass
        if ranfish >= 261 and ranfish <= 265: pass
        if ranfish >= 266 and ranfish <= 270: pass
        if ranfish >= 271 and ranfish <= 275: pass
        #very-rare
        if ranfish >= 276 and ranfish <= 278: pass
        if ranfish >= 279 and ranfish <= 281: pass
        if ranfish >= 282 and ranfish <= 284: pass
        if ranfish >= 285 and ranfish <= 287: pass
        #unknown
        if ranfish >= 288 and ranfish <= 289: pass
        if ranfish >= 290 and ranfish <= 291: pass
        if ranfish >= 292 and ranfish <= 293: pass
        #unique
        if ranfish == 294: pass
        if ranfish == 295: pass
        if ranfish == 296: pass
        if ranfish == 297: pass
        #cursed
        if ranfish >= 298 and ranfish <= 299: pass
        if ranfish == 300: pass


#return



# a is the chat array. a[0] inital, a[1] first parameter and so on
# self.__sendChat_delayed("%s reeled in a quest scroll!!!" % self.sm.getUsernameColoured(source))
# [username] reeled [first word of loot] in:#bot during:[date of event]     this can be used to search the chat log after the event
