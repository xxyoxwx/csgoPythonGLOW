from html import entities
from pymem import Pymem
import pymem.process
import keyboard

dwEntityList = 0x4DFFF04
m_iTeamNum = 0xF4
m_iGlowIndex = 0x10488
dwLocalPlayer = 0xDEA964
dwGlowObjectManager = 0x535A9D8

def main():
    mem = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(mem.process_handle,"client.dll").lpBaseOfDll


    while True:
        if keyboard.is_pressed('end'):
            exit(0)

        glow_manager = mem.read_int(client + dwGlowObjectManager)
        for i in range(1,32):
            entity = mem.read_int(client + dwEntityList + i * 0x10)

            if entity:
                ent_team_id = mem.read_int(entity + m_iTeamNum)
                ent_glow = mem.read_int(entity + m_iGlowIndex)

                if ent_team_id == 2: 
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0x8,float(1)) #R
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0xC,float(0)) #G
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0x10,float(0)) #B
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0x14,float(1)) # ALPHA
                    mem.write_int(glow_manager + ent_glow * 0x38 + 0x28, 1) #ON
                elif ent_team_id == 3: 
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0x8,float(0))
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0xC,float(0)) 
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0x10,float(1)) 
                    mem.write_float(glow_manager + ent_glow * 0x38 + 0x14,float(1))
                    mem.write_int(glow_manager + ent_glow * 0x38 + 0x28, 1)
if __name__ == '__main__':
    main()