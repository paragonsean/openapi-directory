

# BtPlanListItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Float** | The price of a plan. If a free plan then undefined. |  [optional] |
|**ctaText** | **String** | The textual description. |  |
|**currency** | **String** | The currency a plan is offered in. |  |
|**description** | **String** | The textual description. |  |
|**ees07PlanDescription** | **String** |  |  [optional] |
|**ees07PlanTitle** | **String** |  |  [optional] |
|**ees07Title** | **String** |  |  [optional] |
|**headerText** | **String** | The textual description. |  |
|**heroText** | **String** | The textual description. |  |
|**id** | **String** | The identifier of a plan. |  |
|**interval** | [**IntervalEnum**](#IntervalEnum) | The type of billing period used. |  [optional] |
|**intervalCount** | **Integer** | Given the &#x60;interval&#x60; this is how frequently it will run. e.g. every 2 weeks. |  [optional] |
|**longText** | **String** | The textual description. |  |
|**nickname** | **String** | The title of a plan. |  |
|**noThanksText** | **String** |  |  [optional] |
|**product** | **String** | The product of a plan. |  |
|**switchingText** | **String** |  |  [optional] |
|**termsAndConditionsItunes** | **String** |  |  [optional] |
|**termsAndConditionsStripe** | **String** |  |  [optional] |
|**trialPeriodDays** | **Integer** | How many days a trial period runs for a plan. Only valid if &#x60;hasTrialPeriod&#x60; is true. |  |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| YEAR | &quot;year&quot; |
| NONE | &quot;none&quot; |



