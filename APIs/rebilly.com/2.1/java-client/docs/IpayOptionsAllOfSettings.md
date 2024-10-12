

# IpayOptionsAllOfSettings

Ipay Options settings object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardType** | [**CardTypeEnum**](#CardTypeEnum) | Manually set the card_type for iDEAL. |  [optional] |
|**extraStep** | **Boolean** | Show extra step for user to enter their email and DNI number. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform which IpayOptions will process. |  [optional] |
|**subdomain** | [**SubdomainEnum**](#SubdomainEnum) | Subdomain to use when sending request to IpayOptions. |  [optional] |



## Enum: CardTypeEnum

| Name | Value |
|---- | -----|
| IDEAL | &quot;ideal&quot; |
| IDEALQR | &quot;idealqr&quot; |
| SOFORT | &quot;sofort&quot; |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SOAP | &quot;SOAP&quot; |
| TX_HANDLER | &quot;TxHandler&quot; |
| SECURE_HOSTED | &quot;SecureHosted&quot; |



## Enum: SubdomainEnum

| Name | Value |
|---- | -----|
| MIGLITE | &quot;miglite&quot; |
| W88ASIAPAY | &quot;w88asiapay&quot; |



