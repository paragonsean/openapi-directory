

# BusinessName

The Business Name resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**id** | **String** | The resource&#39;s unique identifier. |  [optional] [readonly] |
|**lifecycleState** | [**LifecycleStateEnum**](#LifecycleStateEnum) | The business name&#39;s lifecycle state. |  [optional] |
|**name** | **String** | The business name. |  [optional] |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |



## Enum: LifecycleStateEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;Approved&quot; |
| EXPIRED | &quot;Expired&quot; |
| ISSUED | &quot;Issued&quot; |
| PENDING_APPROVAL | &quot;Pending Approval&quot; |
| SUSPENDED | &quot;Suspended&quot; |



