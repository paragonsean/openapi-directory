

# UpdateSystemResponse

Response of the updateSystem API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**updateCompletedOn** | **OffsetDateTime** | Read Only: The date and time when the last system services update completed. |  [optional] [readonly] |
|**updateStartedOn** | **OffsetDateTime** | Read Only: The date and time when the last system services update was started. |  [optional] [readonly] |
|**updateStatus** | [**UpdateStatusEnum**](#UpdateStatusEnum) | Update status |  [optional] [readonly] |



## Enum: UpdateStatusEnum

| Name | Value |
|---- | -----|
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |



