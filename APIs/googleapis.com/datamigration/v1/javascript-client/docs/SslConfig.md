# DatabaseMigrationApi.SslConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caCertificate** | **String** | Required. Input only. The x509 PEM-encoded certificate of the CA that signed the source database server&#39;s certificate. The replica will use this certificate to verify it&#39;s connecting to the right host. | [optional] 
**clientCertificate** | **String** | Input only. The x509 PEM-encoded certificate that will be used by the replica to authenticate against the source database server.If this field is used then the &#39;client_key&#39; field is mandatory. | [optional] 
**clientKey** | **String** | Input only. The unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. If this field is used then the &#39;client_certificate&#39; field is mandatory. | [optional] 
**type** | **String** | Output only. The ssl config type according to &#39;client_key&#39;, &#39;client_certificate&#39; and &#39;ca_certificate&#39;. | [optional] [readonly] 



## Enum: TypeEnum


* `SSL_TYPE_UNSPECIFIED` (value: `"SSL_TYPE_UNSPECIFIED"`)

* `SERVER_ONLY` (value: `"SERVER_ONLY"`)

* `SERVER_CLIENT` (value: `"SERVER_CLIENT"`)




