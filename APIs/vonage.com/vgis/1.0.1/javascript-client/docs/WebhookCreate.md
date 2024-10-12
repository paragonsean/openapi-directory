# VonageIntegrationSuite.WebhookCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **[String]** | Events to subscribe to the webhook | [optional] 
**metadataPolicy** | **String** | Metadata policy for the webhook | [optional] 
**signingAlgo** | **String** | Signing algorithm for the webhook | [optional] 
**signingKey** | **String** | Signing key for the webhook | [optional] 
**url** | **String** | Destination URL for events | [optional] 



## Enum: [EventsEnum]


* `CALL` (value: `"CALL"`)





## Enum: MetadataPolicyEnum


* `NONE` (value: `"NONE"`)

* `HEADER` (value: `"HEADER"`)

* `BODY` (value: `"BODY"`)





## Enum: SigningAlgoEnum


* `HMAC_SHA256` (value: `"HMAC_SHA256"`)




