# AccountingApi.LedgerAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Whether the account is active or not. | [optional] 
**bankAccount** | [**BankAccount**](BankAccount.md) |  | [optional] 
**categories** | [**[CategoriesInner]**](CategoriesInner.md) | The categories of the account. | [optional] [readonly] 
**classification** | **String** | The classification of account. | [optional] 
**code** | **String** | The code assigned to the account. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currentBalance** | **Number** | The current balance of the account. | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**description** | **String** | The description of the account. | [optional] 
**displayId** | **String** | The human readable display ID used when displaying the account | [optional] 
**fullyQualifiedName** | **String** | The fully qualified name of the account. | [optional] 
**header** | **Boolean** | Whether the account is a header or not. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**lastReconciliationDate** | **Date** | Reconciliation Date means the last calendar day of each Reconciliation Period. | [optional] 
**level** | **Number** |  | [optional] 
**name** | **String** | The name of the account. | [optional] 
**nominalCode** | **String** | The nominal code of the ledger account. | [optional] 
**openingBalance** | **Number** | The opening balance of the account. | [optional] 
**parentAccount** | [**LedgerAccountParentAccount**](LedgerAccountParentAccount.md) |  | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**status** | **String** | The status of the account. | [optional] 
**subAccount** | **Boolean** | Whether the account is a sub account or not. | [optional] 
**subAccounts** | [**[SubAccountsInner]**](SubAccountsInner.md) | The sub accounts of the account. | [optional] [readonly] 
**subType** | **String** | The sub type of account. | [optional] 
**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**taxType** | **String** | The tax type of the account. | [optional] 
**type** | **String** | The type of account. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: ClassificationEnum


* `asset` (value: `"asset"`)

* `equity` (value: `"equity"`)

* `expense` (value: `"expense"`)

* `liability` (value: `"liability"`)

* `revenue` (value: `"revenue"`)

* `income` (value: `"income"`)

* `other_income` (value: `"other_income"`)

* `other_expense` (value: `"other_expense"`)

* `costs_of_sales` (value: `"costs_of_sales"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `archived` (value: `"archived"`)





## Enum: TypeEnum


* `accounts_receivable` (value: `"accounts_receivable"`)

* `revenue` (value: `"revenue"`)

* `sales` (value: `"sales"`)

* `other_income` (value: `"other_income"`)

* `bank` (value: `"bank"`)

* `current_asset` (value: `"current_asset"`)

* `fixed_asset` (value: `"fixed_asset"`)

* `non_current_asset` (value: `"non_current_asset"`)

* `other_asset` (value: `"other_asset"`)

* `balancesheet` (value: `"balancesheet"`)

* `equity` (value: `"equity"`)

* `expense` (value: `"expense"`)

* `other_expense` (value: `"other_expense"`)

* `costs_of_sales` (value: `"costs_of_sales"`)

* `accounts_payable` (value: `"accounts_payable"`)

* `credit_card` (value: `"credit_card"`)

* `current_liability` (value: `"current_liability"`)

* `non_current_liability` (value: `"non_current_liability"`)

* `other_liability` (value: `"other_liability"`)

* `other` (value: `"other"`)




