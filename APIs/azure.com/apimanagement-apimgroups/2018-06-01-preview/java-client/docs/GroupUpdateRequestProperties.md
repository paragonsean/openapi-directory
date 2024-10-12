

# GroupUpdateRequestProperties

Parameters supplied to the Update Group operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Group description. |  [optional] |
|**displayName** | **String** | Group name. |  [optional] |
|**externalId** | **String** | Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory &#x60;aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group object id&gt;&#x60;; otherwise the value is null. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Group type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |
| SYSTEM | &quot;system&quot; |
| EXTERNAL | &quot;external&quot; |



