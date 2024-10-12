

# MacAddressPool

This resource represents a MAC address pool.  The default MAC address pools are used if you set the MAC address type for a virtual machine to 'Static'.  If the virtual machine setting is 'Dynamic', the hypervisor assigns the MAC address.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**MacAddressPoolModel**](MacAddressPoolModel.md) |  |  [optional] |
|**id** | **String** | URI of the resource. |  [optional] [readonly] |
|**location** | **String** | The region where the resource is located. |  [optional] |
|**name** | **String** | Name of the resource. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | List of key-value pairs. |  [optional] |
|**type** | **String** | Type of resource. |  [optional] [readonly] |



