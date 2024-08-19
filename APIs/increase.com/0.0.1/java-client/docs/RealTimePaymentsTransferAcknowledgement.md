

# RealTimePaymentsTransferAcknowledgement

A Real Time Payments Transfer Acknowledgement object. This field will be present in the JSON response if and only if `category` is equal to `real_time_payments_transfer_acknowledgement`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The transfer amount in USD cents. |  |
|**destinationAccountNumber** | **String** | The destination account number. |  |
|**destinationRoutingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**remittanceInformation** | **String** | Unstructured information that will show on the recipient&#39;s bank statement. |  |
|**transferId** | **String** | The identifier of the Real Time Payments Transfer that led to this Transaction. |  |



