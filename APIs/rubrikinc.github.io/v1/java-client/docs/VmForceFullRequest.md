

# VmForceFullRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**virtualDiskInfos** | [**List&lt;VmwareVdiskForceFullInfo&gt;**](VmwareVdiskForceFullInfo.md) | List of virtual disks to be configured to force a full snapshot. The configuration specifies which virtual disks in VMware VM should do forced full snapshots and whether to perform deduplication. If it contains an empty array, a forced full snapshot is requested for all virtual disks in the VMware VM and deduplication is performed by default; otherwise a forced full snapshot is requested for the virtual disks in the array and the shouldDedupe determines whether deduplication is performed. The next backup job checks the configuration and takes full snapshot according to the specification. After the backup job is done, it clears the configuration in order to prevent further full snapshots. |  [optional] |



