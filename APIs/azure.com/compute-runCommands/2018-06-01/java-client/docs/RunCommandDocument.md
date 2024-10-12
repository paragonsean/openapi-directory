

# RunCommandDocument

Describes the properties of a Run Command.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parameters** | [**List&lt;RunCommandParameterDefinition&gt;**](RunCommandParameterDefinition.md) | The parameters used by the script. |  [optional] |
|**script** | **List&lt;String&gt;** | The script to be executed. |  |
|**$schema** | **String** | The VM run command schema. |  |
|**description** | **String** | The VM run command description. |  |
|**id** | **String** | The VM run command id. |  |
|**label** | **String** | The VM run command label. |  |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The Operating System type. |  |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



