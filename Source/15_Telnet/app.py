import telnetlib
class POP3Telnet:
    def __init__(self, host, port):
        # Create a Telnet
        self.tel = telnetlib.Telnet(host, port)
        self.lese_daten()

    def close(self):
        self.tel.close()

    def lese_daten(self):
        return self.tel.read_until(b".\r\n", 20.0)

    def kommando(self, kom):
        self.tel.write(("{}\r\n".format(kom)).encode())
        return self.lese_daten()



# Als Client
host = "pop.server.com"
port = 995
user = "username"
passwd = "password"

pop = POP3Telnet(host, port)
pop.kommando("USER {}".format(user))
pop.kommando("PASS {}".format(passwd))

# Send a telnet Command : For Example List the E-Mails on the POP Server
pop.kommando("LIST")

# Receive Response  from Telnet Device and decode it
print(pop.lese_daten().decode())

# Send a telnet Command : For Example quit the POP Server
pop.kommando("QUIT")
pop.close()