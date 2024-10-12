

# RequestRate

The rate at which requests for resources will be made to downstream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rate** | **Integer** | The number of requests per window unit. |  |
|**size** | **Integer** | Size of request window. |  |
|**unit** | [**UnitEnum**](#UnitEnum) | The window unit for the rate. |  |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| SECOND | &quot;second&quot; |
| MINUTE | &quot;minute&quot; |
| HOUR | &quot;hour&quot; |
| DAY | &quot;day&quot; |



