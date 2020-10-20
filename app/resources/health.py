from flask_restful import Resource


class HealthCheck(Resource):
    """
    Class only used as health check return
    It should return a HTTP 200 response code when invoked
    """
    
    @staticmethod
    def get() -> str:
        """
        Will be activated when the endpoint receives a HTTP GET method

        Returns:
             string only aiming a HTTP 200 response code
        """
        return "OK"
