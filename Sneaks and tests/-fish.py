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
        if ranfish <= 30: loot = "x" # Short-hand-if because we are cool
        #common
        if ranfish >= 31 and ranfish <= 70: loot = "x"
        #well-known
        if ranfish >= 71 and ranfish <= 100: loot = "x"
        if ranfish >= 101 and ranfish <= 130: loot = "x"
        #known
        if ranfish >= 131 and ranfish <= 150: loot = "x"
        if ranfish >= 151 and ranfish <= 170: loot = "x"
        #fancy
        if ranfish >= 171 and ranfish <= 180: loot = "x"
        if ranfish >= 181 and ranfish <= 190: loot = "x"
        if ranfish >= 191 and ranfish <= 200: loot = "x"
        if ranfish >= 201 and ranfish <= 210: loot = "x"
        if ranfish >= 211 and ranfish <= 220: loot = "x"
        if ranfish >= 221 and ranfish <= 230: loot = "x"
        if ranfish >= 231 and ranfish <= 240: loot = "x"
        if ranfish >= 241 and ranfish <= 250: loot = "x"
        #rare
        if ranfish >= 251 and ranfish <= 255: loot = "x"
        if ranfish >= 256 and ranfish <= 260: loot = "x"
        if ranfish >= 261 and ranfish <= 265: loot = "x"
        if ranfish >= 266 and ranfish <= 270: loot = "x"
        if ranfish >= 271 and ranfish <= 275: loot = "x"
        #very-rare
        if ranfish >= 276 and ranfish <= 278: loot = "x"
        if ranfish >= 279 and ranfish <= 281: loot = "x"
        if ranfish >= 282 and ranfish <= 284: loot = "x"
        if ranfish >= 285 and ranfish <= 287: loot = "x"
        #unknown
        if ranfish >= 288 and ranfish <= 289: loot = "x"
        if ranfish >= 290 and ranfish <= 291: loot = "x"
        if ranfish >= 292 and ranfish <= 293: loot = "x"
        #unique
        if ranfish == 294: loot = "x"
        if ranfish == 295: loot = "x"
        if ranfish == 296: loot = "x"
        if ranfish == 297: loot = "x"
        #cursed
        if ranfish >= 298 and ranfish <= 299: loot = "x"
        if ranfish == 300: loot = "x"

        print("xuserx reeled in " + str(loot) + "!")

#return



# a is the chat array. a[0] inital, a[1] first parameter and so on
# self.__sendChat_delayed("%s reeled in a quest scroll!!!" % self.sm.getUsernameColoured(source))
# [username] reeled [first word of loot] in:#bot during:[date of event]     this can be used to search the chat log after the event
