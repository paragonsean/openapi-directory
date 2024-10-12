

# CapitalGrant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | An object containing the amount of the grant, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |  [optional] |
|**balances** | [**CapitalBalance**](CapitalBalance.md) | An object containing the details of the existing grant. |  |
|**counterparty** | [**Counterparty**](Counterparty.md) | An object containing the details of the receiving party of the grant. Setting either an &#x60;accountHolderId&#x60;, &#x60;balanceAccountId&#x60;, or both is required. |  [optional] |
|**fee** | [**Fee**](Fee.md) | An object containing the fee currency and value, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |  [optional] |
|**grantAccountId** | **String** | The identifier of the grant account used for the grant. |  |
|**grantOfferId** | **String** | The identifier of the grant offer that has been selected and from which the grant details will be used. |  |
|**id** | **String** | The identifier of the grant reference. |  |
|**repayment** | [**Repayment**](Repayment.md) | An object containing the details of the 30-day repayment threshold. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the grant. Possible values: **Pending**, **Active**, **Repaid**. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;Pending&quot; |
| ACTIVE | &quot;Active&quot; |
| REPAID | &quot;Repaid&quot; |



