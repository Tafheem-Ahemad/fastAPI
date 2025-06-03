
from pydantic import BaseModel,EmailStr,AnyUrl,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

	name: str
	weight:float
	age:int
	email:EmailStr
	Instagram_ID:AnyUrl
	location:Dict[str,str]

	# We must specify "mode"  in this code
	@model_validator(mode='after')
	def check_email(cls,model):
		
		if model.age >50 and model.weight > 80:
			raise ValueError("Over weight")
			
		return model


def insert_into_value(patient : Patient):

	print(patient.name)
	print(patient.age)
	print(patient.weight)

patient1_info={
	'name':"Tafheem Ahemad",
	'age':51,
	'weight':52.22,	
	"email":"abc@google.com",
	"Instagram_ID":"https://www.linkedin.com/in",
	"location":{'state':'odisha','pin':"000000"}
}

patient1=Patient(**patient1_info)

insert_into_value(patient1)