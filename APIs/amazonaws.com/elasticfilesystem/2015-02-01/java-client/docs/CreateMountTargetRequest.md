

# CreateMountTargetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileSystemId** | **String** | The ID of the file system for which to create the mount target. |  |
|**subnetId** | **String** | The ID of the subnet to add the mount target in. For file systems that use One Zone storage classes, use the subnet that is associated with the file system&#39;s Availability Zone. |  |
|**ipAddress** | **String** | Valid IPv4 address within the address range of the specified subnet. |  [optional] |
|**securityGroups** | **List&lt;String&gt;** | Up to five VPC security group IDs, of the form &lt;code&gt;sg-xxxxxxxx&lt;/code&gt;. These must be for the same VPC as subnet specified. |  [optional] |



