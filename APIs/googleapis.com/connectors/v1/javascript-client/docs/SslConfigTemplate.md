# ConnectorsApi.SslConfigTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalVariables** | [**[ConfigVariableTemplate]**](ConfigVariableTemplate.md) | Any additional fields that need to be rendered | [optional] 
**clientCertType** | **[String]** | List of supported Client Cert Types | [optional] 
**isTlsMandatory** | **Boolean** | Boolean for determining if the connector version mandates TLS. | [optional] 
**serverCertType** | **[String]** | List of supported Server Cert Types | [optional] 
**sslType** | **String** | Controls the ssl type for the given connector version | [optional] 



## Enum: [ClientCertTypeEnum]


* `CERT_TYPE_UNSPECIFIED` (value: `"CERT_TYPE_UNSPECIFIED"`)

* `PEM` (value: `"PEM"`)





## Enum: [ServerCertTypeEnum]


* `CERT_TYPE_UNSPECIFIED` (value: `"CERT_TYPE_UNSPECIFIED"`)

* `PEM` (value: `"PEM"`)





## Enum: SslTypeEnum


* `SSL_TYPE_UNSPECIFIED` (value: `"SSL_TYPE_UNSPECIFIED"`)

* `TLS` (value: `"TLS"`)

* `MTLS` (value: `"MTLS"`)




