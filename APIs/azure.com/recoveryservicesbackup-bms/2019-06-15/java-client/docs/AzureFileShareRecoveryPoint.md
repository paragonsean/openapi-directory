

# AzureFileShareRecoveryPoint

Azure File Share workload specific backup copy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileShareSnapshotUri** | **String** | Contains Url to the snapshot of fileshare, if applicable |  [optional] [readonly] |
|**recoveryPointSizeInGB** | **Integer** | Contains recovery point size |  [optional] [readonly] |
|**recoveryPointTime** | **OffsetDateTime** | Time at which this backup copy was created. |  [optional] [readonly] |
|**recoveryPointType** | **String** | Type of the backup copy. Specifies whether it is a crash consistent backup or app consistent. |  [optional] [readonly] |



