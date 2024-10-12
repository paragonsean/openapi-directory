# CosmosDb.ConflictResolutionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflictResolutionPath** | **String** | The conflict resolution path in the case of LastWriterWins mode. | [optional] 
**conflictResolutionProcedure** | **String** | The procedure to resolve conflicts in the case of custom mode. | [optional] 
**mode** | **String** | Indicates the conflict resolution mode. | [optional] [default to &#39;LastWriterWins&#39;]



## Enum: ModeEnum


* `LastWriterWins` (value: `"LastWriterWins"`)

* `Custom` (value: `"Custom"`)




