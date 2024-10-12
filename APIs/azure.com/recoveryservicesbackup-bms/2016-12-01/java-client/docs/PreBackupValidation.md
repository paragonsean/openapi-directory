

# PreBackupValidation

Pre-backup validation for Azure VM Workload provider.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Error code of protectable item |  [optional] |
|**message** | **String** | Message corresponding to the error code for the protectable item |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of protectable item, i.e. InProgress,Succeeded,Failed |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| SUCCESS | &quot;Success&quot; |
| FAILED | &quot;Failed&quot; |



