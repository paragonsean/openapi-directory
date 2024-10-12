# CloudFirestoreApi.WriteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | Labels associated with this write request. | [optional] 
**streamId** | **String** | The ID of the write stream to resume. This may only be set in the first message. When left empty, a new write stream will be created. | [optional] 
**streamToken** | **Blob** | A stream token that was previously sent by the server. The client should set this field to the token from the most recent WriteResponse it has received. This acknowledges that the client has received responses up to this token. After sending this token, earlier tokens may not be used anymore. The server may close the stream if there are too many unacknowledged responses. Leave this field unset when creating a new stream. To resume a stream at a specific point, set this field and the &#x60;stream_id&#x60; field. Leave this field unset when creating a new stream. | [optional] 
**writes** | [**[Write]**](Write.md) | The writes to apply. Always executed atomically and in order. This must be empty on the first request. This may be empty on the last request. This must not be empty on all other requests. | [optional] 


