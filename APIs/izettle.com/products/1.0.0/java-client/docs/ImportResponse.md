

# ImportResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** |  |  [optional] |
|**errorMessage** | **String** |  |  [optional] |
|**finished** | **OffsetDateTime** |  |  [optional] |
|**items** | **Long** |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**uuid** | **UUID** |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| IMPORTING | &quot;IMPORTING&quot; |
| FINISHED_SUCCESS | &quot;FINISHED_SUCCESS&quot; |
| FINISHED_FAILED | &quot;FINISHED_FAILED&quot; |



