

# ChangeRequest

Content of the change request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptable** | **Boolean** |  |  [optional] |
|**changes** | [**ChangeRequestChanges**](ChangeRequestChanges.md) |  |  [optional] |
|**createdBy** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DEPLOYED | &quot;Deployed&quot; |
| PENDING_DEPLOYMENT | &quot;Pending deployment&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| PENDING_VALIDATION | &quot;Pending validation&quot; |
| OPEN | &quot;Open&quot; |



