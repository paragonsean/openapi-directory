

# ConferenceRecordStartResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**recordFile** | **String** | Directory path/URI where the recording file will be saved |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| CONFERENCE_RECORD_START_EXECUTED | &quot;Conference RecordStart Executed&quot; |
| CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT | &quot;ConferenceName Parameter must be present&quot; |
| FILE_FORMAT_PARAMETER_MUST_BE | &quot;FileFormat Parameter must be&quot; |
| CONFERENCE_RECORD_START_FAILED | &quot;Conference RecordStart Failed&quot; |
| CONFERENCE_RECORD_START_FAILED_CONFERENCE_NOT_FOUND | &quot;Conference RecordStart Failed -- Conference not found&quot; |



