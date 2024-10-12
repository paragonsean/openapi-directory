

# CisInstruction1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cisLineTag** | **String** | The cis instructions&#39; cis line tag |  [optional] |
|**cisLineType** | **String** | The cis instructions&#39; cis line type |  [optional] |
|**description** | **String** | The cis instructions&#39; description |  [optional] |
|**payFrequency** | [**PayFrequencyEnum**](#PayFrequencyEnum) | The cis instructions&#39; pay frequency |  [optional] |
|**periodEnd** | **Integer** | The cis instructions&#39; period end |  [optional] |
|**periodStart** | **Integer** | The cis instructions&#39; period start |  [optional] |
|**taxYearEnd** | **Integer** | The cis instructions&#39; tax year end |  [optional] |
|**taxYearStart** | **Integer** | The cis instructions&#39; tax year start |  [optional] |
|**UOM** | [**UOMEnum**](#UOMEnum) | The cis instructions&#39; u o m |  [optional] |
|**units** | **Double** | The cis instructions&#39; units |  [optional] |
|**VAT** | **Double** | The cis instructions&#39; v a t |  [optional] |
|**value** | **Double** | The cis instructions&#39; value |  [optional] |



## Enum: PayFrequencyEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;Monthly&quot; |
| WEEKLY | &quot;Weekly&quot; |



## Enum: UOMEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| MINUTE | &quot;Minute&quot; |
| HOUR | &quot;Hour&quot; |
| DAY | &quot;Day&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |
| YEAR | &quot;Year&quot; |
| UNIT | &quot;Unit&quot; |



