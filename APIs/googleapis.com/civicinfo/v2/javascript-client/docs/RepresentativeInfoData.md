# GoogleCivicInformationApi.RepresentativeInfoData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**divisions** | [**{String: GeographicDivision}**](GeographicDivision.md) | A map of political geographic divisions that contain the requested address, keyed by the unique Open Civic Data identifier for this division. | [optional] 
**offices** | [**[Office]**](Office.md) | Elected offices referenced by the divisions listed above. Will only be present if includeOffices was true in the request. | [optional] 
**officials** | [**[Official]**](Official.md) | Officials holding the offices listed above. Will only be present if includeOffices was true in the request. | [optional] 


