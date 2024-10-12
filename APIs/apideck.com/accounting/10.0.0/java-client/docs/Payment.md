

# Payment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  |  [optional] |
|**accountsReceivableAccountId** | **String** | Unique identifier for the account to allocate payment to. |  [optional] |
|**accountsReceivableAccountType** | **String** | Type of accounts receivable account. |  [optional] |
|**allocations** | [**List&lt;PaymentAllocationsInner&gt;**](PaymentAllocationsInner.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**currencyRate** | **BigDecimal** | Currency Exchange Rate at the time entity was recorded/generated. |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  |  [optional] |
|**displayId** | **String** | Payment id to be displayed. |  [optional] |
|**downstreamId** | **String** | The third-party API ID of original entity |  [optional] [readonly] |
|**id** | **String** | Unique identifier representing the entity |  [readonly] |
|**note** | **String** | Optional note to be associated with the payment. |  [optional] |
|**paymentMethod** | **String** | Payment method name |  [optional] |
|**paymentMethodId** | **String** | Unique identifier for the payment method. |  [optional] |
|**paymentMethodReference** | **String** | Optional reference message returned by payment method on processing |  [optional] |
|**reconciled** | **Boolean** | Payment has been reconciled |  [optional] |
|**reference** | **String** | Optional payment reference message ie: Debit remittance detail. |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of payment |  [optional] |
|**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  |  [optional] |
|**totalAmount** | **BigDecimal** | Amount of payment |  |
|**transactionDate** | **OffsetDateTime** | Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of payment |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AUTHORISED | &quot;authorised&quot; |
| PAID | &quot;paid&quot; |
| VOIDED | &quot;voided&quot; |
| DELETED | &quot;deleted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RECEIVABLE | &quot;accounts_receivable&quot; |
| PAYABLE | &quot;accounts_payable&quot; |
| RECEIVABLE_CREDIT | &quot;accounts_receivable_credit&quot; |
| PAYABLE_CREDIT | &quot;accounts_payable_credit&quot; |
| RECEIVABLE_OVERPAYMENT | &quot;accounts_receivable_overpayment&quot; |
| PAYABLE_OVERPAYMENT | &quot;accounts_payable_overpayment&quot; |
| RECEIVABLE_PREPAYMENT | &quot;accounts_receivable_prepayment&quot; |
| PAYABLE_PREPAYMENT | &quot;accounts_payable_prepayment&quot; |



