# NetBoxApi.ObjectPermission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **[String]** | The list of actions granted by this permission | 
**constraints** | **Object** | Queryset filter matching the applicable objects of the selected type(s) | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**enabled** | **Boolean** |  | [optional] 
**groups** | [**[NestedGroup]**](NestedGroup.md) |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**name** | **String** |  | 
**objectTypes** | **[String]** |  | 
**url** | **String** |  | [optional] [readonly] 
**users** | [**[NestedUser]**](NestedUser.md) |  | [optional] 


