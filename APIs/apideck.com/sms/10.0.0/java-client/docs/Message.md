

# Message


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | The message text. |  |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction of the message. |  [optional] [readonly] |
|**error** | [**Error**](Error.md) |  |  [optional] |
|**from** | **String** | The phone number that initiated the message. |  |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**messagingServiceId** | **String** | The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID. |  [optional] |
|**numberOfMediaFiles** | **Integer** | The number of media files associated with the message. |  [optional] [readonly] |
|**numberOfUnits** | **Integer** | The number of units that make up the complete message. Messages can be split up due to the constraints of the message size. |  [optional] [readonly] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**reference** | **String** | A client reference. |  [optional] |
|**scheduledAt** | **OffsetDateTime** | The scheduled date and time of the message. |  [optional] |
|**sentAt** | **OffsetDateTime** | The date and time that the message was sent |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the delivery of the message. |  [optional] [readonly] |
|**subject** | **String** |  |  [optional] |
|**to** | **String** | The phone number that received the message. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Set to sms for SMS messages and mms for MMS messages. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |
|**webhookUrl** | **String** | Define a webhook to receive delivery notifications. |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND_API | &quot;outbound-api&quot; |
| OUTBOUND_CALL | &quot;outbound-call&quot; |
| OUTBOUND_REPLY | &quot;outbound-reply&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| CANCELED | &quot;canceled&quot; |
| QUEUED | &quot;queued&quot; |
| SENDING | &quot;sending&quot; |
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| DELIVERED | &quot;delivered&quot; |
| UNDELIVERED | &quot;undelivered&quot; |
| RECEIVING | &quot;receiving&quot; |
| RECEIVED | &quot;received&quot; |
| READ | &quot;read&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| MMS | &quot;mms&quot; |



