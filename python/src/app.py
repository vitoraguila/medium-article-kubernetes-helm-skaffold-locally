import os.path
import csv
import json
from flask import Flask
from flask import request
from flask import jsonify
from youtube_transcript_api import YouTubeTranscriptApi

dataPath = "users.json"
class Customer:
  def __init__(self, c="",f="",l=""):
    self.customerID = c
    self.firstName  = f
    self.lastName   = l
  def fullName(self):
    return self.firstName + " " + self.lastName

def getCustomers():
  if os.path.isfile(dataPath):
    with open(dataPath, newline='') as customerFile:
      data = customerFile.read()
      customers = json.loads(data)
      return customers
  else: 
    return {}

def getCustomer(customerID):
  customers = getCustomers()

  if customerID in customers:
    return customers[customerID]
  else:
    return {}

app = Flask(__name__)

@app.route("/api/python/users", methods=['GET'])
def get_customers():
    customers = getCustomers()
    return jsonify(customers), 200

@app.route("/api/python/captions/<string:videoID>", methods=['GET'])
def get_captions(videoID):
    captions = YouTubeTranscriptApi.get_transcript(videoID)

    return jsonify(captions), 200