

# WebhookCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**events** | [**List&lt;EventsEnum&gt;**](#List&lt;EventsEnum&gt;) | Events to subscribe to the webhook |  [optional] |
|**metadataPolicy** | [**MetadataPolicyEnum**](#MetadataPolicyEnum) | Metadata policy for the webhook |  [optional] |
|**signingAlgo** | [**SigningAlgoEnum**](#SigningAlgoEnum) | Signing algorithm for the webhook |  [optional] |
|**signingKey** | **String** | Signing key for the webhook |  [optional] |
|**url** | **String** | Destination URL for events |  [optional] |



## Enum: List&lt;EventsEnum&gt;

| Name | Value |
|---- | -----|
| CALL | &quot;CALL&quot; |



## Enum: MetadataPolicyEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| HEADER | &quot;HEADER&quot; |
| BODY | &quot;BODY&quot; |



## Enum: SigningAlgoEnum

| Name | Value |
|---- | -----|
| HMAC_SHA256 | &quot;HMAC_SHA256&quot; |



