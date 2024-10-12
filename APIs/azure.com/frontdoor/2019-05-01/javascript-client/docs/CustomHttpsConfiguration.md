# FrontDoorManagementClient.CustomHttpsConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateSource** | **String** | Defines the source of the SSL certificate | 
**frontDoorCertificateSourceParameters** | [**FrontDoorCertificateSourceParameters**](FrontDoorCertificateSourceParameters.md) |  | [optional] 
**keyVaultCertificateSourceParameters** | [**KeyVaultCertificateSourceParameters**](KeyVaultCertificateSourceParameters.md) |  | [optional] 
**minimumTlsVersion** | **String** | The minimum TLS version required from the clients to establish an SSL handshake with Front Door. | 
**protocolType** | **String** | Defines the TLS extension protocol that is used for secure delivery | 



## Enum: CertificateSourceEnum


* `AzureKeyVault` (value: `"AzureKeyVault"`)

* `FrontDoor` (value: `"FrontDoor"`)





## Enum: MinimumTlsVersionEnum


* `0` (value: `"1.0"`)

* `2` (value: `"1.2"`)





## Enum: ProtocolTypeEnum


* `ServerNameIndication` (value: `"ServerNameIndication"`)




