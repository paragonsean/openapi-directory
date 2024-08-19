

# GoogleAnalyticsAdminV1alphaPropertySummary

A virtual resource representing metadata for a GA4 property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Display name for the property referred to in this property summary. |  [optional] |
|**parent** | **String** | Resource name of this property&#39;s logical parent. Note: The Property-Moving UI can be used to change the parent. Format: accounts/{account}, properties/{property} Example: \&quot;accounts/100\&quot;, \&quot;properties/200\&quot; |  [optional] |
|**property** | **String** | Resource name of property referred to by this property summary Format: properties/{property_id} Example: \&quot;properties/1000\&quot; |  [optional] |
|**propertyType** | [**PropertyTypeEnum**](#PropertyTypeEnum) | The property&#39;s property type. |  [optional] |



## Enum: PropertyTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROPERTY_TYPE_UNSPECIFIED&quot; |
| ORDINARY | &quot;PROPERTY_TYPE_ORDINARY&quot; |
| SUBPROPERTY | &quot;PROPERTY_TYPE_SUBPROPERTY&quot; |
| ROLLUP | &quot;PROPERTY_TYPE_ROLLUP&quot; |



