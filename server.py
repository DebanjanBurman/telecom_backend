from flask import Flask,jsonify,request
from datetime import datetime
from flask_cors import CORS 
import json

app = Flask(__name__)
CORS(app)

### API to insert a new customer along with their plan ###
@app.route("/insertCustomer",methods = ["POST"])
def insertCustomer():
    try:
        print("In insertCustomer")
        reqst = request.get_json()
        cust_name = reqst["cust_name"]
        birthday = reqst["birthday"]
        cust_email = reqst["cust_email"]
        aadhar = reqst["aadhar"]
        regn_date = reqst["regn_date"]
        phone = reqst["phone"]
        plan_name = reqst["plan_name"]
        plan_cost = reqst["plan_cost"]
        plan_validity = reqst["plan_validity"]
        plan_status = reqst["plan_status"]
        renewal_date = reqst["renewal_date"]
        with open('database.json') as json_file:
            data_list = json.load(json_file)
        for record in data_list:
            if(record["Aadhar"]==aadhar):
                return jsonify("Customer already exists")
        data_list.append(
            {
                "Name": cust_name,
                "DOB": birthday,
                "Email": cust_email,
                "Aadhar": aadhar,
                "Registration_Date": regn_date,
                "Mobile": phone,
                "Plan_Name": plan_name,
                "Plan_Cost": plan_cost,
                "Plan_Validity": plan_validity,
                "Plan_Status": plan_status,
                "Renewal_Date": renewal_date
            }
        )
        print(data_list)
        try:
            with open("database.json", "w") as jsonFile:
                json.dump(data_list, jsonFile)
        except Exception as e:
            return jsonify("File update failed due to "+str(e))
        return jsonify("Success")
    except Exception as e:
        print("Error occurred: "+str(e))
        return jsonify("Failure")

### API to update details of logged in customer ###
@app.route("/updateCustomer",methods = ["POST"])
def updateCustomer():
    try:
        print("In updateCustomer")
        reqst = request.get_json()
        cust_name = reqst["cust_name"]
        birthday = reqst["birthday"]
        cust_email = reqst["cust_email"]
        aadhar = reqst["aadhar"]
        regn_date = reqst["regn_date"]
        phone = reqst["phone"]
        plan_name = reqst["plan_name"]
        plan_cost = reqst["plan_cost"]
        plan_validity = reqst["plan_validity"]
        plan_status = reqst["plan_status"]
        renewal_date = reqst["renewal_date"]
        with open('database.json') as json_file:
            data_list = json.load(json_file)
        for i in range(len(data_list)):
            if(data_list[i]["Aadhar"]==aadhar):
                data_list[i] = {
                                "Name": cust_name,
                                "DOB": birthday,
                                "Email": cust_email,
                                "Aadhar": aadhar,
                                "Registration_Date": regn_date,
                                "Mobile": phone,
                                "Plan_Name": plan_name,
                                "Plan_Cost": plan_cost,
                                "Plan_Validity": plan_validity,
                                "Plan_Status": plan_status,
                                "Renewal_Date": renewal_date
                                }  
                break      
        print(data_list)
        try:
            with open("database.json", "w") as jsonFile:
                json.dump(data_list, jsonFile)
        except Exception as e:
            return jsonify("File update failed due to "+str(e))
        return jsonify("Success")
    except Exception as e:
        print("Error occurred: "+str(e))
        return jsonify("Failure")

### API to display customer table along with their plans ###
@app.route("/displayCustomer",methods = ["GET"])
def displayCustomer():
    try:
        print("In displayCustomer")
        with open('database.json') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except Exception as e:
        print("Error occurred: "+str(e))
        return jsonify("Failure")

### API to search for logged in customer's details ###
@app.route("/getLoggedInUserDetails", methods=["POST"])
def getLoggedInUserDetails():
    try:
        print("In getLoggedInUserDetails")
        reqst = request.get_json()
        aadhar = reqst["aadhar"]
        with open('database.json') as json_file:
            data_list = json.load(json_file)
        for record in data_list:
            if(record["Aadhar"]==aadhar):
                return jsonify(record)
        return jsonify("No records found for this user.")
    except Exception as e:
        return jsonify("Some error occured: "+str(e))

### Run flask server from a host and enable CORS ###
if __name__=='__main__':
    app.run(host="172.25.16.1",port=9020, threaded=True)