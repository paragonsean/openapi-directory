

# ACHTransferIntention

A ACH Transfer Intention object. This field will be present in the JSON response if and only if `category` is equal to `ach_transfer_intention`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** |  |  |
|**amount** | **Integer** | The amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**routingNumber** | **String** |  |  |
|**statementDescriptor** | **String** |  |  |
|**transferId** | **String** | The identifier of the ACH Transfer that led to this Transaction. |  |



