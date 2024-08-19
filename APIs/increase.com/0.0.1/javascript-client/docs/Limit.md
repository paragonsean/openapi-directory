# IncreaseApi.Limit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The Limit identifier. | 
**interval** | **String** | The interval for the metric. This is required if &#x60;metric&#x60; is &#x60;count&#x60; or &#x60;volume&#x60;. | 
**metric** | **String** | The metric for the Limit. | 
**modelId** | **String** | The identifier of the Account Number, Account, or Card the Limit applies to. | 
**modelType** | **String** | The type of the model you wish to associate the Limit with. | 
**status** | **String** | The current status of the Limit. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;limit&#x60;. | 
**value** | **Number** | The value to evaluate the Limit against. | 



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





## Enum: ModelTypeEnum


* `account` (value: `"account"`)

* `account_number` (value: `"account_number"`)

* `card` (value: `"card"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)





## Enum: TypeEnum


* `limit` (value: `"limit"`)




