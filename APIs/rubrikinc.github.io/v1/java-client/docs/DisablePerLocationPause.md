

# DisablePerLocationPause


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**shouldSkipOldSnapshots** | **Boolean** | Specifies whether to replicate snapshots taken during and before replication pause. When this value is &#39;true,&#39; snapshots taken during and before the replication pause are not replicated. In all other cases, snapshots taken before and during the replication pause are replicated.  |  |
|**sourceClusterUuids** | **List&lt;String&gt;** | Replication from specified Rubrik clusters are resumed. Specified Rubrik clusters must be paused replication sources of local Rubrik cluster.  |  |



