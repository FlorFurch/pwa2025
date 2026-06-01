from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=128, null=False)
    apellido = models.CharField(max_length=128, null=False)
    mostrar = models.CharField(max_length=256, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=128, null=False)
    cant_alumnos = models.IntegerField(default=5)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.id_carrera.nombre} - {self.id_profesor.nombre} {self.id_profesor.apellido}"

class Aula(models.Model):
    descripcion = models.CharField(max_length=128, null=False)
    ubicacion = models.CharField(max_length=128, null=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descripcion} - {self.ubicacion} - Proyectores: {self.cant_proyector} - Aforo: {self.aforo} - Climatizada: {'Sí' if self.es_climatizada else 'No'}"
    
class ReservaAula(models.Model):
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observacion = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.id_aula.descripcion} - {self.fh_desde} to {self.fh_hasta}"
    
class HorarioMateria(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(ReservaAula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    
    def __str__(self):
        return f"{self.id_materia.nombre} - {self.fh_desde} to {self.fh_hasta}"