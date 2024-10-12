# RedactApi.RedactTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The transaction ID to redact | 
**product** | **String** | Product name that the ID provided relates to | 
**type** | **String** | Required if redacting SMS data | [default to &#39;outbound&#39;]



## Enum: ProductEnum


* `sms` (value: `"sms"`)

* `voice` (value: `"voice"`)

* `number-insight` (value: `"number-insight"`)

* `verify` (value: `"verify"`)

* `verify-sdk` (value: `"verify-sdk"`)

* `messages` (value: `"messages"`)





## Enum: TypeEnum


* `inbound` (value: `"inbound"`)

* `outbound` (value: `"outbound"`)




