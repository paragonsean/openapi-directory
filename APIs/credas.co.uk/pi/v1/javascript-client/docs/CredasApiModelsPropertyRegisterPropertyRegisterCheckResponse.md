# CredasApi.CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkStatus** | **Number** | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 | [optional] 
**hasBeenOverridden** | **Boolean** |  | [optional] 
**matchResult** | **Number** | Unknown &#x3D; 0, FullNameMatch &#x3D; 1, SurnameMatch &#x3D; 2, NoNameMatch &#x3D; 3, NoAddressMatch &#x3D; 4, TitleNotRegistered &#x3D; 5, Unavailable &#x3D; 6, OutOfHours &#x3D; 7 | [optional] 
**matchResultText** | **String** |  | [optional] 
**propertyOwnership** | **Number** | Unknown &#x3D; 0, SoleOwnership &#x3D; 1, JointOwnership &#x3D; 2 | [optional] 
**propertyOwnershipText** | **String** |  | [optional] 
**titleNumber** | **String** |  | [optional] 



## Enum: CheckStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)





## Enum: MatchResultEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)





## Enum: PropertyOwnershipEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)




