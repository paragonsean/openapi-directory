# CloudHealthcareApi.SchemaGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choice** | **Boolean** | True indicates that this is a choice group, meaning that only one of its segments can exist in a given message. | [optional] 
**maxOccurs** | **Number** | The maximum number of times this group can be repeated. 0 or -1 means unbounded. | [optional] 
**members** | [**[GroupOrSegment]**](GroupOrSegment.md) | Nested groups and/or segments. | [optional] 
**minOccurs** | **Number** | The minimum number of times this group must be present/repeated. | [optional] 
**name** | **String** | The name of this group. For example, \&quot;ORDER_DETAIL\&quot;. | [optional] 


