# TwilioFax.FaxV1Fax

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the Account that created the resource | [optional] 
**apiVersion** | **String** | The API version used to transmit the fax | [optional] 
**dateCreated** | **Date** | The ISO 8601 formatted date and time in GMT when the resource was created | [optional] 
**dateUpdated** | **Date** | The ISO 8601 formatted date and time in GMT when the resource was last updated | [optional] 
**direction** | **String** | The direction of the fax | [optional] 
**duration** | **Number** | The time it took to transmit the fax | [optional] 
**from** | **String** | The number the fax was sent from | [optional] 
**links** | **Object** | The URLs of the fax&#39;s related resources | [optional] 
**mediaSid** | **String** | The SID of the FaxMedia resource that is associated with the Fax | [optional] 
**mediaUrl** | **String** | The Twilio-hosted URL that can be used to download fax media | [optional] 
**numPages** | **Number** | The number of pages contained in the fax document | [optional] 
**price** | **Number** | The fax transmission price | [optional] 
**priceUnit** | **String** | The ISO 4217 currency used for billing | [optional] 
**quality** | **String** | The quality of the fax | [optional] 
**sid** | **String** | The unique string that identifies the resource | [optional] 
**status** | **String** | The status of the fax | [optional] 
**to** | **String** | The phone number that received the fax | [optional] 
**url** | **String** | The absolute URL of the fax resource | [optional] 



## Enum: DirectionEnum


* `inbound` (value: `"inbound"`)

* `outbound` (value: `"outbound"`)





## Enum: QualityEnum


* `standard` (value: `"standard"`)

* `fine` (value: `"fine"`)

* `superfine` (value: `"superfine"`)





## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `processing` (value: `"processing"`)

* `sending` (value: `"sending"`)

* `delivered` (value: `"delivered"`)

* `receiving` (value: `"receiving"`)

* `received` (value: `"received"`)

* `no-answer` (value: `"no-answer"`)

* `busy` (value: `"busy"`)

* `failed` (value: `"failed"`)

* `canceled` (value: `"canceled"`)




