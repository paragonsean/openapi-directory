

# SubscriptionChange


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effectiveTime** | **OffsetDateTime** | The date from which the renewal time (for &#x60;reset&#x60; operations) and proration calculations are made.  If omitted, it will default to the current time. |  [optional] |
|**items** | [**List&lt;SubscriptionChangeItemsInner&gt;**](SubscriptionChangeItemsInner.md) |  |  |
|**keepTrial** | **Boolean** | If set to true and the subscription order has an active trial, it will use that trial further. Works with &#39;retain&#39; renewalPolicy only. |  [optional] |
|**preview** | **Boolean** | If set to true, it will not change the subscription.  It allows for a way to preview the changes that would be made to a subscription. |  [optional] |
|**prorated** | **Boolean** | Whether or not to give a pro rata credit for the amount of time remaining between the &#x60;effectiveTime&#x60; and the end of the current period. In addition, if the &#x60;renewalTime&#x60; is retained (by setting the &#x60;renewalPolicy&#x60; to &#x60;retain&#x60;), then a pro rata debit will occur as well, for the amount between the &#x60;effectiveTime&#x60; and the &#x60;renewalTime&#x60; as a percentage of the normal period size.  |  |
|**renewalPolicy** | [**RenewalPolicyEnum**](#RenewalPolicyEnum) | The value determines whether the subscription retains its current &#x60;renewalTime&#x60; or resets it to a newly calculated &#x60;renewalTime&#x60;. |  |



## Enum: RenewalPolicyEnum

| Name | Value |
|---- | -----|
| RESET | &quot;reset&quot; |
| RETAIN | &quot;retain&quot; |



