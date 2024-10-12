# DracoonApi.UpdateCustomerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companyName** | **String** | Company name | [optional] 
**customerContractType** | **String** | Customer type | 
**isLocked** | **Boolean** | Customer is locked:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    All users of this customer will be blocked and can not login anymore. | [optional] [default to false]
**lockStatus** | **Boolean** | &amp;#128679; Deprecated since v4.7.0  Customer lock status:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    Please use &#x60;isLocked&#x60; instead.  All users of this customer will be blocked and can not login anymore. | [optional] [default to false]
**providerCustomerId** | **String** | Provider customer ID | [optional] 
**quotaMax** | **Number** | Maximal disc space which can be allocated by customer in bytes. -1 for unlimited | [optional] 
**userMax** | **Number** | Maximal number of users | [optional] 
**webhooksMax** | **Number** | &amp;#128640; Since v4.19.0  Maximal number of webhooks | [optional] 



## Enum: CustomerContractTypeEnum


* `demo` (value: `"demo"`)

* `free` (value: `"free"`)

* `pay` (value: `"pay"`)




