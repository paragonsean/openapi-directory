

# CheckDepositReturn1

A Check Deposit Return object. This field will be present in the JSON response if and only if `category` is equal to `check_deposit_return`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**checkDepositId** | **String** | The identifier of the Check Deposit that was returned. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s currency. |  |
|**returnReason** | [**ReturnReasonEnum**](#ReturnReasonEnum) |  |  |
|**returnedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check deposit was returned. |  |
|**transactionId** | **String** | The identifier of the transaction that reversed the original check deposit transaction. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: ReturnReasonEnum

| Name | Value |
|---- | -----|
| ACH_CONVERSION_NOT_SUPPORTED | &quot;ach_conversion_not_supported&quot; |
| CLOSED_ACCOUNT | &quot;closed_account&quot; |
| DUPLICATE_SUBMISSION | &quot;duplicate_submission&quot; |
| INSUFFICIENT_FUNDS | &quot;insufficient_funds&quot; |
| NO_ACCOUNT | &quot;no_account&quot; |
| NOT_AUTHORIZED | &quot;not_authorized&quot; |
| STALE_DATED | &quot;stale_dated&quot; |
| STOP_PAYMENT | &quot;stop_payment&quot; |
| UNKNOWN_REASON | &quot;unknown_reason&quot; |
| UNMATCHED_DETAILS | &quot;unmatched_details&quot; |
| UNREADABLE_IMAGE | &quot;unreadable_image&quot; |



