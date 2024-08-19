# VisualSearchClient.Offer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregateRating** | [**AggregateRating**](AggregateRating.md) |  | [optional] 
**availability** | **String** | The item&#39;s availability. The following are the possible values: Discontinued, InStock, InStoreOnly, LimitedAvailability, OnlineOnly, OutOfStock, PreOrder, SoldOut. | [optional] [readonly] 
**lastUpdated** | **String** | The last date that the offer was updated. The date is in the form YYYY-MM-DD. | [optional] [readonly] 
**price** | **Number** | The item&#39;s price. | [optional] [readonly] 
**priceCurrency** | **String** | The monetary currency. For example, USD. | [optional] [readonly] [default to &#39;USD&#39;]
**seller** | [**Organization**](Organization.md) |  | [optional] 



## Enum: AvailabilityEnum


* `Discontinued` (value: `"Discontinued"`)

* `InStock` (value: `"InStock"`)

* `InStoreOnly` (value: `"InStoreOnly"`)

* `LimitedAvailability` (value: `"LimitedAvailability"`)

* `OnlineOnly` (value: `"OnlineOnly"`)

* `OutOfStock` (value: `"OutOfStock"`)

* `PreOrder` (value: `"PreOrder"`)

* `SoldOut` (value: `"SoldOut"`)





## Enum: PriceCurrencyEnum


* `USD` (value: `"USD"`)

* `CAD` (value: `"CAD"`)

* `GBP` (value: `"GBP"`)

* `EUR` (value: `"EUR"`)

* `COP` (value: `"COP"`)

* `JPY` (value: `"JPY"`)

* `CNY` (value: `"CNY"`)

* `AUD` (value: `"AUD"`)

* `INR` (value: `"INR"`)

* `AED` (value: `"AED"`)

* `AFN` (value: `"AFN"`)

* `ALL` (value: `"ALL"`)

* `AMD` (value: `"AMD"`)

* `ANG` (value: `"ANG"`)

* `AOA` (value: `"AOA"`)

* `ARS` (value: `"ARS"`)

* `AWG` (value: `"AWG"`)

* `AZN` (value: `"AZN"`)

* `BAM` (value: `"BAM"`)

* `BBD` (value: `"BBD"`)

* `BDT` (value: `"BDT"`)

* `BGN` (value: `"BGN"`)

* `BHD` (value: `"BHD"`)

* `BIF` (value: `"BIF"`)

* `BMD` (value: `"BMD"`)

* `BND` (value: `"BND"`)

* `BOB` (value: `"BOB"`)

* `BOV` (value: `"BOV"`)

* `BRL` (value: `"BRL"`)

* `BSD` (value: `"BSD"`)

* `BTN` (value: `"BTN"`)

* `BWP` (value: `"BWP"`)

* `BYR` (value: `"BYR"`)

* `BZD` (value: `"BZD"`)

* `CDF` (value: `"CDF"`)

* `CHE` (value: `"CHE"`)

* `CHF` (value: `"CHF"`)

* `CHW` (value: `"CHW"`)

* `CLF` (value: `"CLF"`)

* `CLP` (value: `"CLP"`)

* `COU` (value: `"COU"`)

* `CRC` (value: `"CRC"`)

* `CUC` (value: `"CUC"`)

* `CUP` (value: `"CUP"`)

* `CVE` (value: `"CVE"`)

* `CZK` (value: `"CZK"`)

* `DJF` (value: `"DJF"`)

* `DKK` (value: `"DKK"`)

* `DOP` (value: `"DOP"`)

* `DZD` (value: `"DZD"`)

* `EGP` (value: `"EGP"`)

* `ERN` (value: `"ERN"`)

* `ETB` (value: `"ETB"`)

* `FJD` (value: `"FJD"`)

* `FKP` (value: `"FKP"`)

* `GEL` (value: `"GEL"`)

* `GHS` (value: `"GHS"`)

* `GIP` (value: `"GIP"`)

* `GMD` (value: `"GMD"`)

* `GNF` (value: `"GNF"`)

* `GTQ` (value: `"GTQ"`)

* `GYD` (value: `"GYD"`)

* `HKD` (value: `"HKD"`)

* `HNL` (value: `"HNL"`)

* `HRK` (value: `"HRK"`)

* `HTG` (value: `"HTG"`)

* `HUF` (value: `"HUF"`)

* `IDR` (value: `"IDR"`)

* `ILS` (value: `"ILS"`)

* `IQD` (value: `"IQD"`)

* `IRR` (value: `"IRR"`)

* `ISK` (value: `"ISK"`)

* `JMD` (value: `"JMD"`)

* `JOD` (value: `"JOD"`)

* `KES` (value: `"KES"`)

* `KGS` (value: `"KGS"`)

* `KHR` (value: `"KHR"`)

* `KMF` (value: `"KMF"`)

* `KPW` (value: `"KPW"`)

* `KRW` (value: `"KRW"`)

* `KWD` (value: `"KWD"`)

* `KYD` (value: `"KYD"`)

* `KZT` (value: `"KZT"`)

* `LAK` (value: `"LAK"`)

* `LBP` (value: `"LBP"`)

* `LKR` (value: `"LKR"`)

* `LRD` (value: `"LRD"`)

* `LSL` (value: `"LSL"`)

* `LYD` (value: `"LYD"`)

* `MAD` (value: `"MAD"`)

* `MDL` (value: `"MDL"`)

* `MGA` (value: `"MGA"`)

* `MKD` (value: `"MKD"`)

* `MMK` (value: `"MMK"`)

* `MNT` (value: `"MNT"`)

* `MOP` (value: `"MOP"`)

* `MRO` (value: `"MRO"`)

* `MUR` (value: `"MUR"`)

* `MVR` (value: `"MVR"`)

* `MWK` (value: `"MWK"`)

* `MXN` (value: `"MXN"`)

* `MXV` (value: `"MXV"`)

* `MYR` (value: `"MYR"`)

* `MZN` (value: `"MZN"`)

* `NAD` (value: `"NAD"`)

* `NGN` (value: `"NGN"`)

* `NIO` (value: `"NIO"`)

* `NOK` (value: `"NOK"`)

* `NPR` (value: `"NPR"`)

* `NZD` (value: `"NZD"`)

* `OMR` (value: `"OMR"`)

* `PAB` (value: `"PAB"`)

* `PEN` (value: `"PEN"`)

* `PGK` (value: `"PGK"`)

* `PHP` (value: `"PHP"`)

* `PKR` (value: `"PKR"`)

* `PLN` (value: `"PLN"`)

* `PYG` (value: `"PYG"`)

* `QAR` (value: `"QAR"`)

* `RON` (value: `"RON"`)

* `RSD` (value: `"RSD"`)

* `RUB` (value: `"RUB"`)

* `RWF` (value: `"RWF"`)

* `SAR` (value: `"SAR"`)

* `SBD` (value: `"SBD"`)

* `SCR` (value: `"SCR"`)

* `SDG` (value: `"SDG"`)

* `SEK` (value: `"SEK"`)

* `SGD` (value: `"SGD"`)

* `SHP` (value: `"SHP"`)

* `SLL` (value: `"SLL"`)

* `SOS` (value: `"SOS"`)

* `SRD` (value: `"SRD"`)

* `SSP` (value: `"SSP"`)

* `STD` (value: `"STD"`)

* `SYP` (value: `"SYP"`)

* `SZL` (value: `"SZL"`)

* `THB` (value: `"THB"`)

* `TJS` (value: `"TJS"`)

* `TMT` (value: `"TMT"`)

* `TND` (value: `"TND"`)

* `TOP` (value: `"TOP"`)

* `TRY` (value: `"TRY"`)

* `TTD` (value: `"TTD"`)

* `TWD` (value: `"TWD"`)

* `TZS` (value: `"TZS"`)

* `UAH` (value: `"UAH"`)

* `UGX` (value: `"UGX"`)

* `UYU` (value: `"UYU"`)

* `UZS` (value: `"UZS"`)

* `VEF` (value: `"VEF"`)

* `VND` (value: `"VND"`)

* `VUV` (value: `"VUV"`)

* `WST` (value: `"WST"`)

* `XAF` (value: `"XAF"`)

* `XCD` (value: `"XCD"`)

* `XOF` (value: `"XOF"`)

* `XPF` (value: `"XPF"`)

* `YER` (value: `"YER"`)

* `ZAR` (value: `"ZAR"`)

* `ZMW` (value: `"ZMW"`)




