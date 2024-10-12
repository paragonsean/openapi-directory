# AwsSigner.RevokeSigningProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profileVersion** | **String** | The version of the signing profile to be revoked. | 
**reason** | **String** | The reason for revoking a signing profile. | 
**effectiveTime** | **Date** | A timestamp for when revocation of a Signing Profile should become effective. Signatures generated using the signing profile after this timestamp are not trusted. | 


