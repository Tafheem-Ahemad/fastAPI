from fastapi import FastAPI,HTTPException,Path,Query
import json

app=FastAPI()

def load_data():
	with open("data.json","r") as f:
		data=json.load(f)

	return data

@app.get("/")
def home():
	return {'name':"Tafheem Ahemad"}

@app.get("/about")
def about():
	return {"CF Profile" : "Kalix1110"}

@app.get("/patients")
def patients():
	return load_data()


# fastAPI doesnot allow same name of route
@app.get("/patients/sort")
def patients_by_sort(sort_by:str=Query(...,description="sort the balue based on height ,weight"),order: str = Query('asc', description='sort in asc or desc order')):
	data=load_data()

	valid_fields = ['height', 'weight', 'bmi']
	order_field=["asc","dec"]

	print(data)

	if(sort_by not in valid_fields):
		raise HTTPException(status_code=404,detail="not in the {valid_fields}")
	
	if(order not in order_field):
		raise HTTPException(status_code=404,detail="not in the {order_field}")
	
	sort_order = True if order=='dec' else False

	sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

	return sorted_data


@app.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(...,description="Give a valid patient Id",example="P001")):
	data=load_data()

	if (patient_id in data):
		return data[patient_id]
	else: 
		raise HTTPException(status_code=404,detail="Not get value")