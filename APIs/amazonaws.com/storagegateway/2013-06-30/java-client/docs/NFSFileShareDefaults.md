

# NFSFileShareDefaults

Describes Network File System (NFS) file share default values. Files and folders stored as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files and folders are assigned these default Unix permissions. This operation is only supported for S3 File Gateways.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileMode** | [**String**](String.md) |  |  [optional] |
|**directoryMode** | [**String**](String.md) |  |  [optional] |
|**groupId** | [**Integer**](Integer.md) |  |  [optional] |
|**ownerId** | [**Integer**](Integer.md) |  |  [optional] |



