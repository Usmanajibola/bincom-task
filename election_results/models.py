from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class MyCharField(models.Field):
    def db_type(self, connection):
        return 'CHAR'

class Agent_Name(models.Model):
    name_id= models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default=None)
    phone = MyCharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField(validators=[MaxValueValidator(99999999999)])

    class Meta:
        db_table = 'agentname'

    def __str__(self):
        return self.name_id

class Announced_Lga_Results(models.Model):
    result_id = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    lga_name = models.CharField(max_length=50) 
    party_abbreviation = MyCharField(max_length=4) 
    party_score = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    entered_by_user = models.CharField(max_length=50) 
    date_entered = models.DateTimeField()
    user_ip_address =models.CharField(max_length=50)

    class Meta:
        db_table='announced_lga_results'
    def __str__(self):
        return self.result_id


class Announced_Pu_Results(models.Model):
    result_id=models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)]) 
    polling_unit_uniqueid=models.CharField(max_length=50) 
    party_abbreviation=MyCharField(max_length=4)
    party_score = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    entered_by_user = models.CharField(max_length=50) 
    date_entered = models.DateTimeField() 
    user_ip_address = models.CharField(max_length=50) 

    class Meta:
        db_table = 'announced_pu_results'
    def __str__(self):
        return self.party_abbreviation


class Announced_State_Results(models.Model):
    result_id = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)]) 
    state_name=models.CharField(max_length=50) 
    party_abbreviation = MyCharField(max_length=4)
    party_score = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    entered_by_user= models.CharField(max_length=50) 
    date_entered =models.DateTimeField() 
    user_ip_address = models.CharField(max_length=50) 

    class Meta:
        db_table = 'announced_state_results' 

    def __str__(self):
        return self.result_id


class Announced_Ward_Results(models.Model):
    result_id =  models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)]) 
    ward_name =models.CharField(max_length=50) 
    party_abbreviation = MyCharField(max_length=4)
    party_score = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    entered_by_user = models.CharField(max_length=50) 
    date_entered = models.DateTimeField() 
    user_ip_address = models.CharField(max_length=50) 

    class Meta:
        db_table = 'announced_ward_results'

    def __str__(self):
        return self.result_id


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)]) 
    lga_id =  models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    lga_name =  models.CharField(max_length=50) 
    state_id = models.IntegerField(validators=[MaxValueValidator(99999999999999999999999999999999999999999999999999)]) 
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50) 
    date_entered =  models.DateTimeField() 
    user_ip_address = models.CharField(max_length=50) 

    class Meta:
        db_table='lga'

    def __str__(self):
        return self.uniqueid

class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=50)

    class Meta:
        db_table = 'party'
    def __str__(self):
        return self.partyid

class Polling_Unit(models.Model):
    uniqueid =  models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)]) 
    polling_unit_id = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    ward_id =  models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    lga_id = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    uniquewardid = models.IntegerField(validators=[MaxValueValidator(99999999999)], default=None) 
    polling_unit_number = models.CharField(max_length=50, default=None)
    polling_unit_name = models.CharField(max_length=50, default=None)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255, default=None)
    long = models.CharField(max_length=255, default=None)
    entered_by_user = models.CharField(max_length=50, default=None)
    date_entered =  models.DateTimeField(default=None) 
    user_ip_address= models.CharField(max_length=50, default=None)

    class Meta:
        db_table = 'polling_unit'
    def __str__(self):
        return self.polling_unit_name


class States(models.Model):
    state_id = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)]) 
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table='states'

    def __str__(self):
        return self.state_id


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)]) 
    ward_id = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField(validators=[MaxValueValidator(99999999999)]) 
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField() 
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'ward'

    def __str__(self):
        return self.uniqueid