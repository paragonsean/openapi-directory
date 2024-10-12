# TimeSeriesInsightsClient.ReferenceDataSetResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataStringComparisonBehavior** | **String** | The reference data set key comparison behavior can be set using this property. By default, the value is &#39;Ordinal&#39; - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When &#39;OrdinalIgnoreCase&#39; is set, case insensitive comparison will be used. | [optional] 
**keyProperties** | [**[ReferenceDataSetKeyProperty]**](ReferenceDataSetKeyProperty.md) | The list of key properties for the reference data set. | 
**creationTime** | **Date** | The time the resource was created. | [optional] [readonly] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 



## Enum: DataStringComparisonBehaviorEnum


* `Ordinal` (value: `"Ordinal"`)

* `OrdinalIgnoreCase` (value: `"OrdinalIgnoreCase"`)




