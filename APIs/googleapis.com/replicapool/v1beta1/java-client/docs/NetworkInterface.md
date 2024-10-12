

# NetworkInterface

A Compute Engine NetworkInterface resource. Identical to the NetworkInterface on the corresponding Compute Engine resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessConfigs** | [**List&lt;AccessConfig&gt;**](AccessConfig.md) | An array of configurations for this interface. This specifies how this interface is configured to interact with other network services. |  [optional] |
|**network** | **String** | Name the Network resource to which this interface applies. |  [optional] |
|**networkIp** | **String** | An optional IPV4 internal network address to assign to the instance for this network interface. |  [optional] |



