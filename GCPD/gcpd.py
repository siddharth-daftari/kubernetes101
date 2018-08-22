from flask import Flask,json,request,jsonify,session,Response
import requests

app = Flask(__name__)

@app.route('/call-batman',methods=['GET'])
def handle_call_to_batman():

	call_batman_url = "http://batcave:3000/batsignal"
	call_batman_response = requests.get(url = URL)
	call_batman_response_json = call_batman_response.json()

	#add/modify properties of response variable
	response = jsonify(call_batman_response_json)

	#return the response object
	return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0',port=3001)
