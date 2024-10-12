# CredasApi.CredasApiModelsBankAccountsAccountVerificationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **String** |  | [optional] 
**city** | **String** |  | [optional] 
**forename** | **String** |  | [optional] 
**middleName** | **String** |  | [optional] 
**postCode** | **String** |  | [optional] 
**surname** | **String** |  | [optional] 
**accountNumber** | **String** |  | [optional] 
**accountNumberValidation** | **Number** | Unknown &#x3D; 0, NoMatch &#x3D; 1, Valid &#x3D; 2, Invalid &#x3D; 3, SevenDigitsMatched &#x3D; 4, SixDigitsMatched &#x3D; 5 | [optional] 
**accountNumberValidationText** | **String** |  | [optional] [readonly] 
**accountStatus** | **Number** | Unknown &#x3D; 0, NoMatch &#x3D; 1, Live &#x3D; 2, ClosedOrSettled &#x3D; 3 | [optional] 
**accountStatusText** | **String** |  | [optional] [readonly] 
**accountValid** | **Boolean** |  | [optional] 
**addressValidation** | **Number** | Unknown &#x3D; 0, NoMatch &#x3D; 1, CurrentAddress &#x3D; 2, PreviousAddress &#x3D; 3, ForwardingAddress &#x3D; 4 | [optional] 
**addressValidationText** | **String** |  | [optional] [readonly] 
**checkDate** | **Date** |  | [optional] 
**checkId** | **String** |  | [optional] 
**checkStatus** | **Number** | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 | [optional] 
**error** | **Boolean** |  | [optional] 
**hasBeenOverridden** | **Boolean** |  | [optional] 
**nameValidation** | **Number** | Unknown &#x3D; 0, NoMatch &#x3D; 1, Valid &#x3D; 2 | [optional] 
**nameValidationText** | **String** |  | [optional] [readonly] 
**referenceId** | **String** |  | [optional] 
**sortcode** | **String** |  | [optional] 
**sortcodeValidation** | **Number** | Unknown &#x3D; 0, NoMatch &#x3D; 1, Valid &#x3D; 2, Invalid &#x3D; 3, FiveDigitsMatched &#x3D; 4 | [optional] 
**sortcodeValidationText** | **String** |  | [optional] [readonly] 



## Enum: AccountNumberValidationEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)





## Enum: AccountStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)





## Enum: AddressValidationEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)





## Enum: CheckStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)





## Enum: NameValidationEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: SortcodeValidationEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)




