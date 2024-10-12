# CloudFirestoreApi.WriteResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitTime** | **String** | The time at which the commit occurred. Any read with an equal or greater &#x60;read_time&#x60; is guaranteed to see the effects of the write. | [optional] 
**streamId** | **String** | The ID of the stream. Only set on the first message, when a new stream was created. | [optional] 
**streamToken** | **Blob** | A token that represents the position of this response in the stream. This can be used by a client to resume the stream at this point. This field is always set. | [optional] 
**writeResults** | [**[WriteResult]**](WriteResult.md) | The result of applying the writes. This i-th write result corresponds to the i-th write in the request. | [optional] 


