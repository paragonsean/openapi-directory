

# Account


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balance** | **Long** | The current balance of the account in milliunits format |  |
|**clearedBalance** | **Long** | The current cleared balance of the account in milliunits format |  |
|**closed** | **Boolean** | Whether this account is closed or not |  |
|**debtEscrowAmounts** | **Map&lt;String, Long&gt;** |  |  [optional] |
|**debtInterestRates** | **Map&lt;String, Long&gt;** |  |  [optional] |
|**debtMinimumPayments** | **Map&lt;String, Long&gt;** |  |  [optional] |
|**debtOriginalBalance** | **Long** | The original debt/loan account balance, specified in milliunits format. |  [optional] |
|**deleted** | **Boolean** | Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests. |  |
|**directImportInError** | **Boolean** | If an account linked to a financial institution (direct_import_linked&#x3D;true) and the linked connection is not in a healthy state, this will be true. |  [optional] |
|**directImportLinked** | **Boolean** | Whether or not the account is linked to a financial institution for automatic transaction import. |  [optional] |
|**id** | **UUID** |  |  |
|**lastReconciledAt** | **OffsetDateTime** | A date/time specifying when the account was last reconciled. |  [optional] |
|**name** | **String** |  |  |
|**note** | **String** |  |  [optional] |
|**onBudget** | **Boolean** | Whether this account is on budget or not |  |
|**transferPayeeId** | **UUID** | The payee id which should be used when transferring to this account |  |
|**type** | **AccountType** |  |  |
|**unclearedBalance** | **Long** | The current uncleared balance of the account in milliunits format |  |



