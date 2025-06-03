
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

	name: Annotated[str,Field(min_length=1,max_length=20,title="Name of the patient", description="Name of the user",example="Kalix")]
	age:int = Field(gt=0,le=120)
	weight:Annotated[float,Field(default=0,strict=True)]
	email:EmailStr
	Instagram_ID:AnyUrl
	weakness:Annotated[Optional[List[str]],Field(max_length=5)]
	location:Dict[str,str]

def insert_into_value(patient : Patient):

	print(patient.name)
	print(patient.age)

patient1_info={
	'name':"Tafheem Ahemad",
	'age':20,
	'weight':52.22,	
	"email":"abc@gmail.com",
	"Instagram_ID":"https://www.linkedin.com/in",
	'weakness':["eye","nose","teeth"],
	"location":{'state':'odisha','pin':"000000"}
}

patient1=Patient(**patient1_info)

insert_into_value(patient1)