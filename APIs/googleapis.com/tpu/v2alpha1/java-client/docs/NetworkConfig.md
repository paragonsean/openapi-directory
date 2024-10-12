

# NetworkConfig

Network related configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canIpForward** | **Boolean** | Allows the TPU node to send and receive packets with non-matching destination or source IPs. This is required if you plan to use the TPU workers to forward routes. |  [optional] |
|**enableExternalIps** | **Boolean** | Indicates that external IP addresses would be associated with the TPU workers. If set to false, the specified subnetwork or network should have Private Google Access enabled. |  [optional] |
|**network** | **String** | The name of the network for the TPU node. It must be a preexisting Google Compute Engine network. If none is provided, \&quot;default\&quot; will be used. |  [optional] |
|**queueCount** | **Integer** | Optional. Specifies networking queue count for TPU VM instance&#39;s network interface. |  [optional] |
|**subnetwork** | **String** | The name of the subnetwork for the TPU node. It must be a preexisting Google Compute Engine subnetwork. If none is provided, \&quot;default\&quot; will be used. |  [optional] |



