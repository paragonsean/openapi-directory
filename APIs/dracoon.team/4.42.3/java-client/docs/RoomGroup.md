

# RoomGroup

Group information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Long** | Unique identifier for the group |  |
|**isGranted** | **Boolean** | Is user granted room permissions |  |
|**name** | **String** | Group name |  |
|**newGroupMemberAcceptance** | [**NewGroupMemberAcceptanceEnum**](#NewGroupMemberAcceptanceEnum) | Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items. |  [optional] |
|**permissions** | [**NodePermissions**](NodePermissions.md) |  |  [optional] |



## Enum: NewGroupMemberAcceptanceEnum

| Name | Value |
|---- | -----|
| AUTOALLOW | &quot;autoallow&quot; |
| PENDING | &quot;pending&quot; |



