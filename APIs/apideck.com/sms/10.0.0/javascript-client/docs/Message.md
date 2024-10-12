# SmsApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | The message text. | 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**direction** | **String** | The direction of the message. | [optional] [readonly] 
**error** | [**Error**](Error.md) |  | [optional] 
**from** | **String** | The phone number that initiated the message. | 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**messagingServiceId** | **String** | The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID. | [optional] 
**numberOfMediaFiles** | **Number** | The number of media files associated with the message. | [optional] [readonly] 
**numberOfUnits** | **Number** | The number of units that make up the complete message. Messages can be split up due to the constraints of the message size. | [optional] [readonly] 
**price** | [**Price**](Price.md) |  | [optional] 
**reference** | **String** | A client reference. | [optional] 
**scheduledAt** | **Date** | The scheduled date and time of the message. | [optional] 
**sentAt** | **Date** | The date and time that the message was sent | [optional] [readonly] 
**status** | **String** | Status of the delivery of the message. | [optional] [readonly] 
**subject** | **String** |  | [optional] 
**to** | **String** | The phone number that received the message. | 
**type** | **String** | Set to sms for SMS messages and mms for MMS messages. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 
**webhookUrl** | **String** | Define a webhook to receive delivery notifications. | [optional] 



## Enum: DirectionEnum


* `inbound` (value: `"inbound"`)

* `outbound-api` (value: `"outbound-api"`)

* `outbound-call` (value: `"outbound-call"`)

* `outbound-reply` (value: `"outbound-reply"`)

* `unknown` (value: `"unknown"`)





## Enum: StatusEnum


* `accepted` (value: `"accepted"`)

* `scheduled` (value: `"scheduled"`)

* `canceled` (value: `"canceled"`)

* `queued` (value: `"queued"`)

* `sending` (value: `"sending"`)

* `sent` (value: `"sent"`)

* `failed` (value: `"failed"`)

* `delivered` (value: `"delivered"`)

* `undelivered` (value: `"undelivered"`)

* `receiving` (value: `"receiving"`)

* `received` (value: `"received"`)

* `read` (value: `"read"`)





## Enum: TypeEnum


* `sms` (value: `"sms"`)

* `mms` (value: `"mms"`)




