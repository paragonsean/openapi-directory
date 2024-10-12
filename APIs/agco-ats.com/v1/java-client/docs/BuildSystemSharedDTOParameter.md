

# BuildSystemSharedDTOParameter

A DTO for an IParameter

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**direction** | [**DirectionEnum**](#DirectionEnum) | The parameter direction (Input or Output) |  [optional] |
|**name** | **String** | The name of the parameter |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The data type of the parameter |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INPUT | &quot;Input&quot; |
| OUTPUT | &quot;Output&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;String&quot; |
| BOOLEAN | &quot;Boolean&quot; |
| INTEGER | &quot;Integer&quot; |
| FLOAT | &quot;Float&quot; |
| STRING_DICTIONARY | &quot;StringDictionary&quot; |



