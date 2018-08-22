from flask import Flask,json,request,jsonify,session,Response

app = Flask(__name__)

@app.route('/batsignal',methods=['GET'])
def handle_bat_signal():

	#build response json variable
	response_var = {
		"response" : "Look behind you"
	}

	#add/modify properties of response variable
	response = jsonify(response_var)

	#return the response object
	return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0',port=3000)
