# MicrosoftInsights.LogSearchRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | 
**description** | **String** | The description of the Log Search rule. | [optional] 
**enabled** | **String** | The flag which indicates whether the Log Search rule is enabled. Value should be true or false | [optional] 
**lastUpdatedTime** | **Date** | Last time the rule was updated in IS08601 format. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the scheduled query rule | [optional] [readonly] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**source** | [**Source**](Source.md) |  | 



## Enum: EnabledEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Deploying` (value: `"Deploying"`)

* `Canceled` (value: `"Canceled"`)

* `Failed` (value: `"Failed"`)




