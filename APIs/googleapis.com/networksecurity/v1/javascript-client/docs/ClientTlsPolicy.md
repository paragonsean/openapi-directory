# NetworkSecurityApi.ClientTlsPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientCertificate** | [**GoogleCloudNetworksecurityV1CertificateProvider**](GoogleCloudNetworksecurityV1CertificateProvider.md) |  | [optional] 
**createTime** | **String** | Output only. The timestamp when the resource was created. | [optional] [readonly] 
**description** | **String** | Optional. Free-text description of the resource. | [optional] 
**labels** | **{String: String}** | Optional. Set of label tags associated with the resource. | [optional] 
**name** | **String** | Required. Name of the ClientTlsPolicy resource. It matches the pattern &#x60;projects/_*_/locations/{location}/clientTlsPolicies/{client_tls_policy}&#x60; | [optional] 
**serverValidationCa** | [**[ValidationCA]**](ValidationCA.md) | Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate. | [optional] 
**sni** | **String** | Optional. Server Name Indication string to present to the server during TLS handshake. E.g: \&quot;secure.example.com\&quot;. | [optional] 
**updateTime** | **String** | Output only. The timestamp when the resource was updated. | [optional] [readonly] 


