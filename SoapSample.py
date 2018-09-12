import sys
from pysimplesoap.client import SoapClient

def UseSoapFunction(param1, param2):
  client = SoapClient(wsdl="http://..//simple.asmx?wsdl")
  response = client.SoapFunction(param1=param1,param2=param2)
  result = response["SoapFunctionResult"]
  
params = sys.argv

if len(params) < 3
  print('usage : python SoapSample.py param1, param2')
  sys.exit()
  
UseSoapFunction(params[1], params[2])

