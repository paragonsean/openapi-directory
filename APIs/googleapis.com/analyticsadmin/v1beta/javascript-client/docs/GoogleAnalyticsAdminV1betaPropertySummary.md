# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1betaPropertySummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Display name for the property referred to in this property summary. | [optional] 
**parent** | **String** | Resource name of this property&#39;s logical parent. Note: The Property-Moving UI can be used to change the parent. Format: accounts/{account}, properties/{property} Example: \&quot;accounts/100\&quot;, \&quot;properties/200\&quot; | [optional] 
**property** | **String** | Resource name of property referred to by this property summary Format: properties/{property_id} Example: \&quot;properties/1000\&quot; | [optional] 
**propertyType** | **String** | The property&#39;s property type. | [optional] 



## Enum: PropertyTypeEnum


* `UNSPECIFIED` (value: `"PROPERTY_TYPE_UNSPECIFIED"`)

* `ORDINARY` (value: `"PROPERTY_TYPE_ORDINARY"`)

* `SUBPROPERTY` (value: `"PROPERTY_TYPE_SUBPROPERTY"`)

* `ROLLUP` (value: `"PROPERTY_TYPE_ROLLUP"`)




