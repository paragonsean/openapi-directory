# NaviPlanApi.IAssumptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anyHeadAlreadyRetired** | **Boolean** |  | [optional] [readonly] 
**bothRetired** | **Boolean** |  | [optional] [readonly] 
**bucketing** | [**IBucketing**](IBucketing.md) |  | [optional] 
**client** | [**IHeadAssumptions**](IHeadAssumptions.md) |  | [optional] 
**coClient** | [**IHeadAssumptions**](IHeadAssumptions.md) |  | [optional] 
**firstToDieDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**firstToDieMember** | **String** |  | [optional] [readonly] 
**firstToRetireDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**inflationRate** | [**Percent**](Percent.md) |  | [optional] 
**lastToDieDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**lastToDieMember** | **String** |  | [optional] [readonly] 
**lastToRetireDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**retirementYearAdjustedIfAlreadyRetired** | [**Year**](Year.md) |  | [optional] 
**splitSurplusSavingsStrategiesEnabled** | **Boolean** |  | [optional] [readonly] 
**taxMethod** | **String** |  | [optional] [readonly] 



## Enum: FirstToDieMemberEnum


* `Client` (value: `"Client"`)

* `CoClient` (value: `"CoClient"`)





## Enum: LastToDieMemberEnum


* `Client` (value: `"Client"`)

* `CoClient` (value: `"CoClient"`)





## Enum: TaxMethodEnum


* `Average` (value: `"Average"`)

* `Simplified` (value: `"Simplified"`)

* `Detailed` (value: `"Detailed"`)




