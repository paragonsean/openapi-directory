

# HdfsSnapshotSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archivalLocationIds** | **List&lt;String&gt;** |  |  [optional] |
|**cloudState** | **Long** | Integer value that represents the archival state of a snapshot. 0 means the snapshot is not archived. 2 means the snapshot is archived. 3 means the snapshot is downloaded from the archival location. 4 means the snapshot is in the process of being downloaded from the archival location. 6 means the snapshot is stored locally and at the archival location.  |  [optional] |
|**cloudStorageTier** | **SnapshotCloudStorageTier** |  |  [optional] |
|**consistencyLevel** | **String** |  |  [optional] |
|**date** | **OffsetDateTime** |  |  |
|**expirationDate** | **OffsetDateTime** |  |  [optional] |
|**id** | **String** |  |  |
|**indexState** | **Long** | Integer value representing the state of the indexing job for a snapshot. 0 means that the indexing has not begun or is in progress. 1 means indexing completed successfully. 2 means that the indexer failed to process this snapshot.  |  [optional] |
|**isCustomRetentionApplied** | **Boolean** | A Boolean that indicates whether or not custom retention is applied to the snapshot.  |  |
|**isOnDemandSnapshot** | **Boolean** |  |  |
|**isPlacedOnLegalHold** | **Boolean** | A Boolean that indicates whether the snapshot is placed on Legal Hold. When this value is &#39;true&#39;, the snapshot is placed on Legal Hold. |  [optional] |
|**isRetainedByRetentionLockSla** | **Boolean** | A Boolean that indicates whether the snapshot is being retained under a Retention Lock SLA Domain. When this value is &#39;true&#39;, the snapshot is being retained under a Retention Lock SLA Domain. |  [optional] |
|**parentSnapshotId** | **String** | ID of the parent snapshot if the current snapshot is a child snapshot. Child snapshots are snapshots of objects that are part of an app, either a vCloud Director vApp or an AppBlueprint. Snapshots of the app are parent snapshots.  |  [optional] |
|**replicationLocationIds** | **List&lt;String&gt;** |  |  |
|**slaId** | **String** | (Deprecated) For a policy based snapshot this parameter contains the ID of the SLA Domain currently assigned to the data source of that snapshot. For an on demand snapshot this field corresponds to the SLA Domain that was assigned when the snapshot was taken. A data source, and individual snapshots, can be reassigned to a different SLA Domain, or the SLA Domain can be modified. In any of these cases this parameter can contain a stale and incorrect value. To view retention information for this snapshot, use snapshotRetentionInfo instead. |  |
|**slaName** | **String** | (Deprecated) For a policy based snapshot this parameter contains the name of the SLA Domain currently assigned to the data source of that snapshot. For an on demand snapshot this field corresponds to the SLA Domain that was assigned when the snapshot was taken. A data source, and individual snapshots, can be reassigned to a different SLA Domain, or the SLA Domain can be modified. In any of these cases this parameter can contain a stale and incorrect value. To view retention information for this snapshot, use snapshotRetentionInfo instead. |  |
|**snapshotRetentionInfo** | [**SnapshotRetentionInfo**](SnapshotRetentionInfo.md) |  |  [optional] |
|**sourceObjectType** | **String** |  |  [optional] |
|**fileCount** | **Long** |  |  [optional] |
|**hdfsName** | **String** |  |  |



