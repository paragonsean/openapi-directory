# IncreaseApi.CreateALimitParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **String** | The interval for the metric. Required if &#x60;metric&#x60; is &#x60;count&#x60; or &#x60;volume&#x60;. | [optional] 
**metric** | **String** | The metric for the limit. | 
**modelId** | **String** | The identifier of the Account or Account Number you wish to associate the limit with. | 
**value** | **Number** | The value to test the limit against. | 



## Enum: IntervalEnum


* `transaction` (value: `"transaction"`)

* `day` (value: `"day"`)

* `week` (value: `"week"`)

* `month` (value: `"month"`)

* `year` (value: `"year"`)

* `all_time` (value: `"all_time"`)





## Enum: MetricEnum


* `count` (value: `"count"`)

* `volume` (value: `"volume"`)




