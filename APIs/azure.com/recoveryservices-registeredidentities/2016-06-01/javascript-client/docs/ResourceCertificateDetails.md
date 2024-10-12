# RecoveryServicesClient.ResourceCertificateDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authType** | **String** | This property will be used as the discriminator for deciding the specific types in the polymorphic chain of types. | 
**certificate** | **Blob** | The base64 encoded certificate raw data string. | [optional] 
**friendlyName** | **String** | Certificate friendly name. | [optional] 
**issuer** | **String** | Certificate issuer. | [optional] 
**resourceId** | **Number** | Resource ID of the vault. | [optional] 
**subject** | **String** | Certificate Subject Name. | [optional] 
**thumbprint** | **String** | Certificate thumbprint. | [optional] 
**validFrom** | **Date** | Certificate Validity start Date time. | [optional] 
**validTo** | **Date** | Certificate Validity End Date time. | [optional] 


