# ContentDepot.ProgramInformationBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDate** | **String** | The date and time the batch was created. | 
**finishedDate** | **String** | The date and time the batch finished (either successful or failed). | [optional] 
**format** | **String** | The format of the metadata file defining the create or update actions to be performed on one or more EPG programs. | 
**id** | **Number** | The ID of the batch. | 
**message** | **String** | The human readable success or failure message. | [optional] 
**name** | **String** | The optional name of the batch for human reference. | [optional] 
**program** | [**ProgramInformationBatchProgram**](ProgramInformationBatchProgram.md) |  | [optional] 
**status** | **String** | The current processing status. | 
**uri** | **String** | The URI to the metadata file defining the batch creates/updates. | [optional] 



## Enum: FormatEnum


* `radiodns` (value: `"radiodns"`)





## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `processing` (value: `"processing"`)

* `failed` (value: `"failed"`)

* `successful` (value: `"successful"`)




