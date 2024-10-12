# CredasApi.CredasApiModelsRegistrationsDataCheckSourceSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CredasApiModelsDataCheckAddress**](CredasApiModelsDataCheckAddress.md) |  | [optional] 
**dateCreated** | **Date** |  | [optional] 
**hasBeenOverridden** | **Boolean** |  | [optional] 
**hasPepSanctionsData** | **Boolean** |  | [optional] [readonly] 
**label** | **String** |  | [optional] 
**pepSanctionsData** | [**[CredasApiModelsDataCheckPepSanctionsPepSanctionItem]**](CredasApiModelsDataCheckPepSanctionsPepSanctionItem.md) |  | [optional] 
**person** | [**CredasApiModelsDataCheckPerson**](CredasApiModelsDataCheckPerson.md) |  | [optional] 
**remarks** | [**[CredasApiModelsDataCheckCheckRemark]**](CredasApiModelsDataCheckCheckRemark.md) |  | [optional] 
**sourceType** | **Number** | Unknown &#x3D; 0, EditedElectoralRollUk &#x3D; 1, LandlineAppendUk &#x3D; 2, MortalityUk &#x3D; 3, CreaditHeaderAmlUk &#x3D; 4, NcoaAlertFlagUk &#x3D; 5, NcoaAlertFullUk &#x3D; 6, SanctionsEnhancedInternational &#x3D; 7, PepEnhancedInternational &#x3D; 8, NationalIdentityRegisterUk &#x3D; 9, LandRegistry &#x3D; 10 | [optional] 
**status** | **Number** | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 | [optional] 



## Enum: SourceTypeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `8` (value: `8`)

* `9` (value: `9`)

* `10` (value: `10`)





## Enum: StatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)




