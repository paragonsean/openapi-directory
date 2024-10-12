# NumberInsightApi.NiResponseXmlAdvancedCallerIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callerName** | **String** | Full name of the person or business who owns the phone number. &#x60;unknown&#x60; if this information is not available. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. | [optional] 
**callerType** | **String** | The value will be &#x60;business&#x60; if the owner of a phone number is a business. If the owner is an individual the value will be &#x60;consumer&#x60;. The value will be &#x60;unknown&#x60; if this information is not available. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. | [optional] 
**firstName** | **String** | First name of the person who owns the phone number if the owner is an individual. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. | [optional] 
**lastName** | **String** | Last name of the person who owns the phone number if the owner is an individual. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. | [optional] 



## Enum: CallerTypeEnum


* `business` (value: `"business"`)

* `consumer` (value: `"consumer"`)

* `unknown` (value: `"unknown"`)




