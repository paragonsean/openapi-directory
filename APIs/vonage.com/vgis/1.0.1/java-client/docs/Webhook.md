

# Webhook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Unique identifier of the account |  [optional] |
|**createdAt** | **String** | Created time for the webhook |  [optional] |
|**events** | [**List&lt;EventsEnum&gt;**](#List&lt;EventsEnum&gt;) | Subscribed events for the webhook |  [optional] |
|**expireAt** | **String** | Expiration time for the webhook |  [optional] |
|**id** | **String** | Unique identifier for the webhook |  [optional] |
|**metadataPolicy** | [**MetadataPolicyEnum**](#MetadataPolicyEnum) | Metadata policy for the webhook |  [optional] |
|**purgeAt** | **String** | Scheduled purge time for the webhook |  [optional] |
|**renewedAt** | **String** | Last renewed time for the webhook |  [optional] |
|**signingAlgo** | [**SigningAlgoEnum**](#SigningAlgoEnum) | Signing algorithm for the webhook |  [optional] |
|**signingKey** | **String** | Signing key for the webhook |  [optional] |
|**statistics** | [**WebhookStatistics**](WebhookStatistics.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status for the webhook |  [optional] |
|**url** | **String** | Destination URL for events |  [optional] |
|**userId** | **String** | Unique identifier of the user |  [optional] |



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
| NONE | &quot;NONE&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |



