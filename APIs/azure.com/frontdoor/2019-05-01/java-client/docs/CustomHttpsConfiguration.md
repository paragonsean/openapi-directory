

# CustomHttpsConfiguration

Https settings for a domain

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateSource** | [**CertificateSourceEnum**](#CertificateSourceEnum) | Defines the source of the SSL certificate |  |
|**frontDoorCertificateSourceParameters** | [**FrontDoorCertificateSourceParameters**](FrontDoorCertificateSourceParameters.md) |  |  [optional] |
|**keyVaultCertificateSourceParameters** | [**KeyVaultCertificateSourceParameters**](KeyVaultCertificateSourceParameters.md) |  |  [optional] |
|**minimumTlsVersion** | [**MinimumTlsVersionEnum**](#MinimumTlsVersionEnum) | The minimum TLS version required from the clients to establish an SSL handshake with Front Door. |  |
|**protocolType** | [**ProtocolTypeEnum**](#ProtocolTypeEnum) | Defines the TLS extension protocol that is used for secure delivery |  |



## Enum: CertificateSourceEnum

| Name | Value |
|---- | -----|
| AZURE_KEY_VAULT | &quot;AzureKeyVault&quot; |
| FRONT_DOOR | &quot;FrontDoor&quot; |



## Enum: MinimumTlsVersionEnum

| Name | Value |
|---- | -----|
| _0 | &quot;1.0&quot; |
| _2 | &quot;1.2&quot; |



## Enum: ProtocolTypeEnum

| Name | Value |
|---- | -----|
| SERVER_NAME_INDICATION | &quot;ServerNameIndication&quot; |



