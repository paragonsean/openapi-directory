# PublicApi.SslCertificateRequestValidation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoValidated** | **Boolean** | Returns true if no user interaction is required and the domain validation will be verified automatic. | [optional] 
**cnameValidationContent** | **String** | The value-part (Point To) of the CNAME-record that must be created as part of domain verification. | [optional] 
**cnameValidationName** | **String** | The host-part (Name) of the CNAME-record that must be created as part of domain verification. | [optional] 
**dnsName** | **String** | A domain name of the certificate. | [optional] 
**emailAddresses** | **[String]** | An array of eligible domain verification email addresses. | [optional] 
**fileValidationContent** | **[String]** | The content your verification file must contain, consisting of three lines of plain-text. | [optional] 
**fileValidationUrlHttp** | **String** | The URL (http format) your verification file must be uploaded to as part of domain verification. | [optional] 
**fileValidationUrlHttps** | **String** | The URL (https format) your verification file must be uploaded to as part of domain verification. | [optional] 
**type** | [**SslCertificateRequestValidationType**](SslCertificateRequestValidationType.md) |  | [optional] 


