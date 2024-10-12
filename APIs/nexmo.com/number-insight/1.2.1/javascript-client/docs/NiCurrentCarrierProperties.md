# NumberInsightApi.NiCurrentCarrierProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The country that &#x60;number&#x60; is associated with. This is in ISO 3166-1 alpha-2   format. | [optional] 
**name** | **String** | The full name of the carrier that &#x60;number&#x60; is associated with. | [optional] 
**networkCode** | **String** | The [https://en.wikipedia.org/wiki/Mobile_country_code](https://en.wikipedia.org/wiki/Mobile_country_code) for the carrier&#x60;number&#x60; is associated with. Unreal numbers are marked as&#x60;null&#x60; and the request is rejected altogether if the number is impossible according to the [E.164](https://en.wikipedia.org/wiki/E.164) guidelines. | [optional] 
**networkType** | **String** | The type of network that &#x60;number&#x60; is associated with. | [optional] 



## Enum: NetworkTypeEnum


* `mobile` (value: `"mobile"`)

* `landline` (value: `"landline"`)

* `landline_premium` (value: `"landline_premium"`)

* `landline_tollfree` (value: `"landline_tollfree"`)

* `virtual` (value: `"virtual"`)

* `unknown` (value: `"unknown"`)

* `pager` (value: `"pager"`)

* `null` (value: `"null"`)




