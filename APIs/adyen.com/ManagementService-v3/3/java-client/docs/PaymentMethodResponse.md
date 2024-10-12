

# PaymentMethodResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**PaginationLinks**](PaginationLinks.md) | Pagination references. |  [optional] |
|**data** | [**List&lt;PaymentMethod&gt;**](PaymentMethod.md) | The list of supported payment methods and their details. |  [optional] |
|**itemsTotal** | **Integer** | Total number of items. |  |
|**pagesTotal** | **Integer** | Total number of pages. |  |
|**typesWithErrors** | [**List&lt;TypesWithErrorsEnum&gt;**](#List&lt;TypesWithErrorsEnum&gt;) | Payment method types with errors. |  [optional] |



## Enum: List&lt;TypesWithErrorsEnum&gt;

| Name | Value |
|---- | -----|
| AFTERPAYTOUCH | &quot;afterpaytouch&quot; |
| ALIPAY | &quot;alipay&quot; |
| ALIPAY_HK | &quot;alipay_hk&quot; |
| AMEX | &quot;amex&quot; |
| APPLEPAY | &quot;applepay&quot; |
| BCMC | &quot;bcmc&quot; |
| BLIK | &quot;blik&quot; |
| CARTEBANCAIRE | &quot;cartebancaire&quot; |
| CLEARPAY | &quot;clearpay&quot; |
| CUP | &quot;cup&quot; |
| DINERS | &quot;diners&quot; |
| DIRECTDEBIT_GB | &quot;directdebit_GB&quot; |
| DISCOVER | &quot;discover&quot; |
| EBANKING_FI | &quot;ebanking_FI&quot; |
| EFTPOS_AUSTRALIA | &quot;eftpos_australia&quot; |
| ELO | &quot;elo&quot; |
| ELOCREDIT | &quot;elocredit&quot; |
| ELODEBIT | &quot;elodebit&quot; |
| GIROCARD | &quot;girocard&quot; |
| GOOGLEPAY | &quot;googlepay&quot; |
| HIPER | &quot;hiper&quot; |
| HIPERCARD | &quot;hipercard&quot; |
| IDEAL | &quot;ideal&quot; |
| INTERAC_CARD | &quot;interac_card&quot; |
| JCB | &quot;jcb&quot; |
| KLARNA | &quot;klarna&quot; |
| KLARNA_ACCOUNT | &quot;klarna_account&quot; |
| KLARNA_PAYNOW | &quot;klarna_paynow&quot; |
| MAESTRO | &quot;maestro&quot; |
| MBWAY | &quot;mbway&quot; |
| MC | &quot;mc&quot; |
| MCDEBIT | &quot;mcdebit&quot; |
| MEAL_VOUCHER_FR | &quot;mealVoucher_FR&quot; |
| MOBILEPAY | &quot;mobilepay&quot; |
| MULTIBANCO | &quot;multibanco&quot; |
| ONLINE_BANKING_PL | &quot;onlineBanking_PL&quot; |
| PAYBYBANK | &quot;paybybank&quot; |
| PAYPAL | &quot;paypal&quot; |
| PAYSHOP | &quot;payshop&quot; |
| SWISH | &quot;swish&quot; |
| TRUSTLY | &quot;trustly&quot; |
| TWINT | &quot;twint&quot; |
| TWINT_POS | &quot;twint_pos&quot; |
| VIPPS | &quot;vipps&quot; |
| VISA | &quot;visa&quot; |
| VISADEBIT | &quot;visadebit&quot; |
| VPAY | &quot;vpay&quot; |
| WECHATPAY | &quot;wechatpay&quot; |
| WECHATPAY_POS | &quot;wechatpay_pos&quot; |



