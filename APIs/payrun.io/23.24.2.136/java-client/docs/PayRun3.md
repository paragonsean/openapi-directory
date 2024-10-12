

# PayRun3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executed** | **OffsetDateTime** | The pay runs&#39; executed |  [optional] |
|**isSupplementary** | **Boolean** | The pay runs&#39; is supplementary |  [optional] |
|**payFrequency** | [**PayFrequencyEnum**](#PayFrequencyEnum) | The pay runs&#39; pay frequency |  [optional] |
|**paySchedule** | [**PaySchedule2**](PaySchedule2.md) |  |  [optional] |
|**paymentDate** | **LocalDate** | The pay runs&#39; payment date |  [optional] |
|**periodEnd** | **LocalDate** | The pay runs&#39; period end |  [optional] |
|**periodStart** | **LocalDate** | The pay runs&#39; period start |  [optional] |
|**proceedingPayRun** | [**ProceedingPayRun**](ProceedingPayRun.md) |  |  [optional] |
|**sequence** | **Integer** | The pay runs&#39; sequence |  [optional] |
|**taxPeriod** | **Integer** | The pay runs&#39; tax period |  [optional] |
|**taxYear** | **Integer** | The pay runs&#39; tax year |  [optional] |



## Enum: PayFrequencyEnum

| Name | Value |
|---- | -----|
| WEEKLY | &quot;Weekly&quot; |
| MONTHLY | &quot;Monthly&quot; |
| TWO_WEEKLY | &quot;TwoWeekly&quot; |
| FOUR_WEEKLY | &quot;FourWeekly&quot; |
| YEARLY | &quot;Yearly&quot; |



