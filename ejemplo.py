cursos = {"python": ["Jose", "Javier"], "html": ["Lorena", "Jose"] } 

def por_alumno(cursos):
  resultado = {}
  for key in cursos.keys():
    for alumno in cursos[key]:
        resultado[alumno].append(key)
      
      

  return resultado

resul = por_alumno(cursos)
print(resul)