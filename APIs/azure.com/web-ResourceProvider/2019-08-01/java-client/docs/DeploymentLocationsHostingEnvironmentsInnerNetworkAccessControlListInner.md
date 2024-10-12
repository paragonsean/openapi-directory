

# DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner

Network access control entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Action object. |  [optional] |
|**description** | **String** | Description of network access control entry. |  [optional] |
|**order** | **Integer** | Order of precedence. |  [optional] |
|**remoteSubnet** | **String** | Remote subnet. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| PERMIT | &quot;Permit&quot; |
| DENY | &quot;Deny&quot; |



