# RebillyRestApi.ThreeDSecureResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **String** | 3D Secure authentication response status. | 
**enrolled** | **String** | Is the cardholder enrolled in 3D Secure. | 
**flow** | **String** | 3D Secure 2 authentication flow. | [optional] 
**isDowngraded** | **Boolean** | If 3D Secure 2 was attempted but downgraded to 3D Secure 1. | [default to false]
**liability** | **String** |  | 
**version** | **String** | 3D Secure version. | [optional] 



## Enum: AuthenticatedEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)

* `not applicable` (value: `"not applicable"`)

* `attempted` (value: `"attempted"`)





## Enum: EnrolledEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)

* `invalid card/timeout` (value: `"invalid card/timeout"`)

* `unavailable` (value: `"unavailable"`)





## Enum: FlowEnum


* `frictionless` (value: `"frictionless"`)

* `challenge` (value: `"challenge"`)





## Enum: LiabilityEnum


* `protected` (value: `"protected"`)

* `not protected` (value: `"not protected"`)

* `protected (attempt)` (value: `"protected (attempt)"`)





## Enum: VersionEnum


* `1.0.2` (value: `"1.0.2"`)

* `2.1.0` (value: `"2.1.0"`)

* `2.2.0` (value: `"2.2.0"`)




