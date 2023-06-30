# Caesar-cipher
The Caesar cipher, also known as the shift cipher, is a simple encryption technique that involves shifting the letters of the alphabet by a fixed number of positions. It is named after Julius Caesar, who is said to have used it for communication.

Here's how the Caesar cipher works:

Choose a shift value: Select a number to determine the amount of shifting for the letters. For example, a shift value of 3 means that each letter will be replaced by the letter three positions ahead in the alphabet.

Mapping the alphabet: Create a mapping between the original alphabet and the shifted alphabet. For example, with a shift value of 3, the mapping would be:

Original: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Shifted: X Y Z A B C D E F G H I J K L M N O P Q R S T U V W


Encryption: To encrypt a message, replace each letter in the original message with the corresponding shifted letter. Ignore any non-alphabetic characters and maintain the case (uppercase or lowercase) of the original letters. For example, using a shift value of 3:

Original message: "HELLO, WORLD!"
Encrypted message: "EBIIL, TLOIA!"
Decryption: To decrypt a message encrypted with the Caesar cipher, apply the reverse shift. Replace each shifted letter with the corresponding original letter. For example, using a shift value of 3:

Encrypted message: "EBIIL, TLOIA!"
Decrypted message: "HELLO, WORLD!"
The Caesar cipher is a relatively weak encryption method, as there are only 25 possible shift values, making it susceptible to brute-force attacks. It is often used for educational purposes and as a stepping stone to more complex encryption algorithms.




