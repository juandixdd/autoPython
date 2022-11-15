import os

execute = True

# ? C for close cmd and k for not close cmd

edenSoft = 'cmd /c "j: && cd J:\Education\Sena\EdenSoft\Front\eden_soft_angular_v5.0 && code . && cd .. && cd .. && cd Back && cd node_jsedenSoft_backEnd && code . && cd.. && cd.. && cd.. && cd.. && cd.. && d: && cd D:\Programs\DBeaver && start dbeaver.exe"'
finno = 'cmd /c "d: && cd programacion && cd projects && cd finno && cd front && cd Angular_plantilla_inicial_vuexy && code . && cd.. && cd.. && cd finno_back && code . && cd D:\Programs\DBeaver && start dbeaver.exe"'


def cmdCommand(command):
    os.system(command)


while(execute):
    print("Por favor ingrese la opcion del proyecto que desea ejecutar.")
    print("1. EdenSoft")
    print("2. Finno")

    value = input("Opcion: ")

    if(value == "1"):
        print("1. EdenSoft")
        cmdCommand(edenSoft)
        execute = False
    elif(value == "2"):
        print("2. Finno")
        cmdCommand(finno)
        execute = False
    else:
        print("Por favor ingrese un valor valido")
        execute = True
