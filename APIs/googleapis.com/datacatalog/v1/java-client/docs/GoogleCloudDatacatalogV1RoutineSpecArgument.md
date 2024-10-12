

# GoogleCloudDatacatalogV1RoutineSpecArgument

Input or output argument of a function or stored procedure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | Specifies whether the argument is input or output. |  [optional] |
|**name** | **String** | The name of the argument. A return argument of a function might not have a name. |  [optional] |
|**type** | **String** | Type of the argument. The exact value depends on the source system and the language. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| IN | &quot;IN&quot; |
| OUT | &quot;OUT&quot; |
| INOUT | &quot;INOUT&quot; |



