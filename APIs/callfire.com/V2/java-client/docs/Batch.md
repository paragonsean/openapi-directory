

# Batch

A batch represents a group of contacts which can be dialed or texted via call/text broadcast

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**broadcastId** | **Long** | An id of broadcast which batch belongs to |  [optional] |
|**created** | **Long** | A date and time when batch was created, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**enabled** | **Boolean** | An enabled batch. If batch is disabled its contacts remain undialed/untexted |  [optional] |
|**id** | **Long** | A id of a batch |  [optional] |
|**name** | **String** | A batch name |  [optional] |
|**remaining** | **Integer** | A number of contacts remaining undialed/untexted |  [optional] [readonly] |
|**size** | **Integer** | A total number of contacts in batch |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | A status of batch (NEW, VALIDATING, ERRORS, SOURCE_ERROR, ACTIVE). NEW - batch is queued for validation; VALIDATING - batch is currently validating; ERRORS - batch is processed, some validation errors occurred; SOURCE_ERROR - if contact source is contact list in CallFire system and it has an error; ACTIVE - batch is processed and ready |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;NEW&quot; |
| VALIDATING | &quot;VALIDATING&quot; |
| ERRORS | &quot;ERRORS&quot; |
| SOURCE_ERROR | &quot;SOURCE_ERROR&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



