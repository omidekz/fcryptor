import os
from cryptography.fernet import Fernet

class FCryptorBase:
	def __init__(self, key=None):
		if not key:
			key = Fernet.generate_key()
		FCryptorBase.__check_type_is(key, bytes)
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
		FCryptorBase.__check_type_is(message, bytes)
		return self.__fkey.encrypt(message).decode()

	def decrypt(self, message):
		FCryptorBase.__check_type_is(message, bytes)
		return self.__fkey.decrypt(message).decode()

class FCryptor(FCryptorBase):
	def __init__(self, key=None):
		super().__init__(key)

	def crypt(self, inputpath, outpath=None):
		inputpath = os.path.abspath(inputpath)
		if not os.path.exists(inputpath):
			raise ValueError("{} not exists".format(inputpath))
		if not os.path.isfile(inputpath):
			raise ValueError("{} is not regular file".format(inputpath))
		input_file = open(inputpath, 'rb')
		output = super().crypt(input_file.read())
		input_file.close()

		if outpath:
			outpath = os.path.abspath(outpath)
			output_file = open(outpath, 'w')
			output_file.write(output)
			output_file.close()
		
		return output
