

# CampaignSound

Represents a sound recording from account's sound library which can be used in different API operations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **Long** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**duplicate** | **Boolean** | True if the same sound file exists in a sound library of account |  [optional] [readonly] |
|**id** | **Long** | An id of a sound file |  [optional] |
|**lengthInSeconds** | **Integer** | Length of a sound in seconds |  [optional] [readonly] |
|**name** | **String** | A name of a sound file |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A current status of a sound, available values: UPLOAD - uploading is in progress, RECORDING - recording of sound is in progress, ACTIVE - sound is ready, FAILED, ARCHIVED - sound was archived, SCRUBBED - sound was scrubbed  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UPLOAD | &quot;UPLOAD&quot; |
| RECORDING | &quot;RECORDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ACTIVE_SYSTEM | &quot;ACTIVE_SYSTEM&quot; |
| FAILED | &quot;FAILED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| SCRUBBED | &quot;SCRUBBED&quot; |



