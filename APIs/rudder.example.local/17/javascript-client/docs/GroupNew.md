# RudderApi.GroupNew

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Id of the new group&#39;s category | 
**description** | **String** | Group description | [optional] 
**displayName** | **String** | Name of the group | 
**dynamic** | **Boolean** | Should the group be dynamically refreshed (if not, it is a static group) | [optional] [default to true]
**enabled** | **Boolean** | Enable or disable the group | [optional] [default to true]
**id** | **String** | Group id, only provide it when needed. | [optional] 
**properties** | [**[GroupPropertiesInner]**](GroupPropertiesInner.md) | Group properties | [optional] 
**query** | [**GroupNewQuery**](GroupNewQuery.md) |  | [optional] 
**source** | **String** | The id of the group the clone will be based onto. If this parameter if provided,  the new group will be a clone of this source. Other value will override values from the source. | [optional] 


