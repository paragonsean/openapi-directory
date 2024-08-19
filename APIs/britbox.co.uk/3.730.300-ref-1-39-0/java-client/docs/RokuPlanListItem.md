

# RokuPlanListItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Float** | The price of a plan. If a free plan then undefined. |  |
|**currency** | **String** | The currency a plan is offered in. |  |
|**description** | **String** | The textual description. |  |
|**interval** | [**IntervalEnum**](#IntervalEnum) | The type of billing period used. |  |
|**intervalCount** | **Integer** | Given the &#x60;interval&#x60; this is how frequently it will run. e.g. every 2 weeks. |  |
|**nickname** | **String** | The title of a plan. |  |
|**product** | **String** | The product of a plan. |  |
|**productCode** | **String** | The identifier of a plan. |  |
|**savingLabel** | **String** | NA. |  |
|**trialPeriodDays** | **Integer** | How many days a trial period runs for a plan. Only valid if &#x60;hasTrialPeriod&#x60; is true. |  |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| YEAR | &quot;year&quot; |
| NONE | &quot;none&quot; |



