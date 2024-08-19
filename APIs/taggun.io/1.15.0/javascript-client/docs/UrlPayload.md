# TaggunReceiptOcrScanningApi.UrlPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractTime** | **Boolean** | Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000. | [optional] [default to false]
**headers** | [**Headers**](Headers.md) |  | [optional] 
**ignoreMerchantName** | **String** | Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name. | [optional] 
**incognito** | **Boolean** | Set true to avoid saving the receipt in storage | [optional] [default to false]
**ipAddress** | **String** | IP Address of the end user | [optional] 
**language** | **String** | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] 
**near** | **String** | A geo location to search for merchant. Typically in the format of city, state, country. | [optional] 
**referenceId** | **String** | Tag a request with a unique reference ID for feedback and training purposes | [optional] 
**refresh** | **Boolean** | Set true to force re-process image transcription if the receipt is already in storage | [optional] [default to false]
**subAccountId** | **String** | Tag a request with sub-account ID for billing purposes | [optional] 
**url** | **String** | The target URL that contains a receipt file. Only https protocol is accepted. | 



## Enum: LanguageEnum


* `en` (value: `"en"`)

* `es` (value: `"es"`)

* `fr` (value: `"fr"`)

* `jp` (value: `"jp"`)

* `he` (value: `"he"`)

* `iw` (value: `"iw"`)

* `et` (value: `"et"`)

* `lv` (value: `"lv"`)

* `lt` (value: `"lt"`)

* `fi` (value: `"fi"`)

* `el` (value: `"el"`)

* `zh` (value: `"zh"`)




