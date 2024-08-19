

# PendingTransaction

If the authorization attempt succeeds, this will contain the resulting Pending Transaction object. The Pending Transaction's `source` will be of `category: card_authorization`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The identifier for the account this Pending Transaction belongs to. |  |
|**amount** | **Integer** | The Pending Transaction amount in the minor unit of its currency. For dollars, for example, this is cents. |  |
|**completedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Pending Transaction was completed. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Pending Transaction occured. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Pending Transaction&#39;s currency. This will match the currency on the Pending Transcation&#39;s Account. |  |
|**description** | **String** | For a Pending Transaction related to a transfer, this is the description you provide. For a Pending Transaction related to a payment, this is the description the vendor provides. |  |
|**id** | **String** | The Pending Transaction identifier. |  |
|**routeId** | **String** | The identifier for the route this Pending Transaction came through. Routes are things like cards and ACH details. |  |
|**routeType** | [**RouteTypeEnum**](#RouteTypeEnum) | The type of the route this Pending Transaction came through. |  |
|**source** | [**PendingTransactionSource**](PendingTransactionSource.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the Pending Transaction has been confirmed and has an associated Transaction. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;pending_transaction&#x60;. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: RouteTypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_NUMBER | &quot;account_number&quot; |
| CARD | &quot;card&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COMPLETE | &quot;complete&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PENDING_TRANSACTION | &quot;pending_transaction&quot; |



