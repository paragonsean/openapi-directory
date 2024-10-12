

# SlackNotificationEndpoint


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
|**token** | **String** | Specifies the API token string. Specify either &#x60;URL&#x60; or &#x60;Token&#x60;. |  [optional] |
|**url** | **String** | Specifies the URL of the Slack endpoint. Specify either &#x60;URL&#x60; or &#x60;Token&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



