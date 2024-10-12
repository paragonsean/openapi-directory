# GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyUploadAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowOverwrite** | **Boolean** | Whether allow overwrite existing account when user local_id exists. | [optional] 
**blockSize** | **Number** |  | [optional] 
**cpuMemCost** | **Number** | The following 4 fields are for standard scrypt algorithm. | [optional] 
**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. | [optional] 
**dkLen** | **Number** |  | [optional] 
**hashAlgorithm** | **String** | The password hash algorithm. | [optional] 
**memoryCost** | **Number** | Memory cost for hash calculation. Used by scrypt similar algorithms. | [optional] 
**parallelization** | **Number** |  | [optional] 
**rounds** | **Number** | Rounds for hash calculation. Used by scrypt and similar algorithms. | [optional] 
**saltSeparator** | **Blob** | The salt separator. | [optional] 
**sanityCheck** | **Boolean** | If true, backend will do sanity check(including duplicate email and federated id) when uploading account. | [optional] 
**signerKey** | **Blob** | The key for to hash the password. | [optional] 
**targetProjectId** | **String** | Specify which project (field value is actually project id) to operate. Only used when provided credential. | [optional] 
**users** | [**[UserInfo]**](UserInfo.md) | The account info to be stored. | [optional] 


