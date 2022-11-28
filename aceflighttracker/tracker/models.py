# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Flight(models.Model):
    flightid = models.AutoField(db_column='FlightId', primary_key=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    days = models.IntegerField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    flightnum = models.IntegerField(db_column='FlightNum', blank=True, null=True)  # Field name made lowercase.
    aircraftid = models.TextField(db_column='AircraftId', blank=True, null=True)  # Field name made lowercase.
    from_field = models.TextField(db_column='From', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.TextField(db_column='To', blank=True, null=True)  # Field name made lowercase.
    out = models.IntegerField(db_column='Out', blank=True, null=True)  # Field name made lowercase.
    off = models.IntegerField(db_column='Off', blank=True, null=True)  # Field name made lowercase.
    on = models.IntegerField(db_column='On', blank=True, null=True)  # Field name made lowercase.
    in_field = models.IntegerField(db_column='In', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    night = models.FloatField(db_column='Night', blank=True, null=True)  # Field name made lowercase.
    imc = models.FloatField(db_column='IMC', blank=True, null=True)  # Field name made lowercase.
    pilotflying = models.IntegerField(db_column='PilotFlying', blank=True, null=True)  # Field name made lowercase.
    approachtype = models.TextField(db_column='ApproachType', blank=True, null=True)  # Field name made lowercase.
    dayt_o = models.IntegerField(db_column='DayT/O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dayldg = models.IntegerField(db_column='DayLdg', blank=True, null=True)  # Field name made lowercase.
    nightt_o = models.IntegerField(db_column='NightT/O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nightldg = models.IntegerField(db_column='NightLdg', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Flight'
    
    def __str__(self):
        return "{}-{}".format(self.flightid, self.date, self.days, self.flightnum, self.aircraftid,
        self.from_field, self.to, self.out, self.off, self.on, self.in_field, self.total, 
        self.night, self.imc, self.pilotflying, self.approachtype, self.dayt_o, self.dayldg, self.nightt_o, self.nightldg,
        self.remarks)
