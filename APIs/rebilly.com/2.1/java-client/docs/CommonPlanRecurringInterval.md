

# CommonPlanRecurringInterval

The service interval. For a one-time item, use `null`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**length** | **Integer** | The length of time. |  |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit of time. |  |
|**billingTiming** | **PlanBillingTiming** |  |  [optional] |
|**limit** | **Integer** | The number of invoices this subscription order will generate (if 1, it will not generate any beyond the initial order creation). For example, set this property to &#x60;12&#x60;, when the &#x60;periodUnit&#x60; is month and the &#x60;periodDuration&#x60; is 1, for a 1 year contract billed monthly.  |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| YEAR | &quot;year&quot; |



