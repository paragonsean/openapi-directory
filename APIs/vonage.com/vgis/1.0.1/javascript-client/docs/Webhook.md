# VonageIntegrationSuite.Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Unique identifier of the account | [optional] 
**createdAt** | **String** | Created time for the webhook | [optional] 
**events** | **[String]** | Subscribed events for the webhook | [optional] 
**expireAt** | **String** | Expiration time for the webhook | [optional] 
**id** | **String** | Unique identifier for the webhook | [optional] 
**metadataPolicy** | **String** | Metadata policy for the webhook | [optional] 
**purgeAt** | **String** | Scheduled purge time for the webhook | [optional] 
**renewedAt** | **String** | Last renewed time for the webhook | [optional] 
**signingAlgo** | **String** | Signing algorithm for the webhook | [optional] 
**signingKey** | **String** | Signing key for the webhook | [optional] 
**statistics** | [**WebhookStatistics**](WebhookStatistics.md) |  | [optional] 
**status** | **String** | Status for the webhook | [optional] 
**url** | **String** | Destination URL for events | [optional] 
**userId** | **String** | Unique identifier of the user | [optional] 



## Enum: [EventsEnum]


* `CALL` (value: `"CALL"`)





## Enum: MetadataPolicyEnum


* `NONE` (value: `"NONE"`)

* `HEADER` (value: `"HEADER"`)

* `BODY` (value: `"BODY"`)





## Enum: SigningAlgoEnum


* `HMAC_SHA256` (value: `"HMAC_SHA256"`)

* `NONE` (value: `"NONE"`)





## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `PAUSED` (value: `"PAUSED"`)




