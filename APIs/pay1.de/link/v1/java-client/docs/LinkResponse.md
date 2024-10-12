

# LinkResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | identifier for the subaccount |  [optional] |
|**active** | **Boolean** | link activation status |  [optional] |
|**amount** | **Long** | total amount of all shopping cart items in lowest denomination |  [optional] |
|**backgroundImage** | **String** | backgroundImage css property |  [optional] |
|**billing** | [**AddressDataDto**](AddressDataDto.md) |  |  [optional] |
|**created** | **Long** | created time in ISO 8601 format |  [optional] |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | currency code |  [optional] |
|**description** | **String** | free format description of the payment |  [optional] |
|**email** | **String** | customer email for invoices or payment notification |  [optional] |
|**errorUrl** | **String** | final redirect after a failed payment |  [optional] |
|**expiration** | **LocalDate** | link expiration date, the link will only be executable until end of that day |  [optional] |
|**hash** | **String** | hash for the client API |  [optional] |
|**id** | **String** | link id |  [optional] |
|**intent** | [**IntentEnum**](#IntentEnum) | designates the type of transaction that will be created |  [optional] |
|**invoiceInformation** | [**InvoiceInformationDto**](InvoiceInformationDto.md) |  |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) | link ISO language code |  [optional] |
|**link** | **String** | customer payment link |  [optional] |
|**logo** | **String** | logo url |  [optional] |
|**merchantId** | **String** | identifier for the merchant |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | execution mode |  [optional] |
|**modified** | **Long** | last modified time in ISO 8601 format |  [optional] |
|**notifyUrl** | **String** | notify url. If unset no notification will be send |  [optional] |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | available payment methods |  [optional] |
|**paymentMethods** | [**List&lt;PaymentMethodsEnum&gt;**](#List&lt;PaymentMethodsEnum&gt;) | list of available payment methods |  [optional] |
|**paymentProcess** | **String** | identifier of the created payment process. |  [optional] |
|**portalId** | **String** | identifier for the portal |  [optional] |
|**redirectUrl** | **String** | redirect url. empty if the payment process does not require a redirect. |  [optional] |
|**reference** | **String** | payment reference number, has to be unique per merchant and mode |  [optional] |
|**shipping** | [**AddressDataDto**](AddressDataDto.md) |  |  [optional] |
|**shoppingCart** | [**List&lt;CartItemDto&gt;**](CartItemDto.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | link status |  [optional] |
|**successUrl** | **String** | final redirect after a successful payment |  [optional] |
|**userId** | **String** | identifier of the created user. |  [optional] |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| ALL | &quot;ALL&quot; |
| DZD | &quot;DZD&quot; |
| ARS | &quot;ARS&quot; |
| AUD | &quot;AUD&quot; |
| BSD | &quot;BSD&quot; |
| BHD | &quot;BHD&quot; |
| BDT | &quot;BDT&quot; |
| AMD | &quot;AMD&quot; |
| BBD | &quot;BBD&quot; |
| BMD | &quot;BMD&quot; |
| BTN | &quot;BTN&quot; |
| BOB | &quot;BOB&quot; |
| BWP | &quot;BWP&quot; |
| BZD | &quot;BZD&quot; |
| SBD | &quot;SBD&quot; |
| BND | &quot;BND&quot; |
| MMK | &quot;MMK&quot; |
| BIF | &quot;BIF&quot; |
| KHR | &quot;KHR&quot; |
| CAD | &quot;CAD&quot; |
| CVE | &quot;CVE&quot; |
| KYD | &quot;KYD&quot; |
| LKR | &quot;LKR&quot; |
| CLP | &quot;CLP&quot; |
| CNY | &quot;CNY&quot; |
| COP | &quot;COP&quot; |
| KMF | &quot;KMF&quot; |
| CRC | &quot;CRC&quot; |
| HRK | &quot;HRK&quot; |
| CUP | &quot;CUP&quot; |
| CZK | &quot;CZK&quot; |
| DKK | &quot;DKK&quot; |
| DOP | &quot;DOP&quot; |
| SVC | &quot;SVC&quot; |
| ETB | &quot;ETB&quot; |
| ERN | &quot;ERN&quot; |
| FKP | &quot;FKP&quot; |
| FJD | &quot;FJD&quot; |
| DJF | &quot;DJF&quot; |
| GMD | &quot;GMD&quot; |
| GIP | &quot;GIP&quot; |
| GTQ | &quot;GTQ&quot; |
| GNF | &quot;GNF&quot; |
| GYD | &quot;GYD&quot; |
| HTG | &quot;HTG&quot; |
| HNL | &quot;HNL&quot; |
| HKD | &quot;HKD&quot; |
| HUF | &quot;HUF&quot; |
| ISK | &quot;ISK&quot; |
| INR | &quot;INR&quot; |
| IDR | &quot;IDR&quot; |
| IRR | &quot;IRR&quot; |
| IQD | &quot;IQD&quot; |
| ILS | &quot;ILS&quot; |
| JMD | &quot;JMD&quot; |
| JPY | &quot;JPY&quot; |
| KZT | &quot;KZT&quot; |
| JOD | &quot;JOD&quot; |
| KES | &quot;KES&quot; |
| KPW | &quot;KPW&quot; |
| KRW | &quot;KRW&quot; |
| KWD | &quot;KWD&quot; |
| KGS | &quot;KGS&quot; |
| LAK | &quot;LAK&quot; |
| LBP | &quot;LBP&quot; |
| LSL | &quot;LSL&quot; |
| LRD | &quot;LRD&quot; |
| LYD | &quot;LYD&quot; |
| MOP | &quot;MOP&quot; |
| MWK | &quot;MWK&quot; |
| MYR | &quot;MYR&quot; |
| MVR | &quot;MVR&quot; |
| MUR | &quot;MUR&quot; |
| MXN | &quot;MXN&quot; |
| MNT | &quot;MNT&quot; |
| MDL | &quot;MDL&quot; |
| MAD | &quot;MAD&quot; |
| OMR | &quot;OMR&quot; |
| NAD | &quot;NAD&quot; |
| NPR | &quot;NPR&quot; |
| ANG | &quot;ANG&quot; |
| AWG | &quot;AWG&quot; |
| VUV | &quot;VUV&quot; |
| NZD | &quot;NZD&quot; |
| NIO | &quot;NIO&quot; |
| NGN | &quot;NGN&quot; |
| NOK | &quot;NOK&quot; |
| PKR | &quot;PKR&quot; |
| PAB | &quot;PAB&quot; |
| PGK | &quot;PGK&quot; |
| PYG | &quot;PYG&quot; |
| PEN | &quot;PEN&quot; |
| PHP | &quot;PHP&quot; |
| QAR | &quot;QAR&quot; |
| RUB | &quot;RUB&quot; |
| RWF | &quot;RWF&quot; |
| SHP | &quot;SHP&quot; |
| SAR | &quot;SAR&quot; |
| SCR | &quot;SCR&quot; |
| SLL | &quot;SLL&quot; |
| SGD | &quot;SGD&quot; |
| VND | &quot;VND&quot; |
| SOS | &quot;SOS&quot; |
| ZAR | &quot;ZAR&quot; |
| SSP | &quot;SSP&quot; |
| SZL | &quot;SZL&quot; |
| SEK | &quot;SEK&quot; |
| CHF | &quot;CHF&quot; |
| SYP | &quot;SYP&quot; |
| THB | &quot;THB&quot; |
| TOP | &quot;TOP&quot; |
| TTD | &quot;TTD&quot; |
| AED | &quot;AED&quot; |
| TND | &quot;TND&quot; |
| UGX | &quot;UGX&quot; |
| MKD | &quot;MKD&quot; |
| EGP | &quot;EGP&quot; |
| GBP | &quot;GBP&quot; |
| TZS | &quot;TZS&quot; |
| USD | &quot;USD&quot; |
| UYU | &quot;UYU&quot; |
| UZS | &quot;UZS&quot; |
| WST | &quot;WST&quot; |
| YER | &quot;YER&quot; |
| TWD | &quot;TWD&quot; |
| UYW | &quot;UYW&quot; |
| VES | &quot;VES&quot; |
| MRU | &quot;MRU&quot; |
| STN | &quot;STN&quot; |
| CUC | &quot;CUC&quot; |
| ZWL | &quot;ZWL&quot; |
| BYN | &quot;BYN&quot; |
| TMT | &quot;TMT&quot; |
| GHS | &quot;GHS&quot; |
| SDG | &quot;SDG&quot; |
| UYI | &quot;UYI&quot; |
| RSD | &quot;RSD&quot; |
| MZN | &quot;MZN&quot; |
| AZN | &quot;AZN&quot; |
| RON | &quot;RON&quot; |
| CHE | &quot;CHE&quot; |
| CHW | &quot;CHW&quot; |
| TRY | &quot;TRY&quot; |
| XAF | &quot;XAF&quot; |
| XCD | &quot;XCD&quot; |
| XOF | &quot;XOF&quot; |
| XPF | &quot;XPF&quot; |
| XBA | &quot;XBA&quot; |
| XBB | &quot;XBB&quot; |
| XBC | &quot;XBC&quot; |
| XBD | &quot;XBD&quot; |
| XAU | &quot;XAU&quot; |
| XDR | &quot;XDR&quot; |
| XAG | &quot;XAG&quot; |
| XPT | &quot;XPT&quot; |
| XTS | &quot;XTS&quot; |
| XPD | &quot;XPD&quot; |
| XUA | &quot;XUA&quot; |
| ZMW | &quot;ZMW&quot; |
| SRD | &quot;SRD&quot; |
| MGA | &quot;MGA&quot; |
| COU | &quot;COU&quot; |
| AFN | &quot;AFN&quot; |
| TJS | &quot;TJS&quot; |
| AOA | &quot;AOA&quot; |
| BGN | &quot;BGN&quot; |
| CDF | &quot;CDF&quot; |
| BAM | &quot;BAM&quot; |
| EUR | &quot;EUR&quot; |
| MXV | &quot;MXV&quot; |
| UAH | &quot;UAH&quot; |
| GEL | &quot;GEL&quot; |
| BOV | &quot;BOV&quot; |
| PLN | &quot;PLN&quot; |
| BRL | &quot;BRL&quot; |
| CLF | &quot;CLF&quot; |
| XSU | &quot;XSU&quot; |
| USN | &quot;USN&quot; |



## Enum: IntentEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION | &quot;authorization&quot; |
| PREAUTHORIZATION | &quot;preauthorization&quot; |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| DE_DE | &quot;de_DE&quot; |
| EN_US | &quot;en_US&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;live&quot; |
| TEST | &quot;test&quot; |



## Enum: PaymentMethodEnum

| Name | Value |
|---- | -----|
| VISA | &quot;visa&quot; |
| MASTERCARD | &quot;mastercard&quot; |
| AMEX | &quot;amex&quot; |
| PAYPAL | &quot;paypal&quot; |
| SOFORT | &quot;sofort&quot; |
| PAYDIREKT | &quot;paydirekt&quot; |
| POSTFINANCE_E | &quot;postfinance-e&quot; |
| POSTFINANCE_CARD | &quot;postfinance-card&quot; |
| BANCONTACT | &quot;bancontact&quot; |
| PRZELEWY24 | &quot;przelewy24&quot; |
| ALIPAY | &quot;alipay&quot; |
| IDEAL | &quot;ideal&quot; |
| EPS | &quot;eps&quot; |
| GIROPAY | &quot;giropay&quot; |
| SEPA | &quot;sepa&quot; |



## Enum: List&lt;PaymentMethodsEnum&gt;

| Name | Value |
|---- | -----|
| VISA | &quot;visa&quot; |
| MASTERCARD | &quot;mastercard&quot; |
| AMEX | &quot;amex&quot; |
| PAYPAL | &quot;paypal&quot; |
| SOFORT | &quot;sofort&quot; |
| PAYDIREKT | &quot;paydirekt&quot; |
| POSTFINANCE_E | &quot;postfinance-e&quot; |
| POSTFINANCE_CARD | &quot;postfinance-card&quot; |
| BANCONTACT | &quot;bancontact&quot; |
| PRZELEWY24 | &quot;przelewy24&quot; |
| ALIPAY | &quot;alipay&quot; |
| IDEAL | &quot;ideal&quot; |
| EPS | &quot;eps&quot; |
| GIROPAY | &quot;giropay&quot; |
| SEPA | &quot;sepa&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;ready&quot; |
| CREATED | &quot;created&quot; |
| EXECUTED | &quot;executed&quot; |
| EXPIRED | &quot;expired&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



