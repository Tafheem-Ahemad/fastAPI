
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

	name: str
	weight:float
	email:EmailStr
	Instagram_ID:AnyUrl
	location:Dict[str,str]

	@field_validator('email')
	@classmethod
	def check_email(cls,value):
		
		company_name=value.split("@")[-1];

		if(company_name == "google.com"):
			return value
		raise ValueError("not working in Google")



def insert_into_value(patient : Patient):

	print(patient.name)
	print(patient.weight)

patient1_info={
	'name':"Tafheem Ahemad",
	'weight':52.22,	
	"email":"abc@google.com",
	"Instagram_ID":"https://www.linkedin.com/in",
	"location":{'state':'odisha','pin':"000000"}
}

patient1=Patient(**patient1_info)

insert_into_value(patient1)