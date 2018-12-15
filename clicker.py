from actions import typer, press, click, set_cursor
from time import sleep
#from lang import getKeyboardLayout

#TODO check §(тильда Ё)
sleep(5)
click(41, 106)
typer('Hello from there')
press('tab')
typer('and there')
press('tab')
typer('asdfghjkl')
press('tab')
typer('`zxcvbnm,./`')
press('tab')
typer('21.22.2000')
press('tab')
typer('23.21.11')
press('tab')
typer('ALLO')
press('tab')
typer('OLOLO')
press('tab')
typer('DJIGURDA-6677.123ss')
set_cursor(61, 412)
sleep(0.5)
click(62, 505)

print('Done!')

