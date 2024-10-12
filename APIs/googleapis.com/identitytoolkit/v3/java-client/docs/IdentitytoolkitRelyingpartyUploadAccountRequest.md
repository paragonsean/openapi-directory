

# IdentitytoolkitRelyingpartyUploadAccountRequest

Request to upload user account in batch.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowOverwrite** | **Boolean** | Whether allow overwrite existing account when user local_id exists. |  [optional] |
|**blockSize** | **Integer** |  |  [optional] |
|**cpuMemCost** | **Integer** | The following 4 fields are for standard scrypt algorithm. |  [optional] |
|**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. |  [optional] |
|**dkLen** | **Integer** |  |  [optional] |
|**hashAlgorithm** | **String** | The password hash algorithm. |  [optional] |
|**memoryCost** | **Integer** | Memory cost for hash calculation. Used by scrypt similar algorithms. |  [optional] |
|**parallelization** | **Integer** |  |  [optional] |
|**rounds** | **Integer** | Rounds for hash calculation. Used by scrypt and similar algorithms. |  [optional] |
|**saltSeparator** | **byte[]** | The salt separator. |  [optional] |
|**sanityCheck** | **Boolean** | If true, backend will do sanity check(including duplicate email and federated id) when uploading account. |  [optional] |
|**signerKey** | **byte[]** | The key for to hash the password. |  [optional] |
|**targetProjectId** | **String** | Specify which project (field value is actually project id) to operate. Only used when provided credential. |  [optional] |
|**users** | [**List&lt;UserInfo&gt;**](UserInfo.md) | The account info to be stored. |  [optional] |



