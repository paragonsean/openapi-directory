

# Inventory

This API resource represents the available inventory data for a Compute Engine virtual machine (VM) instance at a given point in time. You can use this API resource to determine the inventory data of your VM. For more information, see [Information provided by OS inventory management](https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**Map&lt;String, InventoryItem&gt;**](InventoryItem.md) | Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version. |  [optional] |
|**name** | **String** | Output only. The &#x60;Inventory&#x60; API resource name. Format: &#x60;projects/{project_number}/locations/{location}/instances/{instance_id}/inventory&#x60; |  [optional] [readonly] |
|**osInfo** | [**InventoryOsInfo**](InventoryOsInfo.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Timestamp of the last reported inventory for the VM. |  [optional] [readonly] |



