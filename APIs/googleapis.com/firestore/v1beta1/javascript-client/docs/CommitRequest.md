# CloudFirestoreApi.CommitRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **Blob** | If set, applies all writes in this transaction, and commits it. | [optional] 
**writes** | [**[Write]**](Write.md) | The writes to apply. Always executed atomically and in order. | [optional] 


