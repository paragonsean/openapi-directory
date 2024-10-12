# CloudFirestoreApi.CommitResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitTime** | **String** | The time at which the commit occurred. Any read with an equal or greater &#x60;read_time&#x60; is guaranteed to see the effects of the commit. | [optional] 
**writeResults** | [**[WriteResult]**](WriteResult.md) | The result of applying the writes. This i-th write result corresponds to the i-th write in the request. | [optional] 


