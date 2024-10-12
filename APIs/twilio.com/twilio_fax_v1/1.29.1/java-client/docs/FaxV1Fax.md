

# FaxV1Fax


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the Account that created the resource |  [optional] |
|**apiVersion** | **String** | The API version used to transmit the fax |  [optional] |
|**dateCreated** | **OffsetDateTime** | The ISO 8601 formatted date and time in GMT when the resource was created |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The ISO 8601 formatted date and time in GMT when the resource was last updated |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction of the fax |  [optional] |
|**duration** | **Integer** | The time it took to transmit the fax |  [optional] |
|**from** | **String** | The number the fax was sent from |  [optional] |
|**links** | **Object** | The URLs of the fax&#39;s related resources |  [optional] |
|**mediaSid** | **String** | The SID of the FaxMedia resource that is associated with the Fax |  [optional] |
|**mediaUrl** | **String** | The Twilio-hosted URL that can be used to download fax media |  [optional] |
|**numPages** | **Integer** | The number of pages contained in the fax document |  [optional] |
|**price** | **BigDecimal** | The fax transmission price |  [optional] |
|**priceUnit** | **String** | The ISO 4217 currency used for billing |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) | The quality of the fax |  [optional] |
|**sid** | **String** | The unique string that identifies the resource |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the fax |  [optional] |
|**to** | **String** | The phone number that received the fax |  [optional] |
|**url** | **URI** | The absolute URL of the fax resource |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| FINE | &quot;fine&quot; |
| SUPERFINE | &quot;superfine&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| PROCESSING | &quot;processing&quot; |
| SENDING | &quot;sending&quot; |
| DELIVERED | &quot;delivered&quot; |
| RECEIVING | &quot;receiving&quot; |
| RECEIVED | &quot;received&quot; |
| NO_ANSWER | &quot;no-answer&quot; |
| BUSY | &quot;busy&quot; |
| FAILED | &quot;failed&quot; |
| CANCELED | &quot;canceled&quot; |



