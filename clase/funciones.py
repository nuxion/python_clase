

def filtrar_x_edad(cursos, edad):
  res = {}
  for alumnos in cursos.values():
    for alu in alumnos:
      if alu['edad'] > edad:
        dni = alu["dni"]
        res[dni] = alu 
  return res


def por_alumno(cursos):
    resultado = {}
    for key in cursos.keys():
        for alumno in cursos[key]:
            alus = resultado.get(alumno, [])
            alus.append(key)
            resultado[alumno] = alus
    return resultado


def alumnos_por_curso(cursos, nombre):
    """ Obtiene los alumnos por curso,
    recibe un diccionario
    
    """
    resultado = cursos.get(nombre)
    if resultado is not None:
        return resultado
    else:
        return []

