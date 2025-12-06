from django.db import models

# Create your models here.
class Agenda(models.Model):
    idagenda = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    medico = models.ForeignKey('medicos.Medico', on_delete=models.CASCADE)
    data_consulta = models.DateField()
    hora_consulta = models.TimeField()
    motivo = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta {self.idagenda} - {self.cliente.nome} com {self.medico.nome} em {self.data_consulta} às {self.hora_consulta}"