import datetime


class Responses:
    def successfullResponses(message, data):
        response = {
            "statusCode": 200,
            "message": message,
            "time": datetime.datetime.now(),
            "data": data
        }
        
        print(response)
        return response
        
    def failedResponses(message, code):
        response = {
            "statusCode": code,
            "message": message,
            "time": datetime.datetime.now(),
            "data": None
        }
        
        print(response)
        return response
