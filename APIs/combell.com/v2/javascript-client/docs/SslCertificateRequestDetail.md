# PublicApi.SslCertificateRequestDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateType** | [**SslCertificateType**](SslCertificateType.md) |  | [optional] 
**commonName** | **String** | The common name of the certificate request. | [optional] 
**id** | **Number** | The id of the certificate request. | [optional] 
**orderCode** | **String** | The order code of the certificate request. | [optional] 
**subjectAltNames** | [**[SslSubjectAltName]**](SslSubjectAltName.md) | The list of all supported domains in the certificate. | [optional] 
**validationLevel** | [**SslCertificateValidationLevel**](SslCertificateValidationLevel.md) |  | [optional] 
**validations** | [**[SslCertificateRequestValidation]**](SslCertificateRequestValidation.md) | The list of dns names to be validated with the information related to domain verification. | [optional] 
**vendor** | [**SslCertificateVendor**](SslCertificateVendor.md) |  | [optional] 


