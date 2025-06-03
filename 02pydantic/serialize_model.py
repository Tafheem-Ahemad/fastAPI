
from pydantic import BaseModel,EmailStr,AnyUrl,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

	name: str
	weight:float
	age:int
	email:EmailStr
	Instagram_ID:AnyUrl
	location:Dict[str,str]


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

patient1_info_dic=patient1.model_dump()
print(patient1_info_dic)
print(type(patient1_info_dic))

patient1_info_json=patient1.model_dump_json()
print(patient1_info_json)
print(type(patient1_info_json))

# some property like include,exlude can be used