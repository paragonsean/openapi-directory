

# SslCertificateRequestDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateType** | **SslCertificateType** |  |  [optional] |
|**commonName** | **String** | The common name of the certificate request. |  [optional] |
|**id** | **Integer** | The id of the certificate request. |  [optional] |
|**orderCode** | **String** | The order code of the certificate request. |  [optional] |
|**subjectAltNames** | [**List&lt;SslSubjectAltName&gt;**](SslSubjectAltName.md) | The list of all supported domains in the certificate. |  [optional] |
|**validationLevel** | **SslCertificateValidationLevel** |  |  [optional] |
|**validations** | [**List&lt;SslCertificateRequestValidation&gt;**](SslCertificateRequestValidation.md) | The list of dns names to be validated with the information related to domain verification. |  [optional] |
|**vendor** | **SslCertificateVendor** |  |  [optional] |



