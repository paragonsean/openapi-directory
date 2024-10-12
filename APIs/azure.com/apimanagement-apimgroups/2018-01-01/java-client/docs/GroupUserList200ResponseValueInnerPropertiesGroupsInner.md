

# GroupUserList200ResponseValueInnerPropertiesGroupsInner

Group contract Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**builtIn** | **Boolean** | true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false. |  [optional] [readonly] |
|**description** | **String** | Group description. Can contain HTML formatting tags. |  [optional] |
|**displayName** | **String** | Group name. |  |
|**externalId** | **String** | For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group object id&gt;; otherwise the value is null. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Group type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |
| SYSTEM | &quot;system&quot; |
| EXTERNAL | &quot;external&quot; |



