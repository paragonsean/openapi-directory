

# WireTransferIntention

A Wire Transfer Intention object. This field will be present in the JSON response if and only if `category` is equal to `wire_transfer_intention`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The destination account number. |  |
|**amount** | **Integer** | The transfer amount in USD cents. |  |
|**messageToRecipient** | **String** | The message that will show on the recipient&#39;s bank statement. |  |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**transferId** | **String** |  |  |



