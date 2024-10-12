

# MysqlSslConfig

MySQL SSL configuration information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caCertificate** | **String** | Input only. PEM-encoded certificate of the CA that signed the source database server&#39;s certificate. |  [optional] |
|**caCertificateSet** | **Boolean** | Output only. Indicates whether the ca_certificate field is set. |  [optional] [readonly] |
|**clientCertificate** | **String** | Input only. PEM-encoded certificate that will be used by the replica to authenticate against the source database server. If this field is used then the &#39;client_key&#39; and the &#39;ca_certificate&#39; fields are mandatory. |  [optional] |
|**clientCertificateSet** | **Boolean** | Output only. Indicates whether the client_certificate field is set. |  [optional] [readonly] |
|**clientKey** | **String** | Input only. PEM-encoded private key associated with the Client Certificate. If this field is used then the &#39;client_certificate&#39; and the &#39;ca_certificate&#39; fields are mandatory. |  [optional] |
|**clientKeySet** | **Boolean** | Output only. Indicates whether the client_key field is set. |  [optional] [readonly] |



