from cryptography.fernet import Fernet

class FCryptor:
	def __init__(self, key=None):
		if not key:
			key = Fernet.generate_key()
		FCryptor.__check_type_is(key, bytes)
		self.key = key.decode()
		self.__fkey = Fernet(key)

	@staticmethod
	def __check_type_is(item, be, raise_error=True):
		if type(item) != be:
			if raise_error:
				raise ValueError(str(item)+" must be bytes")
			return False
		return True

	def crypt(self, message):
		FCryptor.__check_type_is(message, bytes)
		return self.__fkey.encrypt(message).decode()

	def decrypt(self, message):
		FCryptor.__check_type_is(message, bytes)
		return self.__fkey.decrypt(message).decode()
