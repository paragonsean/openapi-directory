# ApiISendPro.SubaccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyid** | **String** | Clé API | 
**subAccountAddCredit** | **String** | montant du crédit à ajouter | [optional] 
**subAccountCountryCode** | **String** |  | [optional] 
**subAccountEdit** | **String** | action à réaliser soit setPrice pour définir un prix ou addCredit pour ajouter du credit ou setRestriction modifier la restriction stop / | 
**subAccountKeyId** | **String** | keyid du sous-compte | [optional] 
**subAccountPrice** | **String** |  | [optional] 
**subAccountRestrictionStop** | **String** |  | [optional] 
**subAccountRestrictionTime** | **String** |  | [optional] 



## Enum: SubAccountEditEnum


* `setPrice` (value: `"setPrice"`)

* `addCredit` (value: `"addCredit"`)

* `setRestriction` (value: `"setRestriction"`)





## Enum: SubAccountRestrictionStopEnum


* `0` (value: `"0"`)

* `1` (value: `"1"`)





## Enum: SubAccountRestrictionTimeEnum


* `0` (value: `"0"`)

* `1` (value: `"1"`)




