

# ContinuousBackupSource

Message describing a ContinuousBackupSource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cluster** | **String** | Required. The source cluster from which to restore. This cluster must have continuous backup enabled for this operation to succeed. For the required format, see the comment on the Cluster.name field. |  [optional] |
|**pointInTime** | **String** | Required. The point in time to restore to. |  [optional] |



