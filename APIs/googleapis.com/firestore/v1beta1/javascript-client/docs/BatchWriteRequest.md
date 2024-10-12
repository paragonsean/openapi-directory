# CloudFirestoreApi.BatchWriteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | Labels associated with this batch write. | [optional] 
**writes** | [**[Write]**](Write.md) | The writes to apply. Method does not apply writes atomically and does not guarantee ordering. Each write succeeds or fails independently. You cannot write to the same document more than once per request. | [optional] 


