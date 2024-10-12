

# SlashCommandMetadata

Annotation metadata for slash commands (/).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bot** | [**User**](User.md) |  |  [optional] |
|**commandId** | **String** | The command ID of the invoked slash command. |  [optional] |
|**commandName** | **String** | The name of the invoked slash command. |  [optional] |
|**triggersDialog** | **Boolean** | Indicates whether the slash command is for a dialog. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of slash command. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| ADD | &quot;ADD&quot; |
| INVOKE | &quot;INVOKE&quot; |



