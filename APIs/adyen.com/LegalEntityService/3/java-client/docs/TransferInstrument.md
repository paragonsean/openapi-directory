

# TransferInstrument


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccount** | [**BankAccountInfo**](BankAccountInfo.md) | Contains information about the legal entity&#39;s bank account. |  |
|**capabilities** | [**Map&lt;String, SupportingEntityCapability&gt;**](SupportingEntityCapability.md) | List of capabilities for this transfer instrument. |  [optional] |
|**documentDetails** | [**List&lt;DocumentReference&gt;**](DocumentReference.md) | List of documents uploaded for the transfer instrument. |  [optional] |
|**id** | **String** | The unique identifier of the transfer instrument. |  [readonly] |
|**legalEntityId** | **String** | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument. |  |
|**problems** | [**List&lt;CapabilityProblem&gt;**](CapabilityProblem.md) | The verification errors related to capabilities for this transfer instrument. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of transfer instrument.  Possible value: **bankAccount**. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_ACCOUNT | &quot;bankAccount&quot; |
| RECURRING_DETAIL | &quot;recurringDetail&quot; |



