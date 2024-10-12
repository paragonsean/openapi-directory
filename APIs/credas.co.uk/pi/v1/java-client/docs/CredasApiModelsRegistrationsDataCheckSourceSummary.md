

# CredasApiModelsRegistrationsDataCheckSourceSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**CredasApiModelsDataCheckAddress**](CredasApiModelsDataCheckAddress.md) |  |  [optional] |
|**dateCreated** | **OffsetDateTime** |  |  [optional] |
|**hasBeenOverridden** | **Boolean** |  |  [optional] |
|**hasPepSanctionsData** | **Boolean** |  |  [optional] [readonly] |
|**label** | **String** |  |  [optional] |
|**pepSanctionsData** | [**List&lt;CredasApiModelsDataCheckPepSanctionsPepSanctionItem&gt;**](CredasApiModelsDataCheckPepSanctionsPepSanctionItem.md) |  |  [optional] |
|**person** | [**CredasApiModelsDataCheckPerson**](CredasApiModelsDataCheckPerson.md) |  |  [optional] |
|**remarks** | [**List&lt;CredasApiModelsDataCheckCheckRemark&gt;**](CredasApiModelsDataCheckCheckRemark.md) |  |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Unknown &#x3D; 0, EditedElectoralRollUk &#x3D; 1, LandlineAppendUk &#x3D; 2, MortalityUk &#x3D; 3, CreaditHeaderAmlUk &#x3D; 4, NcoaAlertFlagUk &#x3D; 5, NcoaAlertFullUk &#x3D; 6, SanctionsEnhancedInternational &#x3D; 7, PepEnhancedInternational &#x3D; 8, NationalIdentityRegisterUk &#x3D; 9, LandRegistry &#x3D; 10 |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_8 | 8 |
| NUMBER_9 | 9 |
| NUMBER_10 | 10 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



