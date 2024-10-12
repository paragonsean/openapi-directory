

# InfraRoleInstance

The virtual machine resource is used to represent an infrastructure virtual machine in the Azure Stack environment. The fabric resource provider only surfaces infrastructure virtual machines. These machines are never created directly by the admin, but rather as a side effect of expanding admin services.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**InfraRoleInstanceModel**](InfraRoleInstanceModel.md) |  |  [optional] |
|**id** | **String** | URI of the resource. |  [optional] [readonly] |
|**location** | **String** | The region where the resource is located. |  [optional] |
|**name** | **String** | Name of the resource. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | List of key-value pairs. |  [optional] |
|**type** | **String** | Type of resource. |  [optional] [readonly] |



