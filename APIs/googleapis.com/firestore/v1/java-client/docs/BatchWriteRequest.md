

# BatchWriteRequest

The request for Firestore.BatchWrite.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labels** | **Map&lt;String, String&gt;** | Labels associated with this batch write. |  [optional] |
|**writes** | [**List&lt;Write&gt;**](Write.md) | The writes to apply. Method does not apply writes atomically and does not guarantee ordering. Each write succeeds or fails independently. You cannot write to the same document more than once per request. |  [optional] |



