from flask import Flask,json,request,jsonify,session,Response

app = Flask(__name__)

@app.route('/call-batman',methods=['GET'])
def handle_call_to_batman():

	#build response json variable
	responseVar = {
		"response" : "He's on the way"
	}

	#add/modify properties of response variable
	response = jsonify(responseVar)

	#return the response object
	return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0',port=3001)
