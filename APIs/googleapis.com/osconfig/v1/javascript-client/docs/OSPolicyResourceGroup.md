# OsConfigApi.OSPolicyResourceGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventoryFilters** | [**[OSPolicyInventoryFilter]**](OSPolicyInventoryFilter.md) | List of inventory filters for the resource group. The resources in this resource group are applied to the target VM if it satisfies at least one of the following inventory filters. For example, to apply this resource group to VMs running either &#x60;RHEL&#x60; or &#x60;CentOS&#x60; operating systems, specify 2 items for the list with following values: inventory_filters[0].os_short_name&#x3D;&#39;rhel&#39; and inventory_filters[1].os_short_name&#x3D;&#39;centos&#39; If the list is empty, this resource group will be applied to the target VM unconditionally. | [optional] 
**resources** | [**[OSPolicyResource]**](OSPolicyResource.md) | Required. List of resources configured for this resource group. The resources are executed in the exact order specified here. | [optional] 


