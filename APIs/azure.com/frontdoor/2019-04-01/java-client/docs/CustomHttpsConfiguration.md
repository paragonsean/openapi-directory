

# CustomHttpsConfiguration

Https settings for a domain

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateSource** | [**CertificateSourceEnum**](#CertificateSourceEnum) | Defines the source of the SSL certificate |  [optional] |
|**frontDoorCertificateSourceParameters** | [**FrontDoorCertificateSourceParameters**](FrontDoorCertificateSourceParameters.md) |  |  [optional] |
|**keyVaultCertificateSourceParameters** | [**KeyVaultCertificateSourceParameters**](KeyVaultCertificateSourceParameters.md) |  |  [optional] |
|**protocolType** | [**ProtocolTypeEnum**](#ProtocolTypeEnum) | Defines the TLS extension protocol that is used for secure delivery |  [optional] |



## Enum: CertificateSourceEnum

| Name | Value |
|---- | -----|
| AZURE_KEY_VAULT | &quot;AzureKeyVault&quot; |
| FRONT_DOOR | &quot;FrontDoor&quot; |



## Enum: ProtocolTypeEnum

| Name | Value |
|---- | -----|
| SERVER_NAME_INDICATION | &quot;ServerNameIndication&quot; |



