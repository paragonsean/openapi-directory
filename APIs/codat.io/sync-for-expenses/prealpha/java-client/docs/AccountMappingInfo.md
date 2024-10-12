

# AccountMappingInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Type of the account. |  [optional] |
|**currency** | **String** | Currency of the account. |  [optional] |
|**id** | **String** | Unique identifier of account. |  [optional] |
|**name** | **String** | Name of the account as it appears in the companies accounting software. |  [optional] |
|**validTransactionTypes** | [**List&lt;ValidTransactionTypesEnum&gt;**](#List&lt;ValidTransactionTypesEnum&gt;) | Supported transaction types for the account. |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| ASSET | &quot;Asset&quot; |
| LIABILITY | &quot;Liability&quot; |
| INCOME | &quot;Income&quot; |
| EXPENSE | &quot;Expense&quot; |
| EQUITY | &quot;Equity&quot; |



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



