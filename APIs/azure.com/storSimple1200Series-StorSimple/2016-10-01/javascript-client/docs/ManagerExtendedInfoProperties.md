# StorSimpleManagementClient.ManagerExtendedInfoProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Represents the encryption algorithm used to encrypt the other keys. None - if EncryptionKey is saved in plain text format. AlgorithmName - if encryption is used | 
**encryptionKey** | **String** | Represents the CEK of the resource | [optional] 
**encryptionKeyThumbprint** | **String** | Represents the Cert thumbprint that was used to encrypt the CEK | [optional] 
**integrityKey** | **String** | Represents the CIK of the resource | 
**portalCertificateThumbprint** | **String** | Represents the portal thumbprint which can be used optionally to encrypt the entire data before storing it. | [optional] 
**version** | **String** | Represents the version of the ExtendedInfo object being persisted | [optional] 


