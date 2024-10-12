

# Register201ResponseDataContract



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accepted** | **Boolean** | Whether the contract has been accepted by the agent |  |
|**expiration** | **OffsetDateTime** | The time at which the contract expires |  |
|**factionSymbol** | **String** | The symbol of the faction that this contract is for. |  |
|**fulfilled** | **Boolean** | Whether the contract has been fulfilled |  |
|**id** | **String** |  |  |
|**terms** | [**Register201ResponseDataContractTerms**](Register201ResponseDataContractTerms.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PROCUREMENT | &quot;PROCUREMENT&quot; |
| TRANSPORT | &quot;TRANSPORT&quot; |
| SHUTTLE | &quot;SHUTTLE&quot; |



