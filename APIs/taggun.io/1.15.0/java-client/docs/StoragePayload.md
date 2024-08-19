

# StoragePayload


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | **String** |  |  |
|**extractTime** | **Boolean** | Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000. |  [optional] |
|**ignoreMerchantName** | **String** | Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name. |  [optional] |
|**ipAddress** | **String** | IP Address of the end user |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  |  [optional] |
|**md5** | **String** | MD5 hash of the receipt |  |
|**near** | **String** | A geo location to search for merchant. Typically in the format of city, state, country. |  [optional] |
|**referenceId** | **String** | Tag a request with a unique reference ID for feedback and training purposes |  [optional] |
|**refresh** | **Boolean** | Refresh cache if exists |  [optional] |
|**subAccountId** | **String** | Tag a request with sub-account ID for billing purposes |  [optional] |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |
| FR | &quot;fr&quot; |
| JP | &quot;jp&quot; |
| HE | &quot;he&quot; |
| IW | &quot;iw&quot; |
| ET | &quot;et&quot; |
| LV | &quot;lv&quot; |
| LT | &quot;lt&quot; |
| FI | &quot;fi&quot; |
| EL | &quot;el&quot; |
| ZH | &quot;zh&quot; |



