

# PlanInformationModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] [readonly] |
|**isJointAnalysis** | **Boolean** |  |  [optional] [readonly] |
|**links** | [**List&lt;ObjectLink&gt;**](ObjectLink.md) |  |  [optional] |
|**locale** | **String** |  |  [optional] [readonly] |
|**planDate** | [**Date**](Date.md) |  |  [optional] |
|**planDescription** | **String** |  |  [optional] [readonly] |
|**planId** | **String** |  |  [optional] [readonly] |
|**planLevel** | [**PlanLevelEnum**](#PlanLevelEnum) |  |  [optional] [readonly] |
|**planModules** | [**IPlanModules**](IPlanModules.md) |  |  [optional] |
|**planType** | **String** |  |  [optional] [readonly] |
|**publishDate** | [**Date**](Date.md) |  |  [optional] |



## Enum: PlanLevelEnum

| Name | Value |
|---- | -----|
| CALCULATOR | &quot;Calculator&quot; |
| FINANCIAL_ASSESSMENT | &quot;FinancialAssessment&quot; |
| ASSET_ALLOCATION | &quot;AssetAllocation&quot; |
| LEVEL1 | &quot;Level1&quot; |
| LEVEL2 | &quot;Level2&quot; |
| LEVEL3 | &quot;Level3&quot; |
| UNDEFINED | &quot;Undefined&quot; |



