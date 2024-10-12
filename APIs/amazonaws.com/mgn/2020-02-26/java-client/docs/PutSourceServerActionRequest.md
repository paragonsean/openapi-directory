

# PutSourceServerActionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountID** | **String** | Source server post migration custom account ID. |  [optional] |
|**actionID** | **String** | Source server post migration custom action ID. |  |
|**actionName** | **String** | Source server post migration custom action name. |  |
|**active** | **Boolean** | Source server post migration custom action active status. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Source server post migration custom action category. |  [optional] |
|**description** | **String** | Source server post migration custom action description. |  [optional] |
|**documentIdentifier** | **String** | Source server post migration custom action document identifier. |  |
|**documentVersion** | **String** | Source server post migration custom action document version. |  [optional] |
|**externalParameters** | [**Map&lt;String, SsmExternalParameter&gt;**](SsmExternalParameter.md) | Source server post migration custom action external parameters. |  [optional] |
|**mustSucceedForCutover** | **Boolean** | Source server post migration custom action must succeed for cutover. |  [optional] |
|**order** | **Integer** | Source server post migration custom action order. |  |
|**parameters** | **Map&lt;String, List&lt;SsmParameterStoreParameter&gt;&gt;** | Source server post migration custom action parameters. |  [optional] |
|**sourceServerID** | **String** | Source server ID. |  |
|**timeoutSeconds** | **Integer** | Source server post migration custom action timeout in seconds. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| DISASTER_RECOVERY | &quot;DISASTER_RECOVERY&quot; |
| OPERATING_SYSTEM | &quot;OPERATING_SYSTEM&quot; |
| LICENSE_AND_SUBSCRIPTION | &quot;LICENSE_AND_SUBSCRIPTION&quot; |
| VALIDATION | &quot;VALIDATION&quot; |
| OBSERVABILITY | &quot;OBSERVABILITY&quot; |
| SECURITY | &quot;SECURITY&quot; |
| NETWORKING | &quot;NETWORKING&quot; |
| CONFIGURATION | &quot;CONFIGURATION&quot; |
| BACKUP | &quot;BACKUP&quot; |
| OTHER | &quot;OTHER&quot; |



