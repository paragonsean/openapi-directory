

# LedgerAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether the account is active or not. |  [optional] |
|**bankAccount** | [**BankAccount**](BankAccount.md) |  |  [optional] |
|**categories** | [**List&lt;CategoriesInner&gt;**](CategoriesInner.md) | The categories of the account. |  [optional] [readonly] |
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | The classification of account. |  [optional] |
|**code** | **String** | The code assigned to the account. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**currentBalance** | **BigDecimal** | The current balance of the account. |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**description** | **String** | The description of the account. |  [optional] |
|**displayId** | **String** | The human readable display ID used when displaying the account |  [optional] |
|**fullyQualifiedName** | **String** | The fully qualified name of the account. |  [optional] |
|**header** | **Boolean** | Whether the account is a header or not. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**lastReconciliationDate** | **LocalDate** | Reconciliation Date means the last calendar day of each Reconciliation Period. |  [optional] |
|**level** | **BigDecimal** |  |  [optional] |
|**name** | **String** | The name of the account. |  [optional] |
|**nominalCode** | **String** | The nominal code of the ledger account. |  [optional] |
|**openingBalance** | **BigDecimal** | The opening balance of the account. |  [optional] |
|**parentAccount** | [**LedgerAccountParentAccount**](LedgerAccountParentAccount.md) |  |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the account. |  [optional] |
|**subAccount** | **Boolean** | Whether the account is a sub account or not. |  [optional] |
|**subAccounts** | [**List&lt;SubAccountsInner&gt;**](SubAccountsInner.md) | The sub accounts of the account. |  [optional] [readonly] |
|**subType** | **String** | The sub type of account. |  [optional] |
|**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  |  [optional] |
|**taxType** | **String** | The tax type of the account. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of account. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: ClassificationEnum

| Name | Value |
|---- | -----|
| ASSET | &quot;asset&quot; |
| EQUITY | &quot;equity&quot; |
| EXPENSE | &quot;expense&quot; |
| LIABILITY | &quot;liability&quot; |
| REVENUE | &quot;revenue&quot; |
| INCOME | &quot;income&quot; |
| OTHER_INCOME | &quot;other_income&quot; |
| OTHER_EXPENSE | &quot;other_expense&quot; |
| COSTS_OF_SALES | &quot;costs_of_sales&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| ARCHIVED | &quot;archived&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNTS_RECEIVABLE | &quot;accounts_receivable&quot; |
| REVENUE | &quot;revenue&quot; |
| SALES | &quot;sales&quot; |
| OTHER_INCOME | &quot;other_income&quot; |
| BANK | &quot;bank&quot; |
| CURRENT_ASSET | &quot;current_asset&quot; |
| FIXED_ASSET | &quot;fixed_asset&quot; |
| NON_CURRENT_ASSET | &quot;non_current_asset&quot; |
| OTHER_ASSET | &quot;other_asset&quot; |
| BALANCESHEET | &quot;balancesheet&quot; |
| EQUITY | &quot;equity&quot; |
| EXPENSE | &quot;expense&quot; |
| OTHER_EXPENSE | &quot;other_expense&quot; |
| COSTS_OF_SALES | &quot;costs_of_sales&quot; |
| ACCOUNTS_PAYABLE | &quot;accounts_payable&quot; |
| CREDIT_CARD | &quot;credit_card&quot; |
| CURRENT_LIABILITY | &quot;current_liability&quot; |
| NON_CURRENT_LIABILITY | &quot;non_current_liability&quot; |
| OTHER_LIABILITY | &quot;other_liability&quot; |
| OTHER | &quot;other&quot; |



