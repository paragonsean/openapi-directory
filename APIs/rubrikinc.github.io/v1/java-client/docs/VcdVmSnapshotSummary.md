

# VcdVmSnapshotSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**indexState** | **Long** | Integer value representing the state of the indexing job for a snapshot. 0 means that the indexing has not begun or is in progress. 1 means indexing completed successfully. 2 means that the indexer failed to process this snapshot.  |  [optional] |
|**vcdVmMoid** | **String** | Id assigned by vCloud Director to the virtual machine of the specified snapshot. |  |
|**vcenterVmId** | **String** | ID assigned to the object that represents the virtual machine that is the source of a specified snapshot object. |  |
|**vmName** | **String** | Name of the virtual machine object of the snapshot. |  |
|**vmSnapshotId** | **String** | ID assigned to the object that represents a virtual machine snapshot. |  |



