# FrontDoorManagementClient.CustomHttpsConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateSource** | **String** | Defines the source of the SSL certificate | [optional] 
**frontDoorCertificateSourceParameters** | [**FrontDoorCertificateSourceParameters**](FrontDoorCertificateSourceParameters.md) |  | [optional] 
**keyVaultCertificateSourceParameters** | [**KeyVaultCertificateSourceParameters**](KeyVaultCertificateSourceParameters.md) |  | [optional] 
**protocolType** | **String** | Defines the TLS extension protocol that is used for secure delivery | [optional] 



## Enum: CertificateSourceEnum


* `AzureKeyVault` (value: `"AzureKeyVault"`)

* `FrontDoor` (value: `"FrontDoor"`)





## Enum: ProtocolTypeEnum


* `ServerNameIndication` (value: `"ServerNameIndication"`)




