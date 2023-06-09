"""
    Main "Analyzing" script
"""

from __future__ import annotations
import logging
import gematria as gematria
from hashing import Hashing
from writer import Writer
import utils

logger = logging.getLogger(__name__)

class Analyse:
	"""Class that will take a message and do processing on the string"""

	# String to be processed
	message: str

	# Custom file writer
	writer: Writer

	def __init__(self, message: str, writer: Writer) -> None:
		self.message = message
		self.writer = writer
		self.hasher = Hashing(self.message, self.writer)

	def analyse(self) -> None:
		"""Main analyze function"""
		# Hash and compare string into all implemented hash fn's
		self.hasher.str_check()

		# Gematria related processing
		self.gematria()
	
	def gematria_sum_prime(self, message: str) -> None:
		"""
			Gematria Processing of prime sums
				1. Message + Atbash
				2. Words + Atbash
				3. Lines + Atbash
		"""
		# Assume we are in runes
		runic_message = gematria.Runes(message).to_runes()

		# 1. Message
		message_sum = runic_message.gematria_sum()
		message_prime, message_emirp = utils.get_prime_and_emirp(message_sum)

		# 2. Words
		words_sum = runic_message.gematria_sum_words()
		words_prime, words_emirp = utils.get_prime_and_emirp(words_sum)

		# 3. Lines
		lines_sum = runic_message.gematria_sum_lines()
		lines_prime, lines_emirp = utils.get_prime_and_emirp(lines_sum)

		# Change to atbash
		atbash_message = runic_message.atbash()

		# Atbash 1. Message
		atbash_message_sum = atbash_message.gematria_sum()
		atbash_message_prime, atbash_message_emirp = utils.get_prime_and_emirp(atbash_message_sum)		

		# Atbash 2. Words
		atbash_words_sum = atbash_message.gematria_sum_words()
		atbash_words_prime, atbash_words_emirp = utils.get_prime_and_emirp(atbash_words_sum)

		# Atbash 3. Lines
		atbash_lines_sum = atbash_message.gematria_sum_lines()
		atbash_lines_prime, atbash_lines_emirp = utils.get_prime_and_emirp(atbash_lines_sum)
		
		# TODO .to_numbers() prime list

	def gematria(self) -> None:
		"""Gematria Related Processing"""
		# Logging
		runic_version = gematria.Runes(self.message).to_runes()
		latin_version = gematria.Runes(self.message).to_latin()
		title_str = "GEMATRIA PROCESSING...\n\tRUNIC: " + str(runic_version) + "\n\tLATIN: " + str(latin_version)		
		logger.info(title_str)
		self.writer.title(title_str)
		
		# Gematria sum & Prime
		self.gematria_sum_prime(self.message)
