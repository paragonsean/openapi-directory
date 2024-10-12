

# MasterpassDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |  [optional] |
|**masterpassTransactionId** | **String** | The Masterpass transaction ID. |  |
|**type** | [**TypeEnum**](#TypeEnum) | **masterpass** |  [optional] |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MASTERPASS | &quot;masterpass&quot; |



