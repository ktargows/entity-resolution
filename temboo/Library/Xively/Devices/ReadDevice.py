# -*- coding: utf-8 -*-

###############################################################################
#
# ReadDevice
# Returns a JSON representation of the device with the provided serial number.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReadDevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReadDevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Devices/ReadDevice')


    def new_input_set(self):
        return ReadDeviceInputSet()

    def _make_result_set(self, result, path):
        return ReadDeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReadDeviceChoreographyExecution(session, exec_id, path)

class ReadDeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReadDevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The product ID of the device you would like to read.)
        """
        InputSet._set_input(self, 'ProductID', value)
    def set_SerialNumber(self, value):
        """
        Set the value of the SerialNumber input for this Choreo. ((required, string) The serial number for the device you would like to read.)
        """
        InputSet._set_input(self, 'SerialNumber', value)

class ReadDeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReadDevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Xively.)
        """
        return self._output.get('Response', None)

class ReadDeviceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReadDeviceResultSet(response, path)
