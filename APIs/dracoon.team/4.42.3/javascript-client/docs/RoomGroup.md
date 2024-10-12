# DracoonApi.RoomGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** | Unique identifier for the group | 
**isGranted** | **Boolean** | Is user granted room permissions | 
**name** | **String** | Group name | 
**newGroupMemberAcceptance** | **String** | Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items. | [optional] [default to &#39;autoallow&#39;]
**permissions** | [**NodePermissions**](NodePermissions.md) |  | [optional] 



## Enum: NewGroupMemberAcceptanceEnum


* `autoallow` (value: `"autoallow"`)

* `pending` (value: `"pending"`)




