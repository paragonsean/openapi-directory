

# ContainersUsageInfoLimits


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containers** | **Integer** | The number of containers that can be created in the space. If -1 is returned, then an unlimited number of containers can be created. The number however is counted towards and limited by the container memory.  |  [optional] |
|**floatingIps** | **Integer** | The number of public IP addresses that can be allocated to the space. |  [optional] |
|**memoryMB** | **Integer** | The amount of container memory that can be used in the space in megabyte. |  [optional] |
|**vcpu** | **Integer** | The number of virtual CPUs that are assigned to the space. |  [optional] |



