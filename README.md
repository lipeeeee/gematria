# gematria
3301 Cryptography Tool

# Hashing
In [Page 56](https://static.wikia.nocookie.net/uncovering-cicada/images/2/2f/56.jpg) of LP a message was deciphered.
> Within the deep web, there exists a page that hashes to :
> ```
> 36367763ab73783c7af284446c
> 59466b4cd653239a311cb7116
> d4618dee09a8425893dc7500b
> 464fdaf1672d7bef5e891c6e227
> 4568926a49fb4f45132c2a8b4
> ```
> It is the duty of every pilgrim to seek out this page

The full hash is: (512 bits)
```36367763ab73783c7af284446c59466b4cd653239a311cb7116d4618dee09a8425893dc7500b464fdaf1672d7bef5e891c6e2274568926a49fb4f45132c2a8b4```

It indicates that there is a **onion v2 URL**, which when hashed *(The hashing algorithm is not known, but potential candidates are SHA-512, BLAKE-512 or BLAKE2b)* produces the full hash.
The hash can also be a unique file identifier for deep web applications such as Freenet, GnuNET or P2P file sharing systems, which use Distributed Hash Tables.

## Hashing Check Script
I made a script that hashes a given string into various *512 bit* hashing algorithms and then compares the hex digest into the *DWH*.

An example of Gematria hashing "xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion":
```shell
python lib/main.py xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion
> HASHING "xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion"...
> BLAKE2B   1ed7f0c22b5f0b90db36b120f625034fde7b81055275144ffef65597114c4d29773a114a40a9de8179d3fec16f940696b1f8653dadd8be6a01b42c2b8f936184 | IS_DEEPWEB_HASH() -> False >> d:122
> BLAKE512  050c6418b6a34e5c6d49b268bd9a83bd41d2b840383db3833f3bc7d4305a0d58acaa33e963bddf4e91c65d049a427fa01ba88171151a4ea9884f226becdb3523 | IS_DEEPWEB_HASH() -> False >> d:118
> SHA512    f9f7386ff0abd23d43a58718562be3b9a1c50f135e6080277c91be569ceb09d49e08951b691e66e23f01b028dca5968c2f63e2bc99b582f455d358ffee912b18 | IS_DEEPWEB_HASH() -> False >> d:114
> SHA3      a2e0ff145026a8af2a7592b2e6d9d69d0bd3724c47d76ca643acc4dbf4bc8c62abe6474a6e07ac7a9528da579bd567527cf37a95b16912458e737aa84bd4f1d2 | IS_DEEPWEB_HASH() -> False >> d:118
> WHIRLPOOL cfa22a8e02cb9d0c977dcd43a3d42b80fd381d0520a938097a6dedc29579807e427edc8b328c92b141df75833d1412c434ee4065b883084323932e63c9ec5c54 | IS_DEEPWEB_HASH() -> False >> d:121
> SKEIN512  66f8de627d0177ce0aa64bfa97563c5fdd180cbfcb11aeae275b1a21b041d73328d23b6f8dd0405dda8852e18308c457ca61e752b9ef40d34efd00a298f7ac24 | IS_DEEPWEB_HASH() -> False >> d:114
    ALGO                                                                   HEX-DIGEST                                                               HASH COMPARE             DISTANCE
```
Where:

`ALGO` Is the hash function used.

`HEX-DIGEST` Is the output of the message into the hash function.

`HASH COMPARE` Is the flag checking if found the *DWH*.

`DISTANCE` Is the Hamming distance between `HEX-DIGEST` and *DWH*(0 means they are the same, 128 complete opposite)

# TODO
