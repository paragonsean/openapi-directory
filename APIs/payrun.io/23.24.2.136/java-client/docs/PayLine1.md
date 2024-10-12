

# PayLine1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculator** | **String** | The pay lines&#39; calculator |  [optional] |
|**description** | **String** | The pay lines&#39; description |  [optional] |
|**generated** | **OffsetDateTime** | The pay lines&#39; generated |  [optional] |
|**payCode** | **String** | The pay lines&#39; pay code |  [optional] |
|**payCodeType** | [**PayCodeTypeEnum**](#PayCodeTypeEnum) | The pay lines&#39; pay code type |  [optional] |
|**payRunSequence** | **Integer** | The pay lines&#39; pay run sequence |  [optional] |
|**paymentDate** | **LocalDate** | The pay lines&#39; payment date |  [optional] |
|**taxPeriod** | **Integer** | The pay lines&#39; tax period |  [optional] |
|**taxYear** | **Integer** | The pay lines&#39; tax year |  [optional] |
|**value** | **Double** | The pay lines&#39; value |  [optional] |



## Enum: PayCodeTypeEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| PAYMENT | &quot;Payment&quot; |
| DEDUCTION | &quot;Deduction&quot; |



