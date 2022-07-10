import json, datetime, os, keyboard, math, time;
from msvcrt import getch, kbhit;

def mostrarPacientes():
    os.system('cls');
    
    with open('pacientes.json') as f:
        datos = json.load(f);
        
        for paciente in datos["pacientes"]:
            fecha = datetime.datetime.strptime(paciente["fechaNacimiento"], "%d/%m/%Y");
            edad = math.floor((datetime.date.today() - fecha.date()).days / 365);
            
            print("ID:", str(paciente["id"]) + "\n" + \
                "Nombre:", paciente["nombre"], paciente["apellido"] + "\n" + \
                "DNI:", str(paciente["dni"]) + "\n" + \
                "Edad:", str(edad) + "\n" + \
                "Nacionalidad:", paciente["nacionalidad"] + "\n");
            
            if(len(paciente["historiaClinica"]) == 0):
                print("La/el paciente no tiene una historia clinica.\n");
            else:
                print("HISTORIA CLINICA:")
                for historia in paciente["historiaClinica"]:
                    print("Fecha:", historia["fecha"] + "\n" + \
                        "Enfermedad/Afeccion:", historia["padeceDe"] + "\n" + \
                        "Se atendio con:", historia["pacienteDe"] + "\n" + \
                        "Observaciones:", historia["observaciones"] + "\n");
            print("-----------------------------------------------------------------------------\n");

def registrarPaciente():
    while(True):
        os.system('cls');
        
        f = open('pacientes.json', 'r+');
        pacientes = json.load(f);
        pacienteID = len(pacientes["pacientes"]) + 1;
        
        tecla = "";
        
        datos = {
            "id": pacienteID,
            "dni": int(input("Ingrese el DNI del paciente (solo numeros): ")),
            "apellido": input("Ingrese el apellido del paciente: "),
            "nombre": input("Ingrese el nombre del paciente: "),
            "fechaNacimiento": input("Ingrese la fecha de nacimiento del paciente (DD/MM/AAAA): "),
            "nacionalidad": input("Ingrese la nacionalidad del paciente: "),
            "historiaClinica": []
        }
        
        os.system('cls');
        
        print("Confirme que los datos ingresados son correctos:" + "\n" + \
            "DNI:", str(datos["dni"]) + "\n" + \
            "Apellido:", datos["apellido"] + "\n" + \
            "Nombre:", datos["nombre"] + "\n" + \
            "Fecha de nacimiento:", datos["fechaNacimiento"] + "\n" + \
            "Nacionalidad:", datos["nacionalidad"]);
        print("\n1. Si     2. No     Esc. Cancelar")
        
        while(tecla not in ["1", "2", "esc"]):
            tecla = keyboard.read_key();
            time.sleep(0.2);
        
        while kbhit(): getch();
        if(tecla == "1"):
            pacientes["pacientes"].append(datos);
            f.seek(0);
            json.dump(pacientes, f, indent = 4);
            
            os.system('cls');
            print("Paciente registrado con exito.\n");
            
            tecla2 = "";
            print("Presione 1 para agregar otro paciente. Presione Escape para salir.")
            
            while(tecla2 not in ["1", "esc"]):
                tecla2 = keyboard.read_key();
                time.sleep(0.2);
            
            while kbhit(): getch();
            if(tecla2 == "1"):
                continue;
            if(tecla2 == "esc"):
                f.close();
                return;
            
        elif(tecla == "2"):
            continue;
        elif(tecla == "esc"):
            f.close();
            return;

