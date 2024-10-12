

# PagerDutyNotificationEndpoint


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** | An optional description of the notification endpoint. |  [optional] |
|**id** | **String** |  |  [optional] |
|**labels** | [**List&lt;Label&gt;**](Label.md) |  |  [optional] |
|**links** | [**NotificationEndpointBaseLinks**](NotificationEndpointBaseLinks.md) |  |  [optional] |
|**name** | **String** |  |  |
|**orgID** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the endpoint. |  [optional] |
|**type** | **NotificationEndpointType** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**userID** | **String** |  |  [optional] |
|**clientURL** | **String** |  |  [optional] |
|**routingKey** | **String** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



