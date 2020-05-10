from flask import Flask,jsonify
app = Flask(__name__)

users= [{"userid":"sridharc20", "name":"Sridhar C"},
        {"userid":"venu1", "name" : "Venu G"}
        ]

@app.route("/users/<userid>")
def getusers(userid):
    return search(userid)

def search(userid):
    for user in users:
        if(user["userid"] == userid):
            return jsonify(user['name'])

if __name__=="__main__":
    app.run();

