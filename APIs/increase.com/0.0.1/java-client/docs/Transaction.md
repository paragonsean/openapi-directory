

# Transaction

If the ACH Transfer attempt succeeds, this will contain the resulting [Transaction](#transactions) object. The Transaction's `source` will be of `category: inbound_ach_transfer`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The identifier for the Account the Transaction belongs to. |  |
|**amount** | **Integer** | The Transaction amount in the minor unit of its currency. For dollars, for example, this is cents. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Transaction occured. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Transaction&#39;s currency. This will match the currency on the Transcation&#39;s Account. |  |
|**description** | **String** | For a Transaction related to a transfer, this is the description you provide. For a Transaction related to a payment, this is the description the vendor provides. |  |
|**id** | **String** | The Transaction identifier. |  |
|**routeId** | **String** | The identifier for the route this Transaction came through. Routes are things like cards and ACH details. |  |
|**routeType** | [**RouteTypeEnum**](#RouteTypeEnum) | The type of the route this Transaction came through. |  |
|**source** | [**TransactionSource**](TransactionSource.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;transaction&#x60;. |  |



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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TRANSACTION | &quot;transaction&quot; |



