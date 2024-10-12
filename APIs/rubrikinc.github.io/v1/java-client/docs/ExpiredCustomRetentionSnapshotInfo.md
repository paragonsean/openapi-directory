

# ExpiredCustomRetentionSnapshotInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**birthSlaDomainName** | **String** | The SLA Domain in effect at the time the snapshot was taken. Identical to the SLA Domain assigned to the data source at that time.  |  |
|**globalExpirationDate** | **OffsetDateTime** | Timestamp that indicates when the snapshot expires from all cluster-managed locations.  |  |
|**id** | **String** | The snapshot ID. |  |
|**lastSlaDomainName** | **String** | The most recent SLA Domain assigned to the snapshot. Snapshots expire based on the last known configuration for the assigned SLA Domain.  |  |
|**snapshotDate** | **OffsetDateTime** | Creation timestamp for the snapshot. |  |



