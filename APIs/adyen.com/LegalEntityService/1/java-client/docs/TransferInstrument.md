

# TransferInstrument


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccount** | [**BankAccountInfo**](BankAccountInfo.md) | Contains information about the legal entity&#39;s bank account. |  |
|**documents** | [**List&lt;EntityReference&gt;**](EntityReference.md) | List of documents uploaded for the transfer instrument. |  [optional] |
|**id** | **String** | The unique identifier of the transfer instrument. |  [readonly] |
|**legalEntityId** | **String** | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of transfer instrument.  Possible value: **bankAccount**. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_ACCOUNT | &quot;bankAccount&quot; |
| RECURRING_DETAIL | &quot;recurringDetail&quot; |



