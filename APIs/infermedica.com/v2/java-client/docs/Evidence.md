

# Evidence


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**choiceId** | [**ChoiceIdEnum**](#ChoiceIdEnum) |  |  |
|**id** | **String** | id of observation or condition |  |
|**observedAt** | **String** | time when evidence was observed in ISO 8601 format |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | Flag describing evidence origin |  [optional] |



## Enum: ChoiceIdEnum

| Name | Value |
|---- | -----|
| PRESENT | &quot;present&quot; |
| ABSENT | &quot;absent&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| INITIAL | &quot;initial&quot; |
| SUGGEST | &quot;suggest&quot; |
| PREDEFINED | &quot;predefined&quot; |
| RED_FLAGS | &quot;red_flags&quot; |



