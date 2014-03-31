

import web
import json

from rake import Rake 


#tree = ET.parse('user_data.xml')
#root = tree.getroot()

rake=Rake("SmartStoplist.txt")

urls = (
    '/keywords', 'calculate_keywords',
    '/', 'index',
    #'/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class calculate_keywords:        
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials','true') 
        web.header('Content-Type','application/json') 
        web.header['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        web.header['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


        output='cciao'
        data=web.data()
        json_data=json.loads(data)
        text=json_data['text']
        print text
        keywords=rake.run(text)
        #return simplejson.dumps(dict([("%d,%d" % k, v) for k, v in keywords.items()]))
        return json.dumps(keywords)

class index:
    def GET(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials','true') 
        return """
            <html>
                <head></head>
                <body>
                    <h1>Welcome!</h1>
                </body>
            </html>"""

"""
class get_user:
    def GET(self, user):
	for child in root:
		if child.attrib['id'] == user:
		    return str(child.attrib)
"""


if __name__ == "__main__":
    app.run()
