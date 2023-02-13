var http = require('http')
var options = {
	hostname: 'host3.dreamhack.games',
	path: '/img_viewer', // or with GET argument
	method: 'POST', // or 'GET'
	port: 8288,
	headers: { // just example
		'Origin': 'http://localhost:1337',
		'Content-Type': 'application/x-www-form-urlencoded'
	}
}

myinput = ""

function SendItem()
{
	return new Promise((resolve, reject) => {
		var total = ""
		var req = http.request(options, (res) => {
			//on response data
			res.on('data', function(body) {
				total += body.toString()
			})
			// on response end
			res.on('end', function() {
				process.stdout.write(tmp.toString())
				resolve()
			})
			// on response error
			res.on('error', function(err) {
				reject(err)
			})
		})
		
		// on request error
		req.on('error', function(e) {
			console.log("Got Error: " + e.message)
		})
		
		//WriteBody
		req.write(myinput)
		// send request
		req.end()
	})
}

async function DoJob()
{
	myinput = "url=http%3A%2F%2FLOCALHOST%3A") // just example
	await SendItem()
}

DoJob()