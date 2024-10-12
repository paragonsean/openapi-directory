

# UserGroupsListByUsers200ResponseValueInner

Developer group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**builtIn** | **Boolean** | true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false. |  [optional] [readonly] |
|**description** | **String** | Group description. Can contain HTML formatting tags. |  [optional] |
|**externalId** | **String** | For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group object id&gt;; otherwise the value is null. |  [optional] [readonly] |
|**id** | **String** | Uniquely identifies the group within the current API Management service instance. The value is a valid relative URL in the format of /groups/{groupId} where {groupId} is a group identifier. |  [optional] [readonly] |
|**name** | **String** | Group name. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Group type. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;Custom&quot; |
| SYSTEM | &quot;System&quot; |
| EXTERNAL | &quot;External&quot; |



