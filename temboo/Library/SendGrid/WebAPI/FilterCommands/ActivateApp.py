# -*- coding: utf-8 -*-

###############################################################################
#
# ActivateApp
# Activate an app.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ActivateApp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ActivateApp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/FilterCommands/ActivateApp')


    def new_input_set(self):
        return ActivateAppInputSet()

    def _make_result_set(self, result, path):
        return ActivateAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ActivateAppChoreographyExecution(session, exec_id, path)

class ActivateAppInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ActivateApp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        InputSet._set_input(self, 'APIUser', value)
    def set_AppName(self, value):
        """
        Set the value of the AppName input for this Choreo. ((required, string) The name of the app to be activated.  A list of available apps can be obtained by running the ListAvailableApps Choreo.)
        """
        InputSet._set_input(self, 'AppName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)


class ActivateAppResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ActivateApp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class ActivateAppChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ActivateAppResultSet(response, path)
