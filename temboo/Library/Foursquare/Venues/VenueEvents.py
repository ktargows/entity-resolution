# -*- coding: utf-8 -*-

###############################################################################
#
# VenueEvents
# Allows you to access information about the current events at a place.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareEvent import FoursquareEvent
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class VenueEvents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VenueEvents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/VenueEvents')


    def new_input_set(self):
        return VenueEventsInputSet()

    def _make_result_set(self, result, path):
        return VenueEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VenueEventsChoreographyExecution(session, exec_id, path)

class VenueEventsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VenueEvents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The ID associated with the venue you want to retrieve details for.)
        """
        InputSet._set_input(self, 'VenueID', value)

class VenueEventsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VenueEvents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getMeta(self):
        """
        Get the response status code
        """
        return FoursquareMeta(self.getJSONFromString(self._output.get('Response', [])).get("meta", []))
    def getNotifications(self):
        """
        Get the count of unread notifications for the authenticated user
        """
        return [FoursquareNotification(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("notifications", [])]

    def getEvents(self):
        """
        Get venue events
        """
        return [FoursquareEvent(le) for le in self.getJSONObject(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response"), "events").get("items", [])]


class VenueEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VenueEventsResultSet(response, path)