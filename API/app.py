import sys
import os
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json
import pyodbc

# Initialize Flask
app = Flask(__name__)

# Setup Flask Restful framework
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('customer')

# Create connection to Azure SQL
conn = pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF'])

class Queryable(Resource):
    def executeQueryJson(self, verb, payload=None):
        result = {}        
        cursor = conn.cursor()    
        entity = type(self).__name__.lower()
        procedure = f"dbo.{verb}_{entity}"
        try:
            if payload:
                cursor.execute(f"EXEC {procedure} ?", json.dumps(payload))
            else:
                cursor.execute(f"EXEC {procedure}")

            result = cursor.fetchone()

            if result:
                result = json.loads(result[0])                           
            else:
                result = {}

            cursor.commit()    
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        finally:    
            cursor.close()

        return result

# Customer Class
class Customer(Queryable):
    def get(self, customer_id):     
        customer = {}
        customer["CustomerID"] = customer_id
        result = self.executeQueryJson("get", customer)   
        return result, 200
    
    def put(self):
        args = parser.parse_args()
        customer = json.loads(args['customer'])
        result = self.executeQueryJson("put", customer)
        return result, 201

    def patch(self, customer_id):
        args = parser.parse_args()
        customer = json.loads(args['customer'])
        customer["CustomerID"] = customer_id        
        result = self.executeQueryJson("patch", customer)
        return result, 202

    def delete(self, customer_id):       
        customer = {}
        customer["CustomerID"] = customer_id
        result = self.executeQueryJson("delete", customer)
        return result, 202

# Customers Class
class Customers(Queryable):
    def get(self):     
        result = self.executeQueryJson("get")   
        return result, 200

# Application Class
class Application(Queryable):
    def get(self, applicationid):     
        application = {}
        application["ApplicationID"] = application_id
        result = self.executeQueryJson("get", application)   
        return result, 200
    
    def put(self):
        args = parser.parse_args()
        application = json.loads(args['application'])
        result = self.executeQueryJson("put", application)
        return result, 201

    def patch(self, application_id):
        args = parser.parse_args()
        application = json.loads(args['application'])
        application["ApplicationId"] = application_id        
        result = self.executeQueryJson("patch", application)
        return result, 202

    def delete(self, application_id):       
        customer = {}
        application["ApplicationId"]  = application_id
        result = self.executeQueryJson("delete", application)
        return result, 202

# Application Class
class Applications(Queryable):
    def get(self):     
        result = self.executeQueryJson("get")   
        return result, 200
              
# Users Class
class User(Queryable):
    def get(self, user_id):     
        user = {}
        user["UserID"] = user_id
        result = self.executeQueryJson("get", user)   
        return result, 200
    
    def put(self):
        args = parser.parse_args()
        user = json.loads(args['user'])
        result = self.executeQueryJson("put", user)
        return result, 201

    def patch(self, user_id):
        args = parser.parse_args()
        customer = json.loads(args['user'])
        customer["UserID"] = user_id        
        result = self.executeQueryJson("patch", user)
        return result, 202

    def delete(self, customer_id):       
        customer = {}
        customer["UserID"] = user_id
        result = self.executeQueryJson("delete", user)
        return result, 202

# Users Class
class Users(Queryable):
    def get(self):     
        result = self.executeQueryJson("get")   
        return result, 200

# ApplicationTrack Class
class Trackapplication(Queryable):
    def get(self, applicationtracker_id):     
        track = {}
        track["ApplicationtrackerID"] = applicationtracker_id
        result = self.executeQueryJson("get", track)   
        return result, 200
    
    def put(self):
        args = parser.parse_args()
        track = json.loads(args['track'])
        result = self.executeQueryJson("put", track
        return result, 201

    def patch(self, applicationtracker_id):
        args = parser.parse_args()
        track = json.loads(args['track'])
        track["ApplicationtrackerID"] = applicationtracker_id       
        result = self.executeQueryJson("patch", track)
        return result, 202

    def delete(self, applicationtracker_id):       
        track = {}
        track["ApplicationtrackerID"] = applicationtracker_id       
        result = self.executeQueryJson("delete", track)
        return result, 202

# ApplicationTrack Class
class Trackapplications(Queryable):
    def get(self):     
        result = self.executeQueryJson("get")   
        return result, 200
        

# Loan Class
class Loan(Queryable):
    def get(self, loan_id):     
        loan = {}
        loan["LoanID"] = loan_id
        result = self.executeQueryJson("get", loan)   
        return result, 200
    
    def put(self):
        args = parser.parse_args()
        loan = json.loads(args['loan'])
        result = self.executeQueryJson("put", loan)
        return result, 201

    def patch(self, loan_id):
        args = parser.parse_args()
        customer = json.loads(args['loan'])
        loan = json.loads(args['loan'])
        result = self.executeQueryJson("patch", loan)
        return result, 202

    def delete(self, loan_id):       
        loan= {}
        loan = json.loads(args['loan'])
        result = self.executeQueryJson("delete", loan)
        return result, 202

# Loans Class
class Loans(Queryable):
    def get(self):     
        result = self.executeQueryJson("get")   
        return result, 200

 # Loan Repayment Class
class LoanRepayment(Queryable):
    def get(self, loanrepayment_id):     
        loanrepayment= {}
        loanrepayment["LoanID"] = loanrepayment_id
        result = self.executeQueryJson("get", loanrepayment)   
        return result, 200
    
    def put(self):
        args = parser.parse_args()
        loanrepayment = json.loads(args['loanrepayment'])
        result = self.executeQueryJson("put", loanrepayment)
        return result, 201

    def patch(self, loan_id):
        args = parser.parse_args()
        loanrepayment = json.loads(args['loanrepayment'])
        result = self.executeQueryJson("patch", loanrepayment)
        return result, 202

    def delete(self, loanrepayment_id):       
        loanrepayment= {}
        loanrepayment = json.loads(args['loanrepayment'])
        result = self.executeQueryJson("delete", loanrepayment)
        return result, 202

# Loan Repayment Class
class LoanRepayments(Queryable):
    def get(self):     
        result = self.executeQueryJson("get")   
        return result, 200
   
    
# Create API routes
api.add_resource(Customer, '/customer', '/customer/<customer_id>')
api.add_resource(Customers, '/customers')
api.add_resource(User, '/user', '/user/<user_id>')
api.add_resource(Users, '/users)
api.add_resource(User, '/application', '/application/<application_id>')
api.add_resource(Users, '/applications)
api.add_resource(User, '/applicationtrack', '/track/<applicationtracker_id>')
api.add_resource(Users, '/applicationtracks)
api.add_resource(User, '/loan', '/loan/<loan_id>')
api.add_resource(Users, '/loans)
api.add_resource(User, '/loanrepayment', '/loanrepayment/<loanrepayment_id>')
api.add_resource(Users, '/loanrepayments)
