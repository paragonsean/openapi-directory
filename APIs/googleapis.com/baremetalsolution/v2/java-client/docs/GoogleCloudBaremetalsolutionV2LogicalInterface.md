

# GoogleCloudBaremetalsolutionV2LogicalInterface

Each logical interface represents a logical abstraction of the underlying physical interface (for eg. bond, nic) of the instance. Each logical interface can effectively map to multiple network-IP pairs and still be mapped to one underlying physical interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interfaceIndex** | **Integer** | The index of the logical interface mapping to the index of the hardware bond or nic on the chosen network template. This field is deprecated. |  [optional] |
|**logicalNetworkInterfaces** | [**List&lt;LogicalNetworkInterface&gt;**](LogicalNetworkInterface.md) | List of logical network interfaces within a logical interface. |  [optional] |
|**name** | **String** | Interface name. This is of syntax or and forms part of the network template name. |  [optional] |



