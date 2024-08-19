

# AccountNumber

Each account can have multiple account and routing numbers. We recommend that you use a set per vendor. This is similar to how you use different passwords for different websites. Account numbers can also be used to seamlessly reconcile inbound payments. Generating a unique account number per vendor ensures you always know the originator of an incoming payment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The identifier for the account this Account Number belongs to. |  |
|**accountNumber** | **String** | The account number. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account Number was created. |  |
|**id** | **String** | The Account Number identifier. |  |
|**name** | **String** | The name you choose for the Account Number. |  |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**status** | [**StatusEnum**](#StatusEnum) | This indicates if payments can be made to the Account Number. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;account_number&#x60;. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DISABLED | &quot;disabled&quot; |
| CANCELED | &quot;canceled&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_NUMBER | &quot;account_number&quot; |



