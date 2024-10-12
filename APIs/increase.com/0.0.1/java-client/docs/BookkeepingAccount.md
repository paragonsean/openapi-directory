

# BookkeepingAccount

Accounts are T-accounts. They can store accounting entries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The API Account associated with this bookkeeping account. |  |
|**complianceCategory** | [**ComplianceCategoryEnum**](#ComplianceCategoryEnum) | The compliance category of the account. |  |
|**entityId** | **String** | The Entity associated with this bookkeeping account. |  |
|**id** | **String** | The account identifier. |  |
|**name** | **String** | The name you choose for the account. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;bookkeeping_account&#x60;. |  |



## Enum: ComplianceCategoryEnum

| Name | Value |
|---- | -----|
| COMMINGLED_CASH | &quot;commingled_cash&quot; |
| CUSTOMER_BALANCE | &quot;customer_balance&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BOOKKEEPING_ACCOUNT | &quot;bookkeeping_account&quot; |



