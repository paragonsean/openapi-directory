# RubrikRestApi.CertificateSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certId** | **String** | ID of the certificate. | 
**description** | **String** | User-friendly description for the certificate. | [optional] 
**expiration** | **Date** | The expiration date for the certificate. | 
**hasKey** | **Boolean** | A Boolean value that specifies whether or not the certificate is associated with a stored private key. When this value is &#39;true,&#39; the private key for the certificate is stored. When this value is &#39;false,&#39; the private key for the certificate is not stored. | 
**name** | **String** | Display name for the certificate. | 
**pemFile** | **String** | The certificates, in PEM format. | 
**usedBy** | **String** | A list of components using the certificate. | 


