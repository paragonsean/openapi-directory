# RudderApi.NodeInheritedPropertiesPropertiesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchy** | [**[NodeInheritedPropertiesPropertiesInnerHierarchyInner]**](NodeInheritedPropertiesPropertiesInnerHierarchyInner.md) | A description of the inheritance hierarchy for that property, with most direct parent at head and oldest one at tail | [optional] 
**name** | **String** | Property name | 
**origval** | **Object** | The original value (ie, before overriding and inheritance resolution) for that node | [optional] 
**provider** | **String** | Property provider (if the property is not a simple node property) | [optional] 
**value** | **Object** | Resolved (ie, with inheritance and overriding done) property value (can be a string or JSON object) | 



## Enum: ProviderEnum


* `inherited` (value: `"inherited"`)

* `overridden` (value: `"overridden"`)

* `plugin name like datasources` (value: `"plugin name like datasources"`)




