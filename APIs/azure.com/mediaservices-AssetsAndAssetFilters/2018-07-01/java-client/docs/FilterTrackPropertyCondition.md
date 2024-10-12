

# FilterTrackPropertyCondition

The class to specify one track property condition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | [**OperationEnum**](#OperationEnum) | The track property condition operation. |  |
|**property** | [**PropertyEnum**](#PropertyEnum) | The track property type. |  |
|**value** | **String** | The track property value. |  |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| EQUAL | &quot;Equal&quot; |
| NOT_EQUAL | &quot;NotEqual&quot; |



## Enum: PropertyEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| TYPE | &quot;Type&quot; |
| NAME | &quot;Name&quot; |
| LANGUAGE | &quot;Language&quot; |
| FOUR_CC | &quot;FourCC&quot; |
| BITRATE | &quot;Bitrate&quot; |



