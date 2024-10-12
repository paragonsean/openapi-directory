

# CredasApiModelsStatusChecksStatusCheck


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**CredasApiModelsDataCheckAddress**](CredasApiModelsDataCheckAddress.md) |  |  [optional] |
|**ccj** | [**List&lt;CredasApiModelsStatusChecksCCJCcjResult&gt;**](CredasApiModelsStatusChecksCCJCcjResult.md) |  |  [optional] |
|**checkDate** | **OffsetDateTime** |  |  [optional] |
|**companyDirector** | [**List&lt;CredasApiModelsStatusChecksCompanyDirectorCompanyDirectorResult&gt;**](CredasApiModelsStatusChecksCompanyDirectorCompanyDirectorResult.md) |  |  [optional] |
|**hasBeenOverridden** | **Boolean** |  |  [optional] |
|**insolvency** | [**List&lt;CredasApiModelsStatusChecksInsolvencyInsolvencyResult&gt;**](CredasApiModelsStatusChecksInsolvencyInsolvencyResult.md) |  |  [optional] |
|**person** | [**CredasApiModelsDataCheckPerson**](CredasApiModelsDataCheckPerson.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



