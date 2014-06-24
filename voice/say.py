import sys, os

# gets all the voices possible for the current user
def getVoices(printOrNot):
    # get the output from the command
    a = os.popen("say -v ?").read()
    voices = a.split('\n')
    voices = filter(None, voices)
    returnVoices = []

    # go through each voice
    for s in voices:

        # get details
        details = s.split(' ')
        details = filter(None, details)
        name = details[0].strip()
        currentValue = 1

        # get the full name if it contains 2 words
        while '_' not in details[currentValue]:
            name = name + ' ' + details[currentValue]
            currentValue = currentValue + 1

        # get the language it is
        language = details[currentValue].strip()

        # print it if the user wants to print it
        if not name.isspace() and printOrNot:
            print name, language
        returnVoices.append([name, language])
    return returnVoices

# says the command the user gives, in the voice given
def say(command, voice, allVoices):
    # if input is not correct
    if command is '' or voice is '' or allVoices is None:
        print 'Please provide the correct input'
        return

    # check to see if voice exists in the allVoices array
    found = False
    for i in allVoices:
        if voice == i[0]:
            found = True

    # if it existe then we say the command in that voice
    if found is False:
        print 'Voice not recognized'
    else:
        os.system('say -v ' + voice + ' ' + command)

# if the user doesn't specify a voice
def sayNoVoice(command):
    os.system('say ' + command)

if __name__ == '__main__':
    # get all voices
    voices = getVoices(False)

    # print
    if '-p' in sys.argv:
        print voices
    # say
    elif '-s' in sys.argv:
        # say without user given voice
        # default system voice
        if '-v' not in sys.argv:
            indexOfs = sys.argv.index('-s')
            sayNoVoice(sys.argv[indexOfs + 1])
        # say with user given voice
        else:
            indexOfs = sys.argv.index('-s')
            indexOfv = sys.argv.index('-v')
            say(sys.argv[indexOfs + 1], sys.argv[indexOfv + 1], voices)
    # print out helpsheet
    else:
        print '''
    -p to print all voices
    -s for the command to say
    -v for the voice
              '''
