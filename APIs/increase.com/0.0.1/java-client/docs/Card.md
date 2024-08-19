

# Card

Cards are commercial credit cards. They'll immediately work for online purchases after you create them. All cards maintain a credit limit of 100% of the Account’s available balance at the time of transaction. Funds are deducted from the Account upon transaction settlement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The identifier for the account this card belongs to. |  |
|**billingAddress** | [**BillingAddress**](BillingAddress.md) |  |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Card was created. |  |
|**description** | **String** | The card&#39;s description for display purposes. |  |
|**digitalWallet** | [**DigitalWallet**](DigitalWallet.md) |  |  |
|**expirationMonth** | **Integer** | The month the card expires in M format (e.g., August is 8). |  |
|**expirationYear** | **Integer** | The year the card expires in YYYY format (e.g., 2025). |  |
|**id** | **String** | The card identifier. |  |
|**last4** | **String** | The last 4 digits of the Card&#39;s Primary Account Number. |  |
|**status** | [**StatusEnum**](#StatusEnum) | This indicates if payments can be made with the card. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;card&#x60;. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DISABLED | &quot;disabled&quot; |
| CANCELED | &quot;canceled&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CARD | &quot;card&quot; |



