# Corrigindo problemas ESP32/Arduino-IDE/Python
Um script simples para corrigir erros ao executar a ide do arduino no linux onde se utiliza a placa ESP32.

Ao utilizar a biblioteca do ESP32 na IDE Arduino para distribuições linux, me deparei com um erro
que já deveria ter sido previsto, que foi a utilização do programa python, quando a IDE tenta
executar um arquivo .py, por padrão dentro da IDE é usado o comando "python", porém isso deve ser verificado
antes de executar qualquer tipo de script .py, pois em muitas distribuições linux se usa o
comando "python3" por padrão.

É um erro pequeno, mas impossibilita o uso da IDE por parte de uma pessoa iniciante.
Dito isto, este script corrige o caminho da linguagem python dentro da biblioteca do ESP32,
para ser mais especfico, no arquivo <b>platform.txt</b>

>Antigo:
>```
>recipe.objcopy.bin.pattern.linux=python 🔴
>```
>Novo:
>```
>recipe.objcopy.bin.pattern.linux=python3 🟢
>```

*segunda parte*

>Antigo:
>```
>tools.esptool_py.upload.pattern.linux=python 🔴
>```
>Novo:
>```
>tools.esptool_py.upload.pattern.linux=python3 🟢
>```

*Terceira parte*

E por fim instala uma biblioteca para se comunicar com a placa corretamente:
>```
>pip3 install pyserial
>```


# Modo de uso:
> - Baixe o script "pathPythonArduinoIde.py"<br>
> - Execute ele com o seguinte comando no terminal:
>```
>python3 pathPythonArduinoIde.py
>```

O único requisito para executar este script é ter instalado o <b>Python3</b>

```
Este script é de código aberto, livre para copiar e modificar, use como quiser, conhecimento é poder.
This script is open source, free to copy and modify, use however you like, knowledge is power.
