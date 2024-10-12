

# InvoicePaymentApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | Total amount of the payment |  [optional] |
|**id** | **Integer** | Id of invoice payment |  [optional] |
|**isAutomatic** | **Boolean** | Indicate if the payment is automatic or manual |  [optional] |
|**note** | **String** | Internal payment note |  [optional] |
|**paidOn** | **OffsetDateTime** | When the payment was done by the client |  [optional] |
|**referenceId** | **String** | Id of the payment |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of payment |  [optional] |



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



