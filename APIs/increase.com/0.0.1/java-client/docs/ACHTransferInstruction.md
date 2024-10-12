

# ACHTransferInstruction

A ACH Transfer Instruction object. This field will be present in the JSON response if and only if `category` is equal to `ach_transfer_instruction`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The pending amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**transferId** | **String** | The identifier of the ACH Transfer that led to this Pending Transaction. |  |



