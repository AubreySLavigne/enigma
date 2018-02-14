#!/usr/bin/env python3
"""
Emulation of an Enigma Machine
"""


class EnigmaMachine(object):
    """Enigma Machine Emulator"""
    def __init__(self, **kwargs):
        pass

    def encode(self, input):
        """Encodes and Returns the encoded version of input, and advances the machine's state"""
        return input


class Plugboard(object):
    """Enigma Machine Plug board"""
    def __init__(self, config):
        pass


class Scrambler(object):
    """Desc"""
    pass


class Reflector(object):
    """Desc"""
    pass


PLUGBOARD_CONFIG = (('Q', 'T'),
                    ('Z', 'L'),
                    ('H', 'P'),
                    ('O', 'K'),
                    ('B', 'D'),
                    ('X', 'I'),
                    ('S', 'A'),
                    ('G', 'J'),
                    ('N', 'V'),
                    ('C', 'R'))

def main():
    plugboard = Plugboard(PLUGBOARD_CONFIG)
    #scrambler1 = Scrambler()
    #scrambler2 = Scrambler()
    #scrambler3 = Scrambler()
    #reflector = Reflector()
    enigma = EnigmaMachine(Plugboard=plugboard)
                           #Scramblers=[
                               #scrambler1,
                               #scrambler2,
                               #scrambler3],
                           #Reflector=reflector

    input = 'HELLOWORLD'
    output = ''
    for i in input:
        output += enigma.encode(i)

    print('Result: %s' % (output))



if __name__ == '__main__':
    main()

