

# CheckDeposit

Check Deposits allow you to deposit images of paper checks into your account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Account the check was deposited into. |  |
|**amount** | **Integer** | The deposited amount in the minor unit of the destination account currency. For dollars, for example, this is cents. |  |
|**backImageFileId** | **String** | The ID for the File containing the image of the back of the check. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the deposit. |  |
|**depositAcceptance** | [**CheckDepositAcceptance**](CheckDepositAcceptance.md) |  |  |
|**depositRejection** | [**CheckDepositRejection**](CheckDepositRejection.md) |  |  |
|**depositReturn** | [**CheckDepositReturn**](CheckDepositReturn.md) |  |  |
|**frontImageFileId** | **String** | The ID for the File containing the image of the front of the check. |  |
|**id** | **String** | The deposit&#39;s identifier. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the Check Deposit. |  |
|**transactionId** | **String** | The ID for the Transaction created by the deposit. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;check_deposit&#x60;. |  |



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
| PENDING | &quot;pending&quot; |
| SUBMITTED | &quot;submitted&quot; |
| REJECTED | &quot;rejected&quot; |
| RETURNED | &quot;returned&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHECK_DEPOSIT | &quot;check_deposit&quot; |



