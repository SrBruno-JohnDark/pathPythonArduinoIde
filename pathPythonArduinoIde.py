import os
import sys
import getpass
import subprocess

if sys.version_info.major < 3:
    print("Esse script está mudando o path do arduino de Python2.x para Python3.x, então use Python 3.x para me executar.")
    sys.exit(1)

output = subprocess.check_output(["ls", "/home/"+getpass.getuser()+"/.arduino15/packages/esp32/hardware/esp32/"])
outputStr = str(output.decode().replace('\n', ''))

output2 = subprocess.check_output(["python3", "--version"])
output2Str = str(output2.decode().replace('\n', ''))

print("Python 3.x [OK]")
print("Versão da biblioteca do ESP32: "+outputStr+" [OK]")
print("Versão do Python: "+output2Str+" [OK]")

# primeira parte

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('recipe.objcopy.bin.pattern.linux=python ', 'recipe.objcopy.bin.pattern.linux=python3 ')

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'w') as file:
    file.write(filedata)

# segunda parte 

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('tools.esptool_py.upload.pattern.linux=python ', 'tools.esptool_py.upload.pattern.linux=python3 ')

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'w') as file:
    file.write(filedata)

# terceira parte, aqui modifica as variáveis usadas pelo cmd(windows provavelmente)

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('tools.esptool_py.network_cmd=python ', 'tools.esptool_py.network_cmd=python3 ')

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'w') as file:
    file.write(filedata)

# quarta parte, aqui modifica as variáveis usadas pelo cmd(windows provavelmente) também

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('tools.gen_esp32part.cmd=python ', 'tools.gen_esp32part.cmd=python3 ')

with open('/home/'+getpass.getuser()+'/.arduino15/packages/esp32/hardware/esp32/'+outputStr+'/platform.txt', 'w') as file:
    file.write(filedata)

print("Python3 marcado como padrão na Arduino-IDE")

try:
    import serial
    print("Bibliotecas necessárias já estão instaladas. :)")
except ImportError:
    os.system("pip3 install pyserial")
    try:
        import serial
        print("Bibliotecas necessárias instaladas com sucesso. :)")
    except ImportError:
        print("Erro ao instalar bibliotecas necessárias. :(")