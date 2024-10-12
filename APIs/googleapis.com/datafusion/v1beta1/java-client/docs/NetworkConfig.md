

# NetworkConfig

Network configuration for a Data Fusion instance. These configurations are used for peering with the customer network. Configurations are optional when a public Data Fusion instance is to be created. However, providing these configurations allows several benefits, such as reduced network latency while accessing the customer resources from managed Data Fusion instance nodes, as well as access to the customer on-prem resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) | Optional. Type of connection for establishing private IP connectivity between the Data Fusion customer project VPC and the corresponding tenant project from a predefined list of available connection modes. If this field is unspecified for a private instance, VPC peering is used. |  [optional] |
|**ipAllocation** | **String** | Optional. The IP range in CIDR notation to use for the managed Data Fusion instance nodes. This range must not overlap with any other ranges used in the Data Fusion instance network. This is required only when using connection type VPC_PEERING. Format: a.b.c.d/22 Example: 192.168.0.0/22 |  [optional] |
|**network** | **String** | Optional. Name of the network in the customer project with which the Tenant Project will be peered for executing pipelines. This is required only when using connection type VPC peering. In case of shared VPC where the network resides in another host project the network should specified in the form of projects/{host-project-id}/global/networks/{network}. This is only required for connectivity type VPC_PEERING. |  [optional] |
|**privateServiceConnectConfig** | [**PrivateServiceConnectConfig**](PrivateServiceConnectConfig.md) |  |  [optional] |



## Enum: ConnectionTypeEnum

| Name | Value |
|---- | -----|
| CONNECTION_TYPE_UNSPECIFIED | &quot;CONNECTION_TYPE_UNSPECIFIED&quot; |
| VPC_PEERING | &quot;VPC_PEERING&quot; |
| PRIVATE_SERVICE_CONNECT_INTERFACES | &quot;PRIVATE_SERVICE_CONNECT_INTERFACES&quot; |



