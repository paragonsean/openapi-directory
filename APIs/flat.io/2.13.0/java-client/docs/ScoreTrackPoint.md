

# ScoreTrackPoint

A track synchronization point

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**measureUuid** | **UUID** | The measure unique identifier |  [optional] |
|**time** | **BigDecimal** | The corresponding time in seconds |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the synchronization point. If the type is &#x60;measure&#x60;, the measure uuid must be present in &#x60;measureUuid&#x60; |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MEASURE | &quot;measure&quot; |
| END | &quot;end&quot; |



