#!/usr/bin/env python
import web
#import xml.etree.ElementTree as ET
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
        output='cciao'
        data=web.data()
        json_data=json.loads(data)
        text=json_data['text']
        print text
        keywords=rake.run(text)
        #return simplejson.dumps(dict([("%d,%d" % k, v) for k, v in keywords.items()]))
        return json.dumps(keywords)

class index:
    def GET(self, user):
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