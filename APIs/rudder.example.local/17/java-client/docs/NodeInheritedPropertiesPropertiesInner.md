

# NodeInheritedPropertiesPropertiesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hierarchy** | [**List&lt;NodeInheritedPropertiesPropertiesInnerHierarchyInner&gt;**](NodeInheritedPropertiesPropertiesInnerHierarchyInner.md) | A description of the inheritance hierarchy for that property, with most direct parent at head and oldest one at tail |  [optional] |
|**name** | **String** | Property name |  |
|**origval** | **Object** | The original value (ie, before overriding and inheritance resolution) for that node |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | Property provider (if the property is not a simple node property) |  [optional] |
|**value** | **Object** | Resolved (ie, with inheritance and overriding done) property value (can be a string or JSON object) |  |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| INHERITED | &quot;inherited&quot; |
| OVERRIDDEN | &quot;overridden&quot; |
| PLUGIN_NAME_LIKE_DATASOURCES | &quot;plugin name like datasources&quot; |



