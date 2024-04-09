alphabet = 'abcdefghijklmnopqrstuvwxyz'

def cesar(text, shift, direction):
    output = ''
    for c in text.lower():
        if c in alphabet:
            index = alphabet.index(c)

            if direction == 'encode': index += shift
            elif direction == 'decode': index -= shift

            index %= len(alphabet)
            output += alphabet[index]
        else: output += c
    print(f'The {direction}d text is {output}')

while True:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input('Type your message:\n')
    shift = int(input('Type the shift number:\n'))

    cesar(text, shift, direction)

    yn = input('Type "yes" if you want to go again. Otherwise type "no".\n')
    if yn == 'no':
        print('Goodbye.')
        break