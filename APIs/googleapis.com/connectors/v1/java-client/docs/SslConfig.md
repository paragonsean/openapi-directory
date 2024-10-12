

# SslConfig

SSL Configuration of a connection

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalVariables** | [**List&lt;ConfigVariable&gt;**](ConfigVariable.md) | Additional SSL related field values |  [optional] |
|**clientCertType** | [**ClientCertTypeEnum**](#ClientCertTypeEnum) | Type of Client Cert (PEM/JKS/.. etc.) |  [optional] |
|**clientCertificate** | [**Secret**](Secret.md) |  |  [optional] |
|**clientPrivateKey** | [**Secret**](Secret.md) |  |  [optional] |
|**clientPrivateKeyPass** | [**Secret**](Secret.md) |  |  [optional] |
|**privateServerCertificate** | [**Secret**](Secret.md) |  |  [optional] |
|**serverCertType** | [**ServerCertTypeEnum**](#ServerCertTypeEnum) | Type of Server Cert (PEM/JKS/.. etc.) |  [optional] |
|**trustModel** | [**TrustModelEnum**](#TrustModelEnum) | Trust Model of the SSL connection |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Controls the ssl type for the given connector version. |  [optional] |
|**useSsl** | **Boolean** | Bool for enabling SSL |  [optional] |



## Enum: ClientCertTypeEnum

| Name | Value |
|---- | -----|
| CERT_TYPE_UNSPECIFIED | &quot;CERT_TYPE_UNSPECIFIED&quot; |
| PEM | &quot;PEM&quot; |



## Enum: ServerCertTypeEnum

| Name | Value |
|---- | -----|
| CERT_TYPE_UNSPECIFIED | &quot;CERT_TYPE_UNSPECIFIED&quot; |
| PEM | &quot;PEM&quot; |



## Enum: TrustModelEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;PUBLIC&quot; |
| PRIVATE | &quot;PRIVATE&quot; |
| INSECURE | &quot;INSECURE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SSL_TYPE_UNSPECIFIED | &quot;SSL_TYPE_UNSPECIFIED&quot; |
| TLS | &quot;TLS&quot; |
| MTLS | &quot;MTLS&quot; |



