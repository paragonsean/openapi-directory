

# TaxRateMappingInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Code for the tax rate from the accounting platform. |  [optional] |
|**effectiveTaxRate** | **BigDecimal** | Effective tax rate. |  [optional] |
|**id** | **String** | Unique identifier of tax rate. |  [optional] |
|**name** | **String** | Name of the tax rate in the accounting platform. |  [optional] |
|**totalTaxRate** | **BigDecimal** | Total (not compounded) sum of the components of a tax rate. |  [optional] |
|**validTransactionTypes** | [**List&lt;ValidTransactionTypesEnum&gt;**](#List&lt;ValidTransactionTypesEnum&gt;) | Supported transaction types for the account. |  [optional] |



## Enum: List&lt;ValidTransactionTypesEnum&gt;

| Name | Value |
|---- | -----|
| PAYMENT | &quot;Payment&quot; |
| REFUND | &quot;Refund&quot; |
| REWARD | &quot;Reward&quot; |
| CHARGEBACK | &quot;Chargeback&quot; |
| TRANSFER_IN | &quot;TransferIn&quot; |
| TRANSFER_OUT | &quot;TransferOut&quot; |
| ADJUSTMENT_IN | &quot;AdjustmentIn&quot; |
| ADJUSTMENT_OUT | &quot;AdjustmentOut&quot; |



