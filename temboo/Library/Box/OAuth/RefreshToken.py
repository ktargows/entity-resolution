# -*- coding: utf-8 -*-

###############################################################################
#
# RefreshToken
# Generates a new access token with a given valid refresh token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RefreshToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RefreshToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/OAuth/RefreshToken')


    def new_input_set(self):
        return RefreshTokenInputSet()

    def _make_result_set(self, result, path):
        return RefreshTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefreshTokenChoreographyExecution(session, exec_id, path)

class RefreshTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RefreshToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by Box after registering your application.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret provided by Box after registering your application.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) A valid refresh token used to generate a new access token.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class RefreshTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RefreshToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((string) The access token for the user that has granted access to your application.)
        """
        return self._output.get('AccessToken', None)
    def get_Expires(self):
        """
        Retrieve the value for the "Expires" output from this Choreo execution. ((integer) The expiration time of the access_token retrieved.)
        """
        return self._output.get('Expires', None)
    def get_NewRefreshToken(self):
        """
        Retrieve the value for the "NewRefreshToken" output from this Choreo execution. ((string) The new refresh token which can be used the next time your app needs to get a new access token.)
        """
        return self._output.get('NewRefreshToken', None)

class RefreshTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RefreshTokenResultSet(response, path)
