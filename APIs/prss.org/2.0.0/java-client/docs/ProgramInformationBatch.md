

# ProgramInformationBatch

An electronic program guide (EPG) batch operation to create or update metadata on one or more guide programs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDate** | **String** | The date and time the batch was created. |  |
|**finishedDate** | **String** | The date and time the batch finished (either successful or failed). |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | The format of the metadata file defining the create or update actions to be performed on one or more EPG programs. |  |
|**id** | **Long** | The ID of the batch. |  |
|**message** | **String** | The human readable success or failure message. |  [optional] |
|**name** | **String** | The optional name of the batch for human reference. |  [optional] |
|**program** | [**ProgramInformationBatchProgram**](ProgramInformationBatchProgram.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current processing status. |  |
|**uri** | **URI** | The URI to the metadata file defining the batch creates/updates. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| RADIODNS | &quot;radiodns&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| PROCESSING | &quot;processing&quot; |
| FAILED | &quot;failed&quot; |
| SUCCESSFUL | &quot;successful&quot; |



