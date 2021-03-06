# -*- coding: utf-8 -*-

###############################################################################
#
# ReverseGeocode
# Given a latitude and a longitude coordinates, returns up to 20 places that can be used as a Place ID when updating a status.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReverseGeocode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReverseGeocode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/PlacesAndGeo/ReverseGeocode')


    def new_input_set(self):
        return ReverseGeocodeInputSet()

    def _make_result_set(self, result, path):
        return ReverseGeocodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReverseGeocodeChoreographyExecution(session, exec_id, path)

class ReverseGeocodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReverseGeocode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, string) A hint on the "region" in which to search. If a number, then this is a radius in meters. You can also specify feet by using the ft suffix (i.e. 5ft).)
        """
        InputSet._set_input(self, 'Accuracy', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) If supplied, the response will use the JSONP format with a callback of the given name.)
        """
        InputSet._set_input(self, 'Callback', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_Granularity(self, value):
        """
        Set the value of the Granularity input for this Choreo. ((optional, string) This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. Defaults to neighborhood.)
        """
        InputSet._set_input(self, 'Granularity', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude to search around.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude to search around.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        InputSet._set_input(self, 'MaxResults', value)

class ReverseGeocodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReverseGeocode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class ReverseGeocodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReverseGeocodeResultSet(response, path)
