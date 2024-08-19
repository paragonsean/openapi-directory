# ThePlaidApi.PayPeriodDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkAmount** | **Number** | The amount of the paycheck. | [optional] 
**distributionBreakdown** | [**[DistributionBreakdown]**](DistributionBreakdown.md) |  | [optional] 
**endDate** | **Date** | The pay period end date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: \&quot;yyyy-mm-dd\&quot;. | [optional] 
**grossEarnings** | **Number** | Total earnings before tax/deductions. | [optional] 
**payDate** | **Date** | The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | [optional] 
**payDay** | **Date** | The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | [optional] 
**payFrequency** | **String** | The frequency at which an individual is paid. | [optional] 
**startDate** | **Date** | The pay period start date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: \&quot;yyyy-mm-dd\&quot;. | [optional] 



## Enum: PayFrequencyEnum


* `PAY_FREQUENCY_UNKNOWN` (value: `"PAY_FREQUENCY_UNKNOWN"`)

* `PAY_FREQUENCY_WEEKLY` (value: `"PAY_FREQUENCY_WEEKLY"`)

* `PAY_FREQUENCY_BIWEEKLY` (value: `"PAY_FREQUENCY_BIWEEKLY"`)

* `PAY_FREQUENCY_SEMIMONTHLY` (value: `"PAY_FREQUENCY_SEMIMONTHLY"`)

* `PAY_FREQUENCY_MONTHLY` (value: `"PAY_FREQUENCY_MONTHLY"`)




