

# VmParams

Parameters for creating a Compute Engine Instance resource. Most fields are identical to the corresponding Compute Engine resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseInstanceName** | **String** | Deprecated. Please use baseInstanceName instead. |  [optional] |
|**canIpForward** | **Boolean** | Enables IP Forwarding, which allows this instance to receive packets destined for a different IP address, and send packets with a different source IP. See IP Forwarding for more information. |  [optional] |
|**description** | **String** | An optional textual description of the instance. |  [optional] |
|**disksToAttach** | [**List&lt;ExistingDisk&gt;**](ExistingDisk.md) | A list of existing Persistent Disk resources to attach to each replica in the pool. Each disk will be attached in read-only mode to every replica. |  [optional] |
|**disksToCreate** | [**List&lt;NewDisk&gt;**](NewDisk.md) | A list of Disk resources to create and attach to each Replica in the Pool. Currently, you can only define one disk and it must be a root persistent disk. Note that Replica Pool will create a root persistent disk for each replica. |  [optional] |
|**machineType** | **String** | The machine type for this instance. The resource name (e.g. n1-standard-1). |  [optional] |
|**metadata** | [**Metadata**](Metadata.md) |  |  [optional] |
|**networkInterfaces** | [**List&lt;NetworkInterface&gt;**](NetworkInterface.md) | A list of network interfaces for the instance. Currently only one interface is supported by Google Compute Engine, ONE_TO_ONE_NAT. |  [optional] |
|**onHostMaintenance** | **String** |  |  [optional] |
|**serviceAccounts** | [**List&lt;ServiceAccount&gt;**](ServiceAccount.md) | A list of Service Accounts to enable for this instance. |  [optional] |
|**tags** | [**Tag**](Tag.md) |  |  [optional] |



