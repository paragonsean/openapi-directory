# AlloyDbApi.GenerateClientCertificateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caCert** | **String** | Optional. The pem-encoded cluster ca X.509 certificate. | [optional] 
**pemCertificate** | **String** | Output only. The pem-encoded, signed X.509 certificate. | [optional] [readonly] 
**pemCertificateChain** | **[String]** | Output only. The pem-encoded chain that may be used to verify the X.509 certificate. Expected to be in issuer-to-root order according to RFC 5246. | [optional] [readonly] 


