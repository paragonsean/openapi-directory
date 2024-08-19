# GoogleCivicInformationApi.VoterInfoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contests** | [**[Contest]**](Contest.md) | Contests that will appear on the voter&#39;s ballot. | [optional] 
**dropOffLocations** | [**[PollingLocation]**](PollingLocation.md) | Locations where a voter is eligible to drop off a completed ballot. The voter must have received and completed a ballot prior to arriving at the location. The location may not have ballots available on the premises. These locations could be open on or before election day as indicated in the pollingHours field. | [optional] 
**earlyVoteSites** | [**[PollingLocation]**](PollingLocation.md) | Locations where the voter is eligible to vote early, prior to election day. | [optional] 
**election** | [**Election**](Election.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;civicinfo#voterInfoResponse\&quot;. | [optional] [default to &#39;civicinfo#voterInfoResponse&#39;]
**mailOnly** | **Boolean** | Specifies whether voters in the precinct vote only by mailing their ballots (with the possible option of dropping off their ballots as well). | [optional] 
**normalizedInput** | [**SimpleAddressType**](SimpleAddressType.md) |  | [optional] 
**otherElections** | [**[Election]**](Election.md) | When there are multiple elections for a voter address, the otherElections field is populated in the API response and there are two possibilities: 1. If the earliest election is not the intended election, specify the election ID of the desired election in a second API request using the electionId field. 2. If these elections occur on the same day, the API doesn?t return any polling location, contest, or election official information to ensure that an additional query is made. For user-facing applications, we recommend displaying these elections to the user to disambiguate. A second API request using the electionId field should be made for the election that is relevant to the user. | [optional] 
**pollingLocations** | [**[PollingLocation]**](PollingLocation.md) | Locations where the voter is eligible to vote on election day. | [optional] 
**precinctId** | **String** |  | [optional] 
**precincts** | [**[Precinct]**](Precinct.md) | The precincts that match this voter&#39;s address. Will only be returned for project IDs which have been allowlisted as \&quot;partner projects\&quot;. | [optional] 
**state** | [**[AdministrationRegion]**](AdministrationRegion.md) | Local Election Information for the state that the voter votes in. For the US, there will only be one element in this array. | [optional] 


