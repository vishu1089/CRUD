from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)
@app.route("/",methods=['GET'])
def query_records():
	name = request.args.get('name')
	print(name)
	with open('data.json','r') as f:
		data = f.read()
		print(data)
		records = json.loads(data)
		print(type(records))
		for rec in records:
			print(rec)
			if (rec["name"]==name):
				return jsonify(rec)

	return jsonify({"error":"data not found"})


@app.route("/",methods=['POST'])
def first():
	rec = json.loads(request.data)
	with open('data.json','r') as f:
		data = f.read()
	if not data:
		records = [rec]
	else:
		records=json.loads(data)
		records.append(rec)
	with open('data.json','w') as f:
		f.write(json.dumps(records,indent=3))
	return jsonify(rec)

@app.route("/",methods=['PUT'])
def put_req():
	rec = json.loads(request.data)
	name = rec[0]["name"]
	email = rec[0]["email"]
	print(rec[0]["name"])
	new_record = []
	with open('data.json','r') as f:
		data = f.read()
		records = json.loads(data)
	for r in records:
		if(r['name']==name):
			r['email']=email
			# r["email"]=email
	return jsonify(records)


@app.route("/",methods=['DELETE'])
def delete():
	new_record=""
	with open("data.json","w") as f:
		f.write(new_record)
	return jsonify({"message":"deleted the complete data"})
app.run(debug=True)





