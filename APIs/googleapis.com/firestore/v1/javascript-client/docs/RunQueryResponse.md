# CloudFirestoreApi.RunQueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**Document**](Document.md) |  | [optional] 
**done** | **Boolean** | If present, Firestore has completely finished the request and no more documents will be returned. | [optional] 
**readTime** | **String** | The time at which the document was read. This may be monotonically increasing; in this case, the previous documents in the result stream are guaranteed not to have changed between their &#x60;read_time&#x60; and this one. If the query returns no results, a response with &#x60;read_time&#x60; and no &#x60;document&#x60; will be sent, and this represents the time at which the query was run. | [optional] 
**skippedResults** | **Number** | The number of results that have been skipped due to an offset between the last response and the current response. | [optional] 
**transaction** | **Blob** | The transaction that was started as part of this request. Can only be set in the first response, and only if RunQueryRequest.new_transaction was set in the request. If set, no other fields will be set in this response. | [optional] 


