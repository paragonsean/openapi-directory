

# JournalEntryLineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  |  [optional] |
|**departmentId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**description** | **String** | User defined description |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  |  |
|**locationId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**subTotal** | **BigDecimal** | Sub-total amount, normally before tax. |  [optional] |
|**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount |  [optional] |
|**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  |  [optional] |
|**totalAmount** | **BigDecimal** | Debit entries are considered positive, and credit entries are considered negative. |  [optional] |
|**trackingCategory** | [**LinkedTrackingCategory**](LinkedTrackingCategory.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Debit entries are considered positive, and credit entries are considered negative. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEBIT | &quot;debit&quot; |
| CREDIT | &quot;credit&quot; |