def editarPaciente():
    f = open('pacientes.json', 'r+');
    pacientes = json.load(f);
    
    while(True):
        os.system('cls');
        pacienteID = 0;
        while(True):
            pacienteID = int(input("Ingrese el ID del paciente: "));
            
            if(pacienteID not in range(1, len(pacientes["pacientes"]) + 1)):
                print("El ID ingresado no existe.");
            else:
                break;
        
        while(True):
            print("Nombre:", pacientes["pacientes"][pacienteID-1]["nombre"] + "\n" + \
                "Apellido:", pacientes["pacientes"][pacienteID-1]["apellido"] + "\n" + \
                "DNI:", str(pacientes["pacientes"][pacienteID-1]["dni"]) + "\n" + \
                "Fecha de nacimiento:", pacientes["pacientes"][pacienteID-1]["fechaNacimiento"] + "\n" + \
                "Nacionalidad:", pacientes["pacientes"][pacienteID-1]["nacionalidad"] + "\n");
            
            print("Seleccione el campo a editar:\n" + \
            "1. Nombre    2. Apellido    3. DNI    4. Fecha de nacimiento    5. Nacionalidad    0. Seleccionar otro paciente    Esc. Cancelar\n")
            
            tecla = "";
            while(tecla not in ["1", "2", "3", "4", "5", "0", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);

            while kbhit(): getch();
            if(tecla == "1"):
                pacientes["pacientes"][pacienteID-1]["nombre"] = input("Ingrese un nombre: ");
            elif(tecla == "2"):
                pacientes["pacientes"][pacienteID-1]["apellido"] = input("Ingrese un apellido: ");
            elif(tecla == "3"):
                pacientes["pacientes"][pacienteID-1]["dni"] = int(input("Ingrese un DNI (solo números): "));
            elif(tecla == "4"):
                pacientes["pacientes"][pacienteID-1]["fechaNacimiento"] = input("Ingrese una fecha (DD/MM/AAAA): ");
            elif(tecla == "5"):
                pacientes["pacientes"][pacienteID-1]["nacionalidad"] = input("Ingrese una nacionalidad: ");
            elif(tecla == "0"):
                break;
            elif(tecla == "esc"):
                f.close();
                return;
            
            f.seek(0);
            json.dump(pacientes, f, indent=4);
            f.truncate();
            os.system('cls');
            print("Paciente editado con exito.\n");
            
            tecla = "";
            print("1. Editar otro dato del paciente    2. Editar datos de otro paciente    Esc. Volver al menu principal");
            while(tecla not in ["1", "2", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);
            
            os.system('cls');
            while kbhit(): getch();
            if(tecla == "1"):
                continue;
            if(tecla == "2"):
                break;
            if(tecla == "esc"):
                f.close();
                return;

def eliminarPaciente():
    f = open('pacientes.json', 'r+');
    pacientes = json.load(f);
    os.system('cls');
    
    while(True):
        pacienteID = 0;
        while(True):
            pacienteID = int(input("Ingrese el ID del paciente: "));
            
            if(pacienteID not in range(1, len(pacientes["pacientes"]) + 1)):
                print("El ID ingresado no existe.");
            else:
                break;
        
        while(True):
            print("Nombre:", pacientes["pacientes"][pacienteID-1]["nombre"] + "\n" + \
                "Apellido:", pacientes["pacientes"][pacienteID-1]["apellido"] + "\n" + \
                "DNI:", str(pacientes["pacientes"][pacienteID-1]["dni"]) + "\n" + \
                "Fecha de nacimiento:", pacientes["pacientes"][pacienteID-1]["fechaNacimiento"] + "\n" + \
                "Nacionalidad:", pacientes["pacientes"][pacienteID-1]["nacionalidad"] + "\n");
            
            print("Confirme que quiere eliminar este paciente:\n" + \
            "1. Si    2. No    Esc. Cancelar");
            
            tecla = "";
            while(tecla not in ["1", "2", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);

            while kbhit(): getch();
            if(tecla == "1"):
                pacientes["pacientes"].pop(pacienteID-1);
            elif(tecla == "2"):
                os.system('cls');
                break;
            elif(tecla == "esc"):
                f.close();
                return;
            
            f.seek(0);
            json.dump(pacientes, f, indent=4);
            f.truncate();
            asignarIds("pacientes.json");
            
            os.system('cls');
            print("Paciente eliminado con exito.\n");
            
            tecla = "";
            print("1. Eliminar otro paciente    Esc. Volver al menu principal");
            
            while(tecla not in ["1", "2", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);
            
            while kbhit(): getch();
            if(tecla == "1"):
                os.system('cls');
                break;
            if(tecla == "esc"):
                f.close();
                return;

def asignarIds(archivo):
    categoria = archivo.split(".")[0];
    with open(archivo, 'r+') as f:
        datos = json.load(f);
        
        i = 1;        
        for registro in datos[categoria]:
            registro["id"] = i;
            i += 1;

        f.seek(0);
        json.dump(datos, f, indent=4);
        f.truncate();

def registrarHistoriaClinica():
    f = open('pacientes.json', 'r+');
    pacientes = json.load(f);
    
    while(True):
        os.system('cls');
        pacienteID = 0;
        while(True):
            pacienteID = int(input("Ingrese el ID del paciente: "));
            
            if(pacienteID not in range(1, len(pacientes["pacientes"]) + 1)):
                print("El ID ingresado no existe.");
            else:
                break;
        
        while(True):
            os.system("cls");
            
            print("Nombre:", pacientes["pacientes"][pacienteID-1]["nombre"] + "\n" + \
                "Apellido:", pacientes["pacientes"][pacienteID-1]["apellido"] + "\n" + \
                "DNI:", str(pacientes["pacientes"][pacienteID-1]["dni"]) + "\n" + \
                "Fecha de nacimiento:", pacientes["pacientes"][pacienteID-1]["fechaNacimiento"] + "\n" + \
                "Nacionalidad:", pacientes["pacientes"][pacienteID-1]["nacionalidad"] + "\n");
            
            if(len(pacientes["pacientes"][pacienteID-1]["historiaClinica"]) == 0):
                print("La/el paciente no tiene una historia clinica.\n");
            else:
                print("HISTORIA CLINICA:")
                for historia in pacientes["pacientes"][pacienteID-1]["historiaClinica"]:
                    print("Fecha:", historia["fecha"] + "\n" + \
                        "Enfermedad/Afeccion:", historia["padeceDe"] + "\n" + \
                        "Se atendio con:", historia["pacienteDe"] + "\n" + \
                        "Observaciones:", historia["observaciones"] + "\n");
            
            print("Confirme que desea agregar una historia clinica a este paciente:\n" + \
            "1. Si    2. No    Esc. Cancelar")
            
            tecla = "";
            while(tecla not in ["1", "2", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);

            while kbhit(): getch();
            if(tecla == "1"):
                while(True):
                    datos = {
                        "fecha": input("Fecha de la consulta (DD/MM/AAAA): "),
                        "padeceDe": input("Afeccion del paciente: "),
                        "pacienteDe": input("Paciente de: "),
                        "observaciones": input("Observaciones: ")
                    }
                    
                    os.system('cls');
            
                    print("Confirme que los datos ingresados son correctos:" + "\n" + \
                    "Fecha:", datos["fecha"] + "\n" + \
                    "Afeccion:", datos["padeceDe"] + "\n" + \
                    "Paciente de:", datos["pacienteDe"] + "\n" + \
                    "Observaciones:", datos["observaciones"]);
                    
                    print("\n1. Si     2. No     Esc. Cancelar")
                    
                    tecla2 = "";
                    while(tecla2 not in ["1", "2", "esc"]):
                        tecla2 = keyboard.read_key();
                        time.sleep(0.2);
                    
                    while kbhit(): getch();
                    if(tecla2 == "1"):
                        pacientes["pacientes"][pacienteID-1]["historiaClinica"].append(datos);
                        f.seek(0);
                        json.dump(pacientes, f, indent = 4);
                        f.truncate();
                        
                        os.system('cls');
                        print("Historia clinica registrada con exito.\n");
                        break;
                    elif(tecla2 == "2"):
                        os.system("cls");
                    elif(tecla2 == "esc"):
                        f.close();
                        return;
                
            elif(tecla == "2"):
                break;
            elif(tecla == "esc"):
                f.close();
                return;
            
            tecla = "";
            print("1. Agregar otra historia al paciente    2. Agregar una historia a otro paciente    Esc. Volver al menu principal");
            while(tecla not in ["1", "2", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);
            
            while kbhit(): getch();
            if(tecla == "1"):
                continue;
            if(tecla == "2"):
                break;
            if(tecla == "esc"):
                f.close();
                return;

def mostrarProfesionales():
    os.system('cls');
    
    with open('profesionales.json') as f:
        datos = json.load(f);
        
        for profesional in datos["profesionales"]:
            print("ID:", str(profesional["id"]) + "\n" + \
                "Nombre:", profesional["nombre"], profesional["apellido"] + "\n" + \
                "Especialidad:", profesional["especialidad"] + "\n");
            print("-----------------------------------------------------------------------------\n");

def registrarProfesional():
    while(True):
        os.system('cls');
        
        f = open('profesionales.json', 'r+');
        profesionales = json.load(f);
        profesionalID = len(profesionales["profesionales"]) + 1;
        
        tecla = "";
        
        datos = {
            "id": profesionalID,
            "apellido": input("Ingrese el apellido del profesional: "),
            "nombre": input("Ingrese el nombre del profesional: "),
            "especialidad": input("Ingrese la especialidad del profesional: "),
        }
        
        os.system('cls');
        
        print("Confirme que los datos ingresados son correctos:" + "\n" + \
            "Apellido:", datos["apellido"] + "\n" + \
            "Nombre:", datos["nombre"] + "\n" + \
            "Especialidad:", datos["especialidad"]);
        print("\n1. Si     2. No     Esc. Cancelar")
        
        while(tecla not in ["1", "2", "esc"]):
            tecla = keyboard.read_key();
            time.sleep(0.2);
        
        while kbhit(): getch();
        if(tecla == "1"):
            profesionales["profesionales"].append(datos);
            f.seek(0);
            json.dump(profesionales, f, indent = 4);
            
            os.system('cls');
            print("Profesional registrado con exito.\n");
            
            tecla2 = "";
            print("Presione 1 para agregar otro profesional. Presione Escape para salir.")
            
            while(tecla2 not in ["1", "esc"]):
                tecla2 = keyboard.read_key();
                time.sleep(0.2);
            
            while kbhit(): getch();
            if(tecla2 == "1"):
                continue;
            if(tecla2 == "esc"):
                f.close();
                return;
            
        elif(tecla == "2"):
            continue;
        elif(tecla == "esc"):
            f.close();
            return;

def eliminarProfesional():
    f = open('profesionales.json', 'r+');
    profesionales = json.load(f);
    os.system('cls');
    
    while(True):
        profesionalID = 0;
        while(True):
            profesionalID = int(input("Ingrese el ID del profesional: "));
            
            if(profesionalID not in range(1, len(profesionales["profesionales"]) + 1)):
                print("El ID ingresado no existe.");
            else:
                break;
        
        while(True):
            print("Nombre:", profesionales["profesionales"][profesionalID-1]["nombre"] + "\n" + \
                "Apellido:", profesionales["profesionales"][profesionalID-1]["apellido"] + "\n" + \
                "Especialidad:", profesionales["profesionales"][profesionalID-1]["especialidad"] + "\n");
            
            print("Confirme que quiere eliminar este profesional:\n" + \
            "1. Si    2. No    Esc. Cancelar");
            
            tecla = "";
            while(tecla not in ["1", "2", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);

            while kbhit(): getch();
            if(tecla == "1"):
                profesionales["profesionales"].pop(profesionalID-1);
            elif(tecla == "2"):
                os.system('cls');
                break;
            elif(tecla == "esc"):
                f.close();
                return;
            
            f.seek(0);
            json.dump(profesionales, f, indent=4);
            f.truncate();
            asignarIds("profesionales.json");
            
            os.system('cls');
            print("Profesional eliminado con exito.\n");
            
            tecla = "";
            print("1. Eliminar otro profesional    Esc. Volver al menu principal");
            
            while(tecla not in ["1", "2", "esc"]):
                tecla = keyboard.read_key();
                time.sleep(0.2);
            
            while kbhit(): getch();
            if(tecla == "1"):
                os.system('cls');8
                break;
            if(tecla == "esc"):
                f.close();
                return;

def buscarPaciente():
    f = open('pacientes.json', 'r+');
    pacientes = json.load(f);
    os.system('cls');
    
    while(True):
        print("Seleccione un criterio de busqueda:\n" + \
            "1. Apellido\n"  + \
            "2. Nacionalidad\n" + \
            "3. Rango de fechas de historia clinica\n" + \
            "4. Afeccion\n" + \
            "5. Profesional con quien se trato\n" + \
            "Esc. Cancelar");
    
        tecla = "";
        while(tecla not in ["1", "2", "3", "4", "5", "6", "esc"]):
            tecla = keyboard.read_key();
            time.sleep(0.2);

        while kbhit(): getch();
        os.system('cls');
        
        valor = "";
        criterio = "";
        if(tecla == "1"):
            criterio = "apellido";
            valor = input("Ingrese el apellido del paciente: ");
        elif(tecla == "2"):
            criterio = "nacionalidad";
            valor = input("Ingrese la nacionalidad del paciente: ");
        elif(tecla == "3"):
            criterio = "fecha";
            valor = [input("Ingrese una fecha (DD/MM/AAAA): "), \
                    input("Ingrese otra fecha (DD/MM/AAAA): ")];
        elif(tecla == "4"):
            criterio = "padeceDe";
            valor = input("Ingrese la afeccion del paciente: ");
        elif(tecla == "5"):
            criterio = "pacienteDe";
            valor = input("Ingrese el nombre del profesional: ");
        elif(tecla == "esc"):
            f.close();
            return;

        os.system('cls');
        i = 0;
        
        if tecla in ["1", "2"]:
            for paciente in pacientes["pacientes"]:
                if(valor.lower() in paciente[criterio].lower()):
                    # Estoy repitiendo este código (mala práctica)
                    fecha = datetime.datetime.strptime(paciente["fechaNacimiento"], "%d/%m/%Y");
                    edad = math.floor((datetime.date.today() - fecha.date()).days / 365);
                    
                    print("ID:", str(paciente["id"]) + "\n" + \
                        "Nombre:", paciente["nombre"], paciente["apellido"] + "\n" + \
                        "DNI:", str(paciente["dni"]) + "\n" + \
                        "Edad:", str(edad) + "\n" + \
                        "Nacionalidad:", paciente["nacionalidad"] + "\n");
                    
                    if(len(paciente["historiaClinica"]) == 0):
                        print("La/el paciente no tiene una historia clinica.\n");
                    else:
                        print("HISTORIA CLINICA:")
                        for historia in paciente["historiaClinica"]:
                            print("Fecha:", historia["fecha"] + "\n" + \
                                "Enfermedad/Afeccion:", historia["padeceDe"] + "\n" + \
                                "Se atendio con:", historia["pacienteDe"] + "\n" + \
                                "Observaciones:", historia["observaciones"] + "\n");
                    print("-----------------------------------------------------------------------------\n");
                    i += 1;
        elif tecla in ["4", "5"]:
            for paciente in pacientes["pacientes"]:
                pacienteID = 0;
                for historia in paciente["historiaClinica"]:
                    if(valor.lower() in historia[criterio].lower()):
                        # Estoy repitiendo este código (mala práctica)
                        if(pacienteID != paciente["id"]):
                            fecha = datetime.datetime.strptime(paciente["fechaNacimiento"], "%d/%m/%Y");
                            edad = math.floor((datetime.date.today() - fecha.date()).days / 365);
                        
                            print("ID:", str(paciente["id"]) + "\n" + \
                                "Nombre:", paciente["nombre"], paciente["apellido"] + "\n" + \
                                "DNI:", str(paciente["dni"]) + "\n" + \
                                "Edad:", str(edad) + "\n" + \
                                "Nacionalidad:", paciente["nacionalidad"] + "\n");
                            print("HISTORIA CLINICA:")
                        
                        pacienteID = paciente["id"];
                        
                        print("Fecha:", historia["fecha"] + "\n" + \
                            "Enfermedad/Afeccion:", historia["padeceDe"] + "\n" + \
                            "Se atendio con:", historia["pacienteDe"] + "\n" + \
                            "Observaciones:", historia["observaciones"] + "\n");
                        i += 1;
                if(pacienteID == paciente["id"]):
                    print("-----------------------------------------------------------------------------\n");
        else:
            primerFecha = datetime.datetime.strptime(valor[0], "%d/%m/%Y");
            segundaFecha = datetime.datetime.strptime(valor[1], "%d/%m/%Y");
            for paciente in pacientes["pacientes"]:
                pacienteID = 0;
                for historia in paciente["historiaClinica"]:
                    fechaDeConsulta = datetime.datetime.strptime(historia[criterio], "%d/%m/%Y");
                    if((fechaDeConsulta >= primerFecha) and (fechaDeConsulta <= segundaFecha)):
                        # Estoy repitiendo este código (mala práctica)
                        if(pacienteID != paciente["id"]):
                            fecha = datetime.datetime.strptime(paciente["fechaNacimiento"], "%d/%m/%Y");
                            edad = math.floor((datetime.date.today() - fecha.date()).days / 365);
                            
                            print("ID:", str(paciente["id"]) + "\n" + \
                                "Nombre:", paciente["nombre"], paciente["apellido"] + "\n" + \
                                "DNI:", str(paciente["dni"]) + "\n" + \
                                "Edad:", str(edad) + "\n" + \
                                "Nacionalidad:", paciente["nacionalidad"] + "\n");
                            print("HISTORIA CLINICA:")
                        
                        pacienteID = paciente["id"];
                        
                        print("Fecha:", historia["fecha"] + "\n" + \
                            "Enfermedad/Afeccion:", historia["padeceDe"] + "\n" + \
                            "Se atendio con:", historia["pacienteDe"] + "\n" + \
                            "Observaciones:", historia["observaciones"] + "\n");
                        i += 1;
                if(pacienteID == paciente["id"]):
                    print("-----------------------------------------------------------------------------\n");
            
        if(i > 0):
            print("Se han encontrado", str(i), "registros que coinciden con su criterio de busqueda.");
        else:
            print("No se han encontrado registros que coincidan con su criterio de busqueda.");
        
        tecla = "";
        print("\n1. Buscar de nuevo    Esc. Volver al menu principal");
            
        while(tecla not in ["1", "esc"]):
            tecla = keyboard.read_key();
            time.sleep(0.2);
        
        while kbhit(): getch();
        if(tecla == "1"):
            os.system('cls');
        if(tecla == "esc"):
            f.close();
            return;
        
while(True):
    print("MENU PRINCIPAL\n");
    
    print("Presione una tecla:\n\
    1. Mostrar lista de pacientes\n\
    2. Registrar un nuevo paciente\n\
    3. Editar datos de un paciente\n\
    4. Eliminar un paciente\n\
    5. Agregar una historia clinica a un paciente\n\
    6. Mostrar lista de profesionales\n\
    7. Registrar un nuevo profesional\n\
    8. Eliminar un profesional\n\
    9. Buscar un paciente\n\
    Esc. Salir");
    
    tecla = "";
    while(tecla not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "esc"]):
        tecla = keyboard.read_key();
        time.sleep(0.2);
    
    while kbhit(): getch();
    if(tecla == "1"):
        mostrarPacientes();
        print("\nPresione Escape para volver al menu principal.");
        tecla2 = "";
        while(tecla2 != "esc"):
            tecla2 = keyboard.read_key();
            time.sleep(0.2);
    elif(tecla == "2"):
        registrarPaciente()
    elif(tecla == "3"):
        editarPaciente();
    elif(tecla == "4"):
        eliminarPaciente();
    elif(tecla == "5"):
        registrarHistoriaClinica();
    elif(tecla == "6"):
        mostrarProfesionales();
        print("\nPresione Escape para volver al menu principal.");
        tecla2 = "";
        while(tecla2 != "esc"):
            tecla2 = keyboard.read_key();
            time.sleep(0.2);
    elif(tecla == "7"):
        registrarProfesional();
    elif(tecla == "8"):
        eliminarProfesional();
    elif(tecla == "9"):
        buscarPaciente();
    elif(tecla == "esc"):
        exit();
        
    os.system("cls");
    while kbhit(): getch();