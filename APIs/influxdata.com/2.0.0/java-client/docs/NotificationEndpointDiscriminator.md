

# NotificationEndpointDiscriminator


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
|**token** | **String** | Specifies the Telegram bot token. See https://core.telegram.org/bots#creating-a-new-bot . |  |
|**url** | **String** |  |  |
|**clientURL** | **String** |  |  [optional] |
|**routingKey** | **String** |  |  |
|**authMethod** | [**AuthMethodEnum**](#AuthMethodEnum) |  |  |
|**contentTemplate** | **String** |  |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Customized headers. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  |
|**password** | **String** |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**channel** | **String** | ID of the telegram channel, a chat_id in https://core.telegram.org/bots/api#sendmessage . |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



## Enum: AuthMethodEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| BASIC | &quot;basic&quot; |
| BEARER | &quot;bearer&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| POST | &quot;POST&quot; |
| GET | &quot;GET&quot; |
| PUT | &quot;PUT&quot; |



