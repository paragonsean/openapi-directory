# AmazonConnectCustomerProfiles.CreateCalculatedAttributeDefinitionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The display name of the calculated attribute. | [optional] 
**description** | **String** | The description of the calculated attribute. | [optional] 
**attributeDetails** | [**CreateCalculatedAttributeDefinitionRequestAttributeDetails**](CreateCalculatedAttributeDefinitionRequestAttributeDetails.md) |  | 
**conditions** | [**UpdateCalculatedAttributeDefinitionRequestConditions**](UpdateCalculatedAttributeDefinitionRequestConditions.md) |  | [optional] 
**statistic** | **String** | The aggregation operation to perform for the calculated attribute. | 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. | [optional] 



## Enum: StatisticEnum


* `FIRST_OCCURRENCE` (value: `"FIRST_OCCURRENCE"`)

* `LAST_OCCURRENCE` (value: `"LAST_OCCURRENCE"`)

* `COUNT` (value: `"COUNT"`)

* `SUM` (value: `"SUM"`)

* `MINIMUM` (value: `"MINIMUM"`)

* `MAXIMUM` (value: `"MAXIMUM"`)

* `AVERAGE` (value: `"AVERAGE"`)

* `MAX_OCCURRENCE` (value: `"MAX_OCCURRENCE"`)




