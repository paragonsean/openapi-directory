

# ItvEntitlementPlan


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cost** | **Integer** | Source platform of purchase. |  |
|**interval** | [**IntervalEnum**](#IntervalEnum) | The type of billing period used. |  |
|**trialLength** | **Integer** | Given the &#x60;interval&#x60; this is how frequently it will run. e.g. every 2 weeks. |  |
|**type** | **String** | Type of the plan. |  |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| YEAR | &quot;year&quot; |
| NONE | &quot;none&quot; |



