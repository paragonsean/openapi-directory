# PayoneLinkApi.LinkCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | identifier for the subaccount | 
**active** | **Boolean** | link activation status | [optional] [default to true]
**backgroundImage** | **String** | backgroundImage css property | [optional] 
**billing** | [**AddressDataDto**](AddressDataDto.md) |  | [optional] 
**currency** | **String** | currency code | 
**description** | **String** | free format description of the payment | [optional] 
**email** | **String** | email the invoice should be delivered to | [optional] 
**errorUrl** | **String** | final redirect after a final payment | [optional] 
**expiration** | **Date** | link expiration date, the link will only be executable until end of that day | [optional] 
**intent** | **String** | designates the type of transaction that will be created | [optional] [default to &#39;authorization&#39;]
**invoiceInformation** | [**InvoiceInformationDto**](InvoiceInformationDto.md) |  | [optional] 
**language** | **String** | link ISO language code | [optional] 
**logo** | **String** | logo url | [optional] 
**merchantId** | **String** | identifier for the merchant | 
**mode** | **String** | execution mode | 
**notifyUrl** | **String** | Url where the notification will be send after link was executed | [optional] 
**paymentMethods** | **[String]** | list of available payment methods | [optional] 
**portalId** | **String** | identifier for the portal | 
**reference** | **String** | payment reference number, has to be unique per merchant and mode | 
**shipping** | [**AddressDataDto**](AddressDataDto.md) |  | [optional] 
**shoppingCart** | [**[CartItemDto]**](CartItemDto.md) |  | 
**successUrl** | **String** | final redirect after a successful payment | [optional] 
**userId** | **String** | identifier for the user | [optional] 



## Enum: CurrencyEnum


* `ALL` (value: `"ALL"`)

* `DZD` (value: `"DZD"`)

* `ARS` (value: `"ARS"`)

* `AUD` (value: `"AUD"`)

* `BSD` (value: `"BSD"`)

* `BHD` (value: `"BHD"`)

* `BDT` (value: `"BDT"`)

* `AMD` (value: `"AMD"`)

* `BBD` (value: `"BBD"`)

* `BMD` (value: `"BMD"`)

* `BTN` (value: `"BTN"`)

* `BOB` (value: `"BOB"`)

* `BWP` (value: `"BWP"`)

* `BZD` (value: `"BZD"`)

* `SBD` (value: `"SBD"`)

* `BND` (value: `"BND"`)

* `MMK` (value: `"MMK"`)

* `BIF` (value: `"BIF"`)

* `KHR` (value: `"KHR"`)

* `CAD` (value: `"CAD"`)

* `CVE` (value: `"CVE"`)

* `KYD` (value: `"KYD"`)

* `LKR` (value: `"LKR"`)

* `CLP` (value: `"CLP"`)

* `CNY` (value: `"CNY"`)

* `COP` (value: `"COP"`)

* `KMF` (value: `"KMF"`)

* `CRC` (value: `"CRC"`)

* `HRK` (value: `"HRK"`)

* `CUP` (value: `"CUP"`)

* `CZK` (value: `"CZK"`)

* `DKK` (value: `"DKK"`)

* `DOP` (value: `"DOP"`)

* `SVC` (value: `"SVC"`)

* `ETB` (value: `"ETB"`)

* `ERN` (value: `"ERN"`)

* `FKP` (value: `"FKP"`)

* `FJD` (value: `"FJD"`)

* `DJF` (value: `"DJF"`)

* `GMD` (value: `"GMD"`)

* `GIP` (value: `"GIP"`)

* `GTQ` (value: `"GTQ"`)

* `GNF` (value: `"GNF"`)

* `GYD` (value: `"GYD"`)

* `HTG` (value: `"HTG"`)

* `HNL` (value: `"HNL"`)

* `HKD` (value: `"HKD"`)

* `HUF` (value: `"HUF"`)

* `ISK` (value: `"ISK"`)

* `INR` (value: `"INR"`)

* `IDR` (value: `"IDR"`)

* `IRR` (value: `"IRR"`)

* `IQD` (value: `"IQD"`)

* `ILS` (value: `"ILS"`)

* `JMD` (value: `"JMD"`)

* `JPY` (value: `"JPY"`)

* `KZT` (value: `"KZT"`)

* `JOD` (value: `"JOD"`)

* `KES` (value: `"KES"`)

* `KPW` (value: `"KPW"`)

* `KRW` (value: `"KRW"`)

* `KWD` (value: `"KWD"`)

* `KGS` (value: `"KGS"`)

* `LAK` (value: `"LAK"`)

* `LBP` (value: `"LBP"`)

* `LSL` (value: `"LSL"`)

* `LRD` (value: `"LRD"`)

* `LYD` (value: `"LYD"`)

* `MOP` (value: `"MOP"`)

* `MWK` (value: `"MWK"`)

* `MYR` (value: `"MYR"`)

* `MVR` (value: `"MVR"`)

* `MUR` (value: `"MUR"`)

* `MXN` (value: `"MXN"`)

* `MNT` (value: `"MNT"`)

* `MDL` (value: `"MDL"`)

* `MAD` (value: `"MAD"`)

* `OMR` (value: `"OMR"`)

* `NAD` (value: `"NAD"`)

* `NPR` (value: `"NPR"`)

* `ANG` (value: `"ANG"`)

* `AWG` (value: `"AWG"`)

* `VUV` (value: `"VUV"`)

* `NZD` (value: `"NZD"`)

* `NIO` (value: `"NIO"`)

* `NGN` (value: `"NGN"`)

* `NOK` (value: `"NOK"`)

* `PKR` (value: `"PKR"`)

* `PAB` (value: `"PAB"`)

* `PGK` (value: `"PGK"`)

* `PYG` (value: `"PYG"`)

* `PEN` (value: `"PEN"`)

* `PHP` (value: `"PHP"`)

* `QAR` (value: `"QAR"`)

* `RUB` (value: `"RUB"`)

* `RWF` (value: `"RWF"`)

* `SHP` (value: `"SHP"`)

* `SAR` (value: `"SAR"`)

* `SCR` (value: `"SCR"`)

* `SLL` (value: `"SLL"`)

* `SGD` (value: `"SGD"`)

* `VND` (value: `"VND"`)

* `SOS` (value: `"SOS"`)

* `ZAR` (value: `"ZAR"`)

* `SSP` (value: `"SSP"`)

* `SZL` (value: `"SZL"`)

* `SEK` (value: `"SEK"`)

* `CHF` (value: `"CHF"`)

* `SYP` (value: `"SYP"`)

* `THB` (value: `"THB"`)

* `TOP` (value: `"TOP"`)

* `TTD` (value: `"TTD"`)

* `AED` (value: `"AED"`)

* `TND` (value: `"TND"`)

* `UGX` (value: `"UGX"`)

* `MKD` (value: `"MKD"`)

* `EGP` (value: `"EGP"`)

* `GBP` (value: `"GBP"`)

* `TZS` (value: `"TZS"`)

* `USD` (value: `"USD"`)

* `UYU` (value: `"UYU"`)

* `UZS` (value: `"UZS"`)

* `WST` (value: `"WST"`)

* `YER` (value: `"YER"`)

* `TWD` (value: `"TWD"`)

* `UYW` (value: `"UYW"`)

* `VES` (value: `"VES"`)

* `MRU` (value: `"MRU"`)

* `STN` (value: `"STN"`)

* `CUC` (value: `"CUC"`)

* `ZWL` (value: `"ZWL"`)

* `BYN` (value: `"BYN"`)

* `TMT` (value: `"TMT"`)

* `GHS` (value: `"GHS"`)

* `SDG` (value: `"SDG"`)

* `UYI` (value: `"UYI"`)

* `RSD` (value: `"RSD"`)

* `MZN` (value: `"MZN"`)

* `AZN` (value: `"AZN"`)

* `RON` (value: `"RON"`)

* `CHE` (value: `"CHE"`)

* `CHW` (value: `"CHW"`)

* `TRY` (value: `"TRY"`)

* `XAF` (value: `"XAF"`)

* `XCD` (value: `"XCD"`)

* `XOF` (value: `"XOF"`)

* `XPF` (value: `"XPF"`)

* `XBA` (value: `"XBA"`)

* `XBB` (value: `"XBB"`)

* `XBC` (value: `"XBC"`)

* `XBD` (value: `"XBD"`)

* `XAU` (value: `"XAU"`)

* `XDR` (value: `"XDR"`)

* `XAG` (value: `"XAG"`)

* `XPT` (value: `"XPT"`)

* `XTS` (value: `"XTS"`)

* `XPD` (value: `"XPD"`)

* `XUA` (value: `"XUA"`)

* `ZMW` (value: `"ZMW"`)

* `SRD` (value: `"SRD"`)

* `MGA` (value: `"MGA"`)

* `COU` (value: `"COU"`)

* `AFN` (value: `"AFN"`)

* `TJS` (value: `"TJS"`)

* `AOA` (value: `"AOA"`)

* `BGN` (value: `"BGN"`)

* `CDF` (value: `"CDF"`)

* `BAM` (value: `"BAM"`)

* `EUR` (value: `"EUR"`)

* `MXV` (value: `"MXV"`)

* `UAH` (value: `"UAH"`)

* `GEL` (value: `"GEL"`)

* `BOV` (value: `"BOV"`)

* `PLN` (value: `"PLN"`)

* `BRL` (value: `"BRL"`)

* `CLF` (value: `"CLF"`)

* `XSU` (value: `"XSU"`)

* `USN` (value: `"USN"`)





## Enum: IntentEnum


* `authorization` (value: `"authorization"`)

* `preauthorization` (value: `"preauthorization"`)





## Enum: LanguageEnum


* `de_DE` (value: `"de_DE"`)

* `en_US` (value: `"en_US"`)





## Enum: ModeEnum


* `live` (value: `"live"`)

* `test` (value: `"test"`)





## Enum: [PaymentMethodsEnum]


* `visa` (value: `"visa"`)

* `mastercard` (value: `"mastercard"`)

* `amex` (value: `"amex"`)

* `paypal` (value: `"paypal"`)

* `sofort` (value: `"sofort"`)

* `paydirekt` (value: `"paydirekt"`)

* `postfinance-e` (value: `"postfinance-e"`)

* `postfinance-card` (value: `"postfinance-card"`)

* `bancontact` (value: `"bancontact"`)

* `przelewy24` (value: `"przelewy24"`)

* `alipay` (value: `"alipay"`)

* `ideal` (value: `"ideal"`)

* `eps` (value: `"eps"`)

* `giropay` (value: `"giropay"`)

* `sepa` (value: `"sepa"`)




