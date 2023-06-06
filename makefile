#
# MAKEFILE
#

# Example on how to run gematria:
example_build:
	python lib/main.py testeteste__cicada

arg_build:
	python lib/main.py $(m)

hash_build:
	python hash.py . --input inputs/5.txt
