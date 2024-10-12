

# VappVmNetworkConnection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressingMode** | **VappVmIpAddressingMode** |  |  |
|**ipAddress** | **String** | IPv4 address to assign to the specified vApp network connection. Set this value only when the network address allocation method is &#39;Static&#39;. Otherwise, the value should be empty. |  [optional] |
|**isConnected** | **Boolean** | Boolean value that indicates whether the specified vApp network connection is enabled. Set the value to &#39;true&#39; to enable the connection or &#39;false&#39; to disable the connection. |  |
|**macAddress** | **String** | MAC address of the NIC that is used by the specified vApp network connection. |  [optional] |
|**networkAdapterType** | **String** | The network adapter type of the NIC. |  [optional] |
|**nicIndex** | **Integer** | Index assigned to the NIC that is used by the specified vApp network connection. |  |
|**vappNetworkName** | **String** | Name of the vApp network to which the NIC corresponding to this connection will connect to. |  [optional] |



