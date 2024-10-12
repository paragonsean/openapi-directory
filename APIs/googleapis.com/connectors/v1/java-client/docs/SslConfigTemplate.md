

# SslConfigTemplate

Ssl config details of a connector version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalVariables** | [**List&lt;ConfigVariableTemplate&gt;**](ConfigVariableTemplate.md) | Any additional fields that need to be rendered |  [optional] |
|**clientCertType** | [**List&lt;ClientCertTypeEnum&gt;**](#List&lt;ClientCertTypeEnum&gt;) | List of supported Client Cert Types |  [optional] |
|**isTlsMandatory** | **Boolean** | Boolean for determining if the connector version mandates TLS. |  [optional] |
|**serverCertType** | [**List&lt;ServerCertTypeEnum&gt;**](#List&lt;ServerCertTypeEnum&gt;) | List of supported Server Cert Types |  [optional] |
|**sslType** | [**SslTypeEnum**](#SslTypeEnum) | Controls the ssl type for the given connector version |  [optional] |



## Enum: List&lt;ClientCertTypeEnum&gt;

| Name | Value |
|---- | -----|
| CERT_TYPE_UNSPECIFIED | &quot;CERT_TYPE_UNSPECIFIED&quot; |
| PEM | &quot;PEM&quot; |



## Enum: List&lt;ServerCertTypeEnum&gt;

| Name | Value |
|---- | -----|
| CERT_TYPE_UNSPECIFIED | &quot;CERT_TYPE_UNSPECIFIED&quot; |
| PEM | &quot;PEM&quot; |



## Enum: SslTypeEnum

| Name | Value |
|---- | -----|
| SSL_TYPE_UNSPECIFIED | &quot;SSL_TYPE_UNSPECIFIED&quot; |
| TLS | &quot;TLS&quot; |
| MTLS | &quot;MTLS&quot; |



