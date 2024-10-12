

# PutRecordBatchResponseEntry

Contains the result for an individual record from a <a>PutRecordBatch</a> request. If the record is successfully added to your delivery stream, it receives a record ID. If the record fails to be added to your delivery stream, the result includes an error code and an error message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recordId** | [**String**](String.md) |  |  [optional] |
|**errorCode** | [**String**](String.md) |  |  [optional] |
|**errorMessage** | [**String**](String.md) |  |  [optional] |



