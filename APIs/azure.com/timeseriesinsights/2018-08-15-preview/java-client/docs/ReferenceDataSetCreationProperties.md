

# ReferenceDataSetCreationProperties

Properties used to create a reference data set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataStringComparisonBehavior** | [**DataStringComparisonBehaviorEnum**](#DataStringComparisonBehaviorEnum) | The reference data set key comparison behavior can be set using this property. By default, the value is &#39;Ordinal&#39; - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When &#39;OrdinalIgnoreCase&#39; is set, case insensitive comparison will be used. |  [optional] |
|**keyProperties** | [**List&lt;ReferenceDataSetKeyProperty&gt;**](ReferenceDataSetKeyProperty.md) | The list of key properties for the reference data set. |  |



## Enum: DataStringComparisonBehaviorEnum

| Name | Value |
|---- | -----|
| ORDINAL | &quot;Ordinal&quot; |
| ORDINAL_IGNORE_CASE | &quot;OrdinalIgnoreCase&quot; |



