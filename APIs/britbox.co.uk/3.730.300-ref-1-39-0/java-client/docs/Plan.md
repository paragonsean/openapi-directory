

# Plan


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | An alias for a plan. |  |
|**benefits** | **List&lt;String&gt;** | The list of benefits to display for a plan. |  |
|**billingPeriodFrequency** | **Integer** | Given the &#x60;billingPeriodType&#x60; this is how frequently it will run. e.g. every 2 weeks. |  |
|**billingPeriodType** | [**BillingPeriodTypeEnum**](#BillingPeriodTypeEnum) | The type of billing period used. |  |
|**currency** | **String** | The currency a plan is offered in. |  |
|**customFields** | **Map&lt;String, Object&gt;** | A map of custom fields defined by a curator for a plan. |  [optional] |
|**hasTrialPeriod** | **Boolean** | True if a plan has a trial period, false if not. |  |
|**id** | **String** | The identifier of a plan. |  |
|**isActive** | **Boolean** | True if a plan is active, false if its retired. |  |
|**isFeatured** | **Boolean** | True if a plan should be highlighted as featured, false if not. |  |
|**isPrivate** | **Boolean** | True if a plan should not be presented in the primary plan options, false if not. |  |
|**price** | **Float** | The price of a plan. If a free plan then undefined. |  [optional] |
|**revenueType** | [**RevenueTypeEnum**](#RevenueTypeEnum) | The revenue type a plan targets. |  |
|**subscriptionCode** | **String** | The subscription code a plan targets. |  |
|**tagline** | **String** | The short tagline for a plan. |  |
|**termsAndConditions** | **String** | The terms and conditions for a plan. |  |
|**title** | **String** | The title of a plan. |  |
|**trialPeriodDays** | **Integer** | How many days a trial period runs for a plan. Only valid if &#x60;hasTrialPeriod&#x60; is true. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of plan. |  |



## Enum: BillingPeriodTypeEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| YEAR | &quot;year&quot; |
| NONE | &quot;none&quot; |



## Enum: RevenueTypeEnum

| Name | Value |
|---- | -----|
| TVOD | &quot;TVOD&quot; |
| SVOD | &quot;SVOD&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FREE | &quot;Free&quot; |
| SUBSCRIPTION | &quot;Subscription&quot; |



