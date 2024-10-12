

# ClientTlsPolicy

ClientTlsPolicy is a resource that specifies how a client should authenticate connections to backends of a service. This resource itself does not affect configuration unless it is attached to a backend service resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientCertificate** | [**GoogleCloudNetworksecurityV1beta1CertificateProvider**](GoogleCloudNetworksecurityV1beta1CertificateProvider.md) |  |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Free-text description of the resource. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the resource. |  [optional] |
|**name** | **String** | Required. Name of the ClientTlsPolicy resource. It matches the pattern &#x60;projects/_*_/locations/{location}/clientTlsPolicies/{client_tls_policy}&#x60; |  [optional] |
|**serverValidationCa** | [**List&lt;ValidationCA&gt;**](ValidationCA.md) | Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate. |  [optional] |
|**sni** | **String** | Optional. Server Name Indication string to present to the server during TLS handshake. E.g: \&quot;secure.example.com\&quot;. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



