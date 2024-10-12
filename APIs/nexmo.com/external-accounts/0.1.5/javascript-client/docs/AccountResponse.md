# ExternalAccountsApi.AccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The provider access token (only for &#x60;messenger&#x60;) | [optional] 
**apiKey** | **String** | The external api key for this account | 
**applications** | **[String]** | The array of associated application ids | [optional] 
**externalId** | **String** | The external identifier for this account | 
**name** | **String** | The account name | [optional] 
**provider** | **String** | The provider (will be one of &#x60;messenger, viber_service_msg, whatsapp&#x60;). | 



## Enum: ProviderEnum


* `messenger` (value: `"messenger"`)

* `viber_service_msg` (value: `"viber_service_msg"`)

* `whatsapp` (value: `"whatsapp"`)




