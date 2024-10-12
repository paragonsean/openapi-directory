

# PaidByTime

paid-by-time restrictions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Redemption&#39;s additional restriction type. |  |
|**time** | **OffsetDateTime** | The time when the coupon&#39;s redemption is no longer valid and removed from unpaid invoices if applied. Note that this datetime cannot be changed. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DISCOUNTS_PER_REDEMPTION | &quot;discounts-per-redemption&quot; |
| MINIMUM_ORDER_AMOUNT | &quot;minimum-order-amount&quot; |
| RESTRICT_TO_INVOICES | &quot;restrict-to-invoices&quot; |
| RESTRICT_TO_PLANS | &quot;restrict-to-plans&quot; |
| RESTRICT_TO_SUBSCRIPTIONS | &quot;restrict-to-subscriptions&quot; |
| RESTRICT_TO_PRODUCTS | &quot;restrict-to-products&quot; |
| PAID_BY_TIME | &quot;paid-by-time&quot; |



