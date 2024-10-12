

# CisLine1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cisDeduction** | **Double** | The cis lines&#39; cis deduction |  [optional] |
|**cisLineType** | **String** | The cis lines&#39; cis line type |  [optional] |
|**description** | **String** | The cis lines&#39; description |  [optional] |
|**generated** | **OffsetDateTime** | The cis lines&#39; generated |  [optional] |
|**grossPay** | **Double** | The cis lines&#39; gross pay |  [optional] |
|**nominalCodeKey** | **String** | The cis lines&#39; nominal code key |  [optional] |
|**payFrequency** | [**PayFrequencyEnum**](#PayFrequencyEnum) | The cis lines&#39; pay frequency |  [optional] |
|**taxMonth** | **Integer** | The cis lines&#39; tax month |  [optional] |
|**taxPeriod** | **Integer** | The cis lines&#39; tax period |  [optional] |
|**taxTreatment** | [**TaxTreatmentEnum**](#TaxTreatmentEnum) | The cis lines&#39; tax treatment |  [optional] |
|**taxYear** | **Integer** | The cis lines&#39; tax year |  [optional] |
|**UOM** | [**UOMEnum**](#UOMEnum) | The cis lines&#39; u o m |  [optional] |
|**unitRate** | **Double** | The cis lines&#39; unit rate |  [optional] |
|**units** | **Double** | The cis lines&#39; units |  [optional] |
|**VAT** | **Double** | The cis lines&#39; v a t |  [optional] |



## Enum: PayFrequencyEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;Monthly&quot; |
| WEEKLY | &quot;Weekly&quot; |



## Enum: TaxTreatmentEnum

| Name | Value |
|---- | -----|
| TAXABLE | &quot;Taxable&quot; |
| NON_TAXABLE | &quot;NonTaxable&quot; |
| NOTIONAL | &quot;Notional&quot; |
| MATERIALS | &quot;Materials&quot; |



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



