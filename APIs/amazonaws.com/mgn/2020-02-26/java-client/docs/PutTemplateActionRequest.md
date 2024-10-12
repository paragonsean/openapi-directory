

# PutTemplateActionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionID** | **String** | Template post migration custom action ID. |  |
|**actionName** | **String** | Template post migration custom action name. |  |
|**active** | **Boolean** | Template post migration custom action active status. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Template post migration custom action category. |  [optional] |
|**description** | **String** | Template post migration custom action description. |  [optional] |
|**documentIdentifier** | **String** | Template post migration custom action document identifier. |  |
|**documentVersion** | **String** | Template post migration custom action document version. |  [optional] |
|**externalParameters** | [**Map&lt;String, SsmExternalParameter&gt;**](SsmExternalParameter.md) | Template post migration custom action external parameters. |  [optional] |
|**launchConfigurationTemplateID** | **String** | Launch configuration template ID. |  |
|**mustSucceedForCutover** | **Boolean** | Template post migration custom action must succeed for cutover. |  [optional] |
|**operatingSystem** | **String** | Operating system eligible for this template post migration custom action. |  [optional] |
|**order** | **Integer** | Template post migration custom action order. |  |
|**parameters** | **Map&lt;String, List&lt;SsmParameterStoreParameter&gt;&gt;** | Template post migration custom action parameters. |  [optional] |
|**timeoutSeconds** | **Integer** | Template post migration custom action timeout in seconds. |  [optional] |



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



