

# ContainersQuotaInfoOrgQuota


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**floatingIpsMax** | **String** | The number of public IP addresses that can be assigned across all spaces of the organization. |  [optional] |
|**floatingIpsSpaceDefault** | **String** | The number of public IP addresses that are required for one space. If the number of public IP addresses is not available, then a new space cannot be created to be used with IBM Containers.  |  [optional] |
|**floatingIpsUsage** | **Integer** | The number of public IP addresses that are currently assigned to the spaces of the organization. |  [optional] |
|**ramMax** | **Integer** | The maximum amount of container memory on the compute host that can be assigned across the spaces of the organization. |  [optional] |
|**ramSpaceDefault** | **Integer** | The amount of container memory that is required to be used for one space. If this amount is not available, then a new space cannot be created to be used with IBM Containers.  |  [optional] |
|**ramUsage** | **Integer** | The amount of container memory that is currently used across all spaces of the organization. |  [optional] |
|**subnetUsage** | **Integer** | The number of subnets that were created across all spaces of the organization. |  [optional] |
|**subnetsDefault** | **Integer** | The number of subnets that is required to create a new space. If this number is not available, then a new space cannot be created to be used with IBM Containers. |  [optional] |
|**subnetsMax** | **Integer** | The maximum number of container private subnet that can be created across all spaces of the organization. |  [optional] |



