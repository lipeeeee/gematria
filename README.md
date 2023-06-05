# gematria
3301 Cryptography Tool

# Hashing
In [Page 56](https://static.wikia.nocookie.net/uncovering-cicada/images/2/2f/56.jpg/revision/latest/scale-to-width-down/1000?cb=20150109104852) of LP there is a message which is encrypted using (prime numbers -1)as a stream cipher. The `F` rune in the plaintext is an interrupter and is not encrypted.
```
AN END: WITHIN THE DEEP WEB TH
ERE EXISTS A PAGE THAT HA
SHES TO:
36367763ab73783c7af284446c
59466b4cd653239a311cb7116
d4618dee09a8425893dc7500b
464fdaf1672d7bef5e891c6e227
4568926a49fb4f45132c2a8b4
IT IS THE DUTY OF EUERY PILGR
IM TO SEEK OUT THIS PAGE.
```
The full hash is: (512 bits)
```36367763ab73783c7af284446c59466b4cd653239a311cb7116d4618dee09a8425893dc7500b464fdaf1672d7bef5e891c6e2274568926a49fb4f45132c2a8b4```

It indicates that there is a page on the deep web, most likely a **onion v2 URL**, which when hashed *(The hashing algorithm is not known, but potential candidates are SHA-512, BLAKE-512 or BLAKE2b)* produces the full hash.
The hash can also be a unique file identifier for deep web applications such as Freenet, GnuNET or P2P file sharing systems, which use Distributed Hash Tables.

# TODO
