

# ConflictResolutionPolicy

The conflict resolution policy for the container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conflictResolutionPath** | **String** | The conflict resolution path in the case of LastWriterWins mode. |  [optional] |
|**conflictResolutionProcedure** | **String** | The procedure to resolve conflicts in the case of custom mode. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Indicates the conflict resolution mode. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| LAST_WRITER_WINS | &quot;LastWriterWins&quot; |
| CUSTOM | &quot;Custom&quot; |



