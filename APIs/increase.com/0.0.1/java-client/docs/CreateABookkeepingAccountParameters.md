

# CreateABookkeepingAccountParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The entity, if &#x60;compliance_category&#x60; is &#x60;commingled_cash&#x60;. |  [optional] |
|**complianceCategory** | [**ComplianceCategoryEnum**](#ComplianceCategoryEnum) | The account compliance category. |  [optional] |
|**entityId** | **String** | The entity, if &#x60;compliance_category&#x60; is &#x60;customer_balance&#x60;. |  [optional] |
|**name** | **String** | The name you choose for the account. |  |



## Enum: ComplianceCategoryEnum

| Name | Value |
|---- | -----|
| COMMINGLED_CASH | &quot;commingled_cash&quot; |
| CUSTOMER_BALANCE | &quot;customer_balance&quot; |



