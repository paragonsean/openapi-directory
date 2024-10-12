# StreetViewPublishApi.ListPhotoSequencesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | Token to retrieve the next page of results, or empty if there are no more results in the list. | [optional] 
**photoSequences** | [**[Operation]**](Operation.md) | List of photo sequences via Operation interface. The maximum number of items returned is based on the pageSize field in the request. Each item in the list can have three possible states, * &#x60;Operation.done&#x60; &#x3D; false, if the processing of PhotoSequence is not finished yet. * &#x60;Operation.done&#x60; &#x3D; true and &#x60;Operation.error&#x60; is populated, if there was an error in processing. * &#x60;Operation.done&#x60; &#x3D; true and &#x60;Operation.response&#x60; contains a PhotoSequence message, In each sequence, only Id is populated. | [optional] 


