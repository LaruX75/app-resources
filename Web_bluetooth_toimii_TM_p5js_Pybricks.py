from pybricks.hubs import InventorHub
from pybricks.parameters import Color, Icon, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from usys import stdin
from uselect import poll

hub = InventorHub()

# ALUSTA MOOTTORI (Uusi lisäys)
# Varmista että moottori on kytketty porttiin A
motor_a = Motor(Port.A)

# Skrollaa teksti käynnistyessä
hub.display.text("READY")

hub.light.on(Color.CYAN)

poller = poll()
poller.register(stdin)

# Omat kuvat (5x5 matriisi, 0-100 kirkkaus)
IHMINEN = [
    [0, 0, 100, 0, 0],
    [0, 100, 100, 100, 0],
    [100, 0, 100, 0, 100],
    [0, 0, 100, 0, 0],
    [0, 100, 0, 100, 0],
]

KISSA = [
    [100, 0, 0, 0, 100],
    [100, 100, 0, 100, 100],
    [0, 100, 0, 100, 0],
    [0, 100, 100, 100, 0],
    [0, 100, 0, 100, 0],
]

KOIRA = [
    [100, 100, 0, 0, 0],
    [100, 100, 100, 100, 0],
    [0, 100, 0, 100, 0],
    [0, 100, 100, 100, 100],
    [0, 100, 0, 100, 0],
]

while True:
    events = poller.poll(100)
    
    if events:
        c = stdin.read(1)
        
        if c in ['\n', '\r', '', None]:
            continue
        
        hub.light.on(Color.WHITE)
        wait(100)
        
        if c == '1':
            hub.light.on(Color.GREEN)
            hub.display.icon(IHMINEN)
            
        elif c == '2':
            hub.light.on(Color.YELLOW)
            hub.display.icon(KISSA)
            
        elif c == '3':
            hub.light.on(Color.RED)
            hub.display.icon(KOIRA)
            
            # --- MOOTTORIN LIIKE ---
            # Nopeus 500 astetta/sek (positiivinen = myötäpäivään)
            # Aika 2000 ms (2 sekuntia)
            motor_a.run_time(500, 2000)
            
        else:
            hub.light.on(Color.MAGENTA)
            hub.display.text("?")
        
        wait(500)
        hub.light.on(Color.CYAN)
        hub.display.icon(Icon.HEART)
    
    if hub.buttons.pressed():
        hub.light.off()
        hub.display.off()
        break