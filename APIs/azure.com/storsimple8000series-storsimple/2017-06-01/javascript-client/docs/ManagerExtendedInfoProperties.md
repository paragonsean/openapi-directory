# StorSimple8000SeriesManagementClient.ManagerExtendedInfoProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Represents the encryption algorithm used to encrypt the keys. None - if Key is saved in plain text format. Algorithm name - if key is encrypted | 
**encryptionKey** | **String** | Represents the CEK of the resource. | [optional] 
**encryptionKeyThumbprint** | **String** | Represents the Cert thumbprint that was used to encrypt the CEK. | [optional] 
**integrityKey** | **String** | Represents the CIK of the resource. | 
**portalCertificateThumbprint** | **String** | Represents the portal thumbprint which can be used optionally to encrypt the entire data before storing it. | [optional] 
**version** | **String** | The version of the extended info being persisted. | [optional] 


