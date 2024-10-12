# KeyVaultClient.CertificateOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellationRequested** | **Boolean** | Indicates if cancellation was requested on the certificate operation. | [optional] 
**csr** | **Blob** | The certificate signing request (CSR) that is being used in the certificate operation. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**id** | **String** | The certificate id. | [optional] [readonly] 
**issuer** | [**IssuerParameters**](IssuerParameters.md) |  | [optional] 
**requestId** | **String** | Identifier for the certificate operation. | [optional] 
**status** | **String** | Status of the certificate operation. | [optional] 
**statusDetails** | **String** | The status details of the certificate operation. | [optional] 
**target** | **String** | Location which contains the result of the certificate operation. | [optional] 


