from CaesorMngr import Caesor 

c = Caesor()
c.change_input('I Enjoy being that stupid since I am so in love with my Dear Olga')
c.change_input(c.encrypt(23))
c.change_input(c.brute_force())
c.print()