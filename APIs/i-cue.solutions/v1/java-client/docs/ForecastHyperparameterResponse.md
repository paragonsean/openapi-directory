

# ForecastHyperparameterResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discardData** | **Boolean** |  |  [optional] |
|**errorType** | [**ErrorTypeEnum**](#ErrorTypeEnum) |  |  [optional] |
|**holdOutPeriod** | **Integer** |  |  [optional] |
|**noFcst** | **Integer** |  |  [optional] |
|**periodicity** | **Integer** |  |  [optional] |



## Enum: ErrorTypeEnum

| Name | Value |
|---- | -----|
| MEAN_ABSOLUTE_PERCENTAGE_ERROR | &quot;MeanAbsolutePercentageError&quot; |
| MEAN_SQUARED_ERROR | &quot;MeanSquaredError&quot; |
| MEAN_ABSOLUTE_ERROR | &quot;MeanAbsoluteError&quot; |
| MEDIAN_ABSOLUTE_DEVIATION | &quot;MedianAbsoluteDeviation&quot; |
| NONE | &quot;None&quot; |



