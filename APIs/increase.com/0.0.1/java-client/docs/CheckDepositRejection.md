

# CheckDepositRejection

If your deposit is rejected by Increase, this will contain details as to why it was rejected.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The rejected amount in the minor unit of check&#39;s currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check&#39;s currency. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Why the check deposit was rejected. |  |
|**rejectedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check deposit was rejected. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| INCOMPLETE_IMAGE | &quot;incomplete_image&quot; |
| DUPLICATE | &quot;duplicate&quot; |
| POOR_IMAGE_QUALITY | &quot;poor_image_quality&quot; |
| INCORRECT_AMOUNT | &quot;incorrect_amount&quot; |
| INCORRECT_RECIPIENT | &quot;incorrect_recipient&quot; |
| NOT_ELIGIBLE_FOR_MOBILE_DEPOSIT | &quot;not_eligible_for_mobile_deposit&quot; |
| UNKNOWN | &quot;unknown&quot; |



