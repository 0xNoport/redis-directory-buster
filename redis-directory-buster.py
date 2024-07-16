import socket
import argparse

class Main:
	def __init__(self):
		parser = argparse.ArgumentParser(
			prog="redis-directory-buster",
			description="Perform directory enumeration by using redis",
			epilog="")

		parser.add_argument('-i','--rhost', required=True, help='IP address or hostname of the target redis server')
		parser.add_argument('-port', '--rport', default=6379, required=False, help='Port of the target redis server. Default:6379')
		parser.add_argument('-w', '--wordlist', required=True, help='File to use to find paths, containing, e.g. /var/ or /var/lib line per line.')
		parser.add_argument('-u', '--username', required=False, help='Username used to authenticate to redis')
		parser.add_argument('-pass', '--password', required=False, help='Password used to authenticate to redis')
		args = parser.parse_args()

		if args.username is not None and args.password is None:
			parser.error("If you specify a username you have to specify a password for the user.")
		self.brute_force(args)

	def brute_force(self, args):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((args.rhost, args.rport))

		if args.username is not None:
			command = f"AUTH {args.username} {args.password}\n"
			s.send(command.encode())
			s.recv(1024)
		elif args.password is not None:
			command = f"AUTH {args.password}\n"
			s.send(command.encode())
			s.recv(1024)
		
		with open(args.wordlist, "r") as file:
			for line in file:
				command = f"config set dir {line}\n"
				s.send(command.encode())
				print(line, end="") if s.recv(1024).strip().decode() == "+OK" else None

		s.close()

if __name__ == "__main__":
	main = Main()

