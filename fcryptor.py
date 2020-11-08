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

	@staticmethod
	def __check_files(path, exists=True, file=True):
		path = os.path.abspath(path)
		if exists and not os.path.exists(path):
			raise ValueError("{} not exists".format(path))
		if file and not os.path.isfile(path):
			raise ValueError("{} is not regular file".format(path))
		return path
	
	@staticmethod
	def __load_file(path):
		return open(path, 'rb').read()

	def crypt(self, inputpath, outpath=None):
		inputpath = FCryptor.__check_files(inputpath)
		input_data = FCryptor.__load_file(inputpath)
		output = super().crypt(input_data)

		if outpath:
			outpath = FCryptor.__check_files(outpath, exists=False, file=False)
			output_file = open(outpath, 'w')
			output_file.write(output)
			output_file.close()
		
		return output
	
	def decrypt(self, inputpath, outpath):
		inputpath = FCryptor.__check_files(inputpath)
		input_data = FCryptor.__load_file(inputpath)
		output = super().decrypt(input_data)
		
		if outpath:
			outpath = FCryptor.__check_files(outpath, exists=False, file=False)
			output_file = open(outpath, 'w')
			output_file.write(output)
			output_file.close()
		
		return output
fc = FCryptor()
fc.crypt("./test.txt", "o.enc")
fc.decrypt("o.enc", "oo.enc")
