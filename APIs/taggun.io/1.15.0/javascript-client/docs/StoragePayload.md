# TaggunReceiptOcrScanningApi.StoragePayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** |  | 
**extractTime** | **Boolean** | Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000. | [optional] [default to false]
**ignoreMerchantName** | **String** | Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name. | [optional] 
**ipAddress** | **String** | IP Address of the end user | [optional] 
**language** | **String** | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] 
**md5** | **String** | MD5 hash of the receipt | 
**near** | **String** | A geo location to search for merchant. Typically in the format of city, state, country. | [optional] 
**referenceId** | **String** | Tag a request with a unique reference ID for feedback and training purposes | [optional] 
**refresh** | **Boolean** | Refresh cache if exists | [optional] [default to false]
**subAccountId** | **String** | Tag a request with sub-account ID for billing purposes | [optional] 



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




