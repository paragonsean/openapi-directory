

# Payment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  [optional] |
|**invoiceId** | **Integer** |  |  [optional] |
|**isAutomatic** | **Boolean** |  |  [optional] |
|**note** | **String** |  |  [optional] |
|**paidOn** | **OffsetDateTime** |  |  [optional] |
|**referenceId** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OTHER | &quot;Other&quot; |
| PAYPAL | &quot;Paypal&quot; |
| STRIPE | &quot;Stripe&quot; |
| PAYONEER | &quot;Payoneer&quot; |
| BANK | &quot;Bank&quot; |
| CASH | &quot;Cash&quot; |
| CHEQUE | &quot;Cheque&quot; |
| ACH | &quot;Ach&quot; |
| SEPA | &quot;Sepa&quot; |
| SQUARE | &quot;Square&quot; |
| KLIK_AND_PAY | &quot;KlikAndPay&quot; |
| RAZORPAY | &quot;Razorpay&quot; |
| WEPAY | &quot;Wepay&quot; |
| HALKBANK | &quot;Halkbank&quot; |
| TWO_CHECKOUT | &quot;TwoCheckout&quot; |
| PAYMENT_WALL | &quot;PaymentWall&quot; |
| BAMBORA_EU | &quot;BamboraEU&quot; |
| BAMBORA_NA | &quot;BamboraNA&quot; |
| NLB | &quot;Nlb&quot; |
| AUTHORIZE_NET | &quot;AuthorizeNet&quot; |
| BRAINTREE | &quot;Braintree&quot; |



