# -*- coding: utf-8 -*-

###############################################################################
#
# CommitteeSearch
# Search for a political action committee (PACs) by name, or partial name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CommitteeSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CommitteeSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/Committees/CommitteeSearch')


    def new_input_set(self):
        return CommitteeSearchInputSet()

    def _make_result_set(self, result, path):
        return CommitteeSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeSearchChoreographyExecution(session, exec_id, path)

class CommitteeSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CommitteeSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CampaignCycle(self, value):
        """
        Set the value of the CampaignCycle input for this Choreo. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year. )
        """
        InputSet._set_input(self, 'CampaignCycle', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) Specify the name of the committee to be retireved. Partial names are also acceptable.  Examples: viacom.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class CommitteeSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CommitteeSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class CommitteeSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CommitteeSearchResultSet(response, path)
