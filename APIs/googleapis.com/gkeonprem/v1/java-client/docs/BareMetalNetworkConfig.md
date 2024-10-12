

# BareMetalNetworkConfig

Specifies the cluster network configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedNetworking** | **Boolean** | Enables the use of advanced Anthos networking features, such as Bundled Load Balancing with BGP or the egress NAT gateway. Setting configuration for advanced networking features will automatically set this flag. |  [optional] |
|**islandModeCidr** | [**BareMetalIslandModeCidrConfig**](BareMetalIslandModeCidrConfig.md) |  |  [optional] |
|**multipleNetworkInterfacesConfig** | [**BareMetalMultipleNetworkInterfacesConfig**](BareMetalMultipleNetworkInterfacesConfig.md) |  |  [optional] |
|**srIovConfig** | [**BareMetalSrIovConfig**](BareMetalSrIovConfig.md) |  |  [optional] |



