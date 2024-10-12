

# IAssumptions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**anyHeadAlreadyRetired** | **Boolean** |  |  [optional] [readonly] |
|**bothRetired** | **Boolean** |  |  [optional] [readonly] |
|**bucketing** | [**IBucketing**](IBucketing.md) |  |  [optional] |
|**client** | [**IHeadAssumptions**](IHeadAssumptions.md) |  |  [optional] |
|**coClient** | [**IHeadAssumptions**](IHeadAssumptions.md) |  |  [optional] |
|**firstToDieDate** | [**Date**](Date.md) |  |  [optional] |
|**firstToDieMember** | [**FirstToDieMemberEnum**](#FirstToDieMemberEnum) |  |  [optional] [readonly] |
|**firstToRetireDate** | [**Date**](Date.md) |  |  [optional] |
|**inflationRate** | [**Percent**](Percent.md) |  |  [optional] |
|**lastToDieDate** | [**Date**](Date.md) |  |  [optional] |
|**lastToDieMember** | [**LastToDieMemberEnum**](#LastToDieMemberEnum) |  |  [optional] [readonly] |
|**lastToRetireDate** | [**Date**](Date.md) |  |  [optional] |
|**retirementYearAdjustedIfAlreadyRetired** | [**Year**](Year.md) |  |  [optional] |
|**splitSurplusSavingsStrategiesEnabled** | **Boolean** |  |  [optional] [readonly] |
|**taxMethod** | [**TaxMethodEnum**](#TaxMethodEnum) |  |  [optional] [readonly] |



## Enum: FirstToDieMemberEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |



## Enum: LastToDieMemberEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |



## Enum: TaxMethodEnum

| Name | Value |
|---- | -----|
| AVERAGE | &quot;Average&quot; |
| SIMPLIFIED | &quot;Simplified&quot; |
| DETAILED | &quot;Detailed&quot; |



