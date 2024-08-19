

# RecordStartResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**recordFile** | **String** | Directory path/URI where the recording file will be saved |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| RECORD_START_EXECUTED | &quot;RecordStart Executed&quot; |
| CALL_UUID_PARAMETER_MUST_BE_PRESENT | &quot;CallUUID Parameter must be present&quot; |
| FILE_FORMAT_PARAMETER_MUST_BE | &quot;FileFormat Parameter must be&quot; |
| RECORD_START_FAILED_INVALID_TIME_LIMIT | &quot;RecordStart Failed: invalid TimeLimit&quot; |
| RECORD_START_FAILED_CALL_NOT_FOUND | &quot;RecordStart Failed -- Call not found&quot; |
| RECORD_START_FAILED | &quot;RecordStart Failed&quot; |



