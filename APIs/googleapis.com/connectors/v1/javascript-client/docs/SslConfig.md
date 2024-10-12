# ConnectorsApi.SslConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalVariables** | [**[ConfigVariable]**](ConfigVariable.md) | Additional SSL related field values | [optional] 
**clientCertType** | **String** | Type of Client Cert (PEM/JKS/.. etc.) | [optional] 
**clientCertificate** | [**Secret**](Secret.md) |  | [optional] 
**clientPrivateKey** | [**Secret**](Secret.md) |  | [optional] 
**clientPrivateKeyPass** | [**Secret**](Secret.md) |  | [optional] 
**privateServerCertificate** | [**Secret**](Secret.md) |  | [optional] 
**serverCertType** | **String** | Type of Server Cert (PEM/JKS/.. etc.) | [optional] 
**trustModel** | **String** | Trust Model of the SSL connection | [optional] 
**type** | **String** | Controls the ssl type for the given connector version. | [optional] 
**useSsl** | **Boolean** | Bool for enabling SSL | [optional] 



## Enum: ClientCertTypeEnum


* `CERT_TYPE_UNSPECIFIED` (value: `"CERT_TYPE_UNSPECIFIED"`)

* `PEM` (value: `"PEM"`)





## Enum: ServerCertTypeEnum


* `CERT_TYPE_UNSPECIFIED` (value: `"CERT_TYPE_UNSPECIFIED"`)

* `PEM` (value: `"PEM"`)





## Enum: TrustModelEnum


* `PUBLIC` (value: `"PUBLIC"`)

* `PRIVATE` (value: `"PRIVATE"`)

* `INSECURE` (value: `"INSECURE"`)





## Enum: TypeEnum


* `SSL_TYPE_UNSPECIFIED` (value: `"SSL_TYPE_UNSPECIFIED"`)

* `TLS` (value: `"TLS"`)

* `MTLS` (value: `"MTLS"`)




