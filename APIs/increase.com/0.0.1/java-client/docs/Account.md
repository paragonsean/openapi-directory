

# Account

Accounts are your bank accounts with Increase. They store money, receive transfers, and send payments. They earn interest and have depository insurance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account was created. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Account currency. |  |
|**entityId** | **String** | The identifier for the Entity the Account belongs to. |  |
|**id** | **String** | The Account identifier. |  |
|**informationalEntityId** | **String** | The identifier of an Entity that, while not owning the Account, is associated with its activity. |  |
|**interestAccrued** | **String** | The interest accrued but not yet paid, expressed as a string containing a floating-point value. |  |
|**interestAccruedAt** | **LocalDate** | The latest [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which interest was accrued. |  |
|**name** | **String** | The name you choose for the Account. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the Account. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;account&#x60;. |  |



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
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT | &quot;account&quot; |



