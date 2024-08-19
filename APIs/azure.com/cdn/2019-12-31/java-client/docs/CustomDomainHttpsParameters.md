

# CustomDomainHttpsParameters

The JSON object that contains the properties to secure a custom domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateSource** | [**CertificateSourceEnum**](#CertificateSourceEnum) | Defines the source of the SSL certificate. |  |
|**minimumTlsVersion** | [**MinimumTlsVersionEnum**](#MinimumTlsVersionEnum) | TLS protocol version that will be used for Https |  [optional] |
|**protocolType** | [**ProtocolTypeEnum**](#ProtocolTypeEnum) | Defines the TLS extension protocol that is used for secure delivery. |  |



## Enum: CertificateSourceEnum

| Name | Value |
|---- | -----|
| AZURE_KEY_VAULT | &quot;AzureKeyVault&quot; |
| CDN | &quot;Cdn&quot; |



## Enum: MinimumTlsVersionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| TLS10 | &quot;TLS10&quot; |
| TLS12 | &quot;TLS12&quot; |



## Enum: ProtocolTypeEnum

| Name | Value |
|---- | -----|
| SERVER_NAME_INDICATION | &quot;ServerNameIndication&quot; |
| IP_BASED | &quot;IPBased&quot; |



