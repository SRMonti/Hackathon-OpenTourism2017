from flask import Flask
from flask import render_template
from flask import request
import model as dbHandler
import json
from json import dumps

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'POST':
		id = request.form['id']
		center_lat = request.form['center_lat']
		center_lon = request.form['center_lon']
		zoom = request.form['zoom']
		dbHandler.insertMap(id, center_lat, center_lon, zoom)
		maps = dbHandler.retrieveMap()
		return render_template('index.html', maps=maps)
	else:
   		return render_template('index.html')

@app.route("/getjson")
def getJsonList():
	mapList = []
	maps = dbHandler.retrieveMap()
	for map in maps:
		mapDict = {
        	'Id': map[0],
        	'Reated': map[1],
        	'Center_lat': map[2],
        	'Center_lon': map[3],
			'Zoom': map[4]}
    	mapList.append(mapDict)
	return json.dumps(mapList)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
