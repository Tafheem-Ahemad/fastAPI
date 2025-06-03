
from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict


# here use some inbulid paydantic models like EmailStr,AnyUrl,AnyHttpUrl
# use List and Dict for strong typing

class Patient(BaseModel):

	name:str
	age:int
	weight:float
	email:EmailStr
	Instagram_ID:AnyUrl
	weakness:List[str]
	location:Dict[str,str]

def insert_into_value(patient : Patient):

	print(patient.name)
	print(patient.age)

patient1_info={
	'name':"Tafheem Ahemad",
	'age':20,
	'weight':30,
	"email":"abc@gmail.com",
	"Instagram_ID":"https://www.linkedin.com/in",
	'weakness':["eye","nose","teeth"],
	"location":{'state':'odisha','pin':"000000"}
}

patient1=Patient(**patient1_info)

insert_into_value(patient1)