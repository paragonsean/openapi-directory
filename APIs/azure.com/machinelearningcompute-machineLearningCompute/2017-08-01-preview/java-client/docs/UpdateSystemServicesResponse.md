

# UpdateSystemServicesResponse

Response of the update system services API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**updateCompletedOn** | **OffsetDateTime** | The date and time when the last system services update completed. |  [optional] [readonly] |
|**updateStartedOn** | **OffsetDateTime** | The date and time when the last system services update was started. |  [optional] [readonly] |
|**updateStatus** | [**UpdateStatusEnum**](#UpdateStatusEnum) | Update status |  [optional] [readonly] |



## Enum: UpdateStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UPDATING | &quot;Updating&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



