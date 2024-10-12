

# InboundFundsHold

A Inbound Funds Hold object. This field will be present in the JSON response if and only if `category` is equal to `inbound_funds_hold`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The held amount in the minor unit of the account&#39;s currency. For dollars, for example, this is cents. |  |
|**automaticallyReleasesAt** | **OffsetDateTime** | When the hold will be released automatically. Certain conditions may cause it to be released before this time. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the hold was created. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the hold&#39;s currency. |  |
|**heldTransactionId** | **String** | The ID of the Transaction for which funds were held. |  |
|**pendingTransactionId** | **String** | The ID of the Pending Transaction representing the held funds. |  |
|**releasedAt** | **OffsetDateTime** | When the hold was released (if it has been released). |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the hold. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| HELD | &quot;held&quot; |
| COMPLETE | &quot;complete&quot; |



