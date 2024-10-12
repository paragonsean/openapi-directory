# RebillyRestApi.IpayOptionsAllOfSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardType** | **String** | Manually set the card_type for iDEAL. | [optional] 
**extraStep** | **Boolean** | Show extra step for user to enter their email and DNI number. | [optional] 
**platform** | **String** | Platform which IpayOptions will process. | [optional] 
**subdomain** | **String** | Subdomain to use when sending request to IpayOptions. | [optional] 



## Enum: CardTypeEnum


* `ideal` (value: `"ideal"`)

* `idealqr` (value: `"idealqr"`)

* `sofort` (value: `"sofort"`)





## Enum: PlatformEnum


* `SOAP` (value: `"SOAP"`)

* `TxHandler` (value: `"TxHandler"`)

* `SecureHosted` (value: `"SecureHosted"`)





## Enum: SubdomainEnum


* `miglite` (value: `"miglite"`)

* `w88asiapay` (value: `"w88asiapay"`)




