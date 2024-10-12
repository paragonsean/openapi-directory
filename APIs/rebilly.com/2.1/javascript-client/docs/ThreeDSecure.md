# RebillyRestApi.ThreeDSecure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**amount** | **Number** | Transaction amount. | 
**cavv** | **String** | The 3D Secure entry cardholder authentication verification value. | [optional] 
**createdTime** | **Date** | The 3D Secure entry created time. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | 
**customerId** | **String** | Related customer ID. | 
**eci** | **Number** | The 3D Secure entry electronic commerce indicator. | [optional] 
**enrolled** | **String** | Is the cardholder enrolled in 3DSecure. | 
**enrollmentEci** | **String** | The 3D Secure entry enrollment eci. | 
**gatewayAccountId** | **String** | Related gateway account ID. | 
**id** | **String** | The 3D Secure entry identifier string. | [optional] [readonly] 
**payerAuthResponseStatus** | **String** | The 3D Secure entry Auth Response Status. | [optional] 
**paymentCardId** | **String** | Related payment card ID. | 
**signatureVerification** | **String** | If signature was verified. | [optional] 
**websiteId** | **String** | Related Website ID. | 
**xid** | **String** | The 3D Secure entry transaction Id. | [optional] 



## Enum: EnrolledEnum


* `Y` (value: `"Y"`)

* `N` (value: `"N"`)

* `U` (value: `"U"`)





## Enum: PayerAuthResponseStatusEnum


* `Y` (value: `"Y"`)

* `N` (value: `"N"`)

* `U` (value: `"U"`)

* `A` (value: `"A"`)





## Enum: SignatureVerificationEnum


* `Y` (value: `"Y"`)

* `N` (value: `"N"`)




