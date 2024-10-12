

# NewPayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** |  |  [optional] |
|**customerIDFK** | **Integer** | Only required if no invoice allocations specified. |  [optional] |
|**dateIssued** | **OffsetDateTime** | Date of Payment. If not specified, assumes today. |  [optional] |
|**exchangeRate** | **Double** | Optional. Only used when the Customer&#39;s currecy is different from the Avaza account&#39;s base currency. Specifies the exchange rate that should apply between the customer currency and base currency. If not provided we will obtain an up to date exchange rate for the Payment Issue Date. |  [optional] |
|**notes** | **String** |  |  [optional] |
|**paymentAllocations** | [**List&lt;NewPaymentAllocation&gt;**](NewPaymentAllocation.md) | List of amounts within this payment that are allocated to invoices. The sum of these be less than or equal to the payment amount. |  [optional] |
|**paymentNumber** | **String** | Optional. If not specified will be automatically generated |  [optional] |
|**paymentProviderCode** | **String** | Optional for storing the payment provider who was the source of funds. |  [optional] |
|**transactionPrefix** | **String** | Optional to override the default prefix added to Payment Numbers |  [optional] |
|**transactionReference** | **String** | Optional for storing the reference # of the payment method. |  [optional] |



