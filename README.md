# Enigma Machine Emulator

This is a for-fun program, so I can practice Python.

For this reason, I will be using Python 3.5.2, and will refrain from  non-standard packages.

**Please Provide Any Feedback, if you have any critiques on how I can improve**

## Enigma Machine?

The *Enigma Machine* was the German Code-Generation Engine used during World War II.

More Information can be found on [Wikipedia](https://en.wikipedia.org/wiki/Enigma_machine)

## This Project

I'm less concerned about the specifics, and more just taking inspiration from  the technique.

For that reason, I will be randomly generating some of this data, instead of  relying on historical configurations.

I am taking inspiration from the description of the machine found on [this page](http://enigma.louisedade.co.uk/howitworks.html)

![Enigma Machine - (c) 2006 Louise Dade](http://enigma.louisedade.co.uk/wiringdiagram.png)

### How to use it

1. Configure the Machine for Use. (Historically, the configurations would be known ahead of time, so the recipient would know which settings to use)

2. Using the keyboard (that is, the keyboard of the Enigma Machine), press one key at a time.

3. The Encoded Character would light up on the lightboard.

### Modules

This is a description of the individual pieces of this representation. Some of this has been changed for the sake of simplicity.

#### Input

In a physical machine, this would be a keyboard. 

For our purposes, this will be the input to the encryption function.

Values may be A-Z, no spaces, symbols, numbers.

#### Output

In a physical Machine, this was a series of lights. 

When pressing the input, the value would be encoded, and the correct light would be displayed.

Once again, values may be A-Z, no spaces, symbols, numbers.

#### Plugboard

This is one way the machine was configured. 

This is a switchboard is provided to allow any two characters to be "swapped".

For example, C and X could be linked. 

In this case, an input of C would be passed forward as X, and an input of X would be passed forward as C.

If a letter was not configured in the Plugboard, it would be forwarded unmodified (e.g. A is pressed and A is received).

#### Rotors/Scramblers

The Enigma Machine had 3 slots for these scrambler drums. 

Each Drum had 26 positional contacts for input and output, and the variation differed for each drum.

After each key pressed, the position for the right-most motor would increment.

Each rotor also had a certain position marked. 

If incrementing the position for a given rotor caused that certain position to be reached, it would also increment the rotor to it left.

In the case of the middle rotor, it would also increase its position again (in effect, it would move twice).

While the rotors themselves were static, different drums can be used in different order, each with a different starting position.

#### Reflector

The Reflector will take the input (scrambled by the rotors) and return it down a different path.

The input/output pairs were mirrored. 

If input is position 3 with output position 19, input of 19 would produce 3.

