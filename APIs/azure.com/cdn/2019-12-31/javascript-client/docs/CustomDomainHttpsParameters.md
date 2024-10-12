# CdnManagementClient.CustomDomainHttpsParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateSource** | **String** | Defines the source of the SSL certificate. | 
**minimumTlsVersion** | **String** | TLS protocol version that will be used for Https | [optional] 
**protocolType** | **String** | Defines the TLS extension protocol that is used for secure delivery. | 



## Enum: CertificateSourceEnum


* `AzureKeyVault` (value: `"AzureKeyVault"`)

* `Cdn` (value: `"Cdn"`)





## Enum: MinimumTlsVersionEnum


* `None` (value: `"None"`)

* `TLS10` (value: `"TLS10"`)

* `TLS12` (value: `"TLS12"`)





## Enum: ProtocolTypeEnum


* `ServerNameIndication` (value: `"ServerNameIndication"`)

* `IPBased` (value: `"IPBased"`)




