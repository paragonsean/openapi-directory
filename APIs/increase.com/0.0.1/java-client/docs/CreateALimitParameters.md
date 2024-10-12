

# CreateALimitParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interval** | [**IntervalEnum**](#IntervalEnum) | The interval for the metric. Required if &#x60;metric&#x60; is &#x60;count&#x60; or &#x60;volume&#x60;. |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) | The metric for the limit. |  |
|**modelId** | **String** | The identifier of the Account or Account Number you wish to associate the limit with. |  |
|**value** | **Integer** | The value to test the limit against. |  |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| TRANSACTION | &quot;transaction&quot; |
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| YEAR | &quot;year&quot; |
| ALL_TIME | &quot;all_time&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;count&quot; |
| VOLUME | &quot;volume&quot; |



