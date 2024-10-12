# CoreApiV2.Repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataProviderSourceStats** | **[Object]** | Statistics based on the Data Provider/repository rather than data processed and filtered by CORE. This array is in beta and may change in the future | [optional] 
**history** | **[Object]** | The number of deposits in the repository per date. This field is in beta and may change in the future | [optional] 
**historyCumulative** | **[Object]** | The number of deposits in the repository per date over time (cumulative). This field is in beta and may change in the future | [optional] 
**id** | **Number** | CORE repository ID | [optional] 
**lastSeen** | **Date** | The time the repository was last harvested by CORE. This field is in beta and may change in the future | [optional] 
**name** | **String** | Repository name | [optional] 
**openDoarId** | **Number** | ID of the repository in Open DOAR | [optional] 
**repositoryLocation** | [**RepositoryLocation**](RepositoryLocation.md) |  | [optional] 
**repositoryStats** | [**RepositoryStats**](RepositoryStats.md) |  | [optional] 
**uri** | **String** | Repository URI | [optional] 
**urlHomepage** | **String** | Repository homepage | [optional] 
**urlOaipmh** | **String** | Repository OAI-PMH endpoint | [optional] 


