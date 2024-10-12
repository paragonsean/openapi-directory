# KubernetesEngineApi.PrivateClusterConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enablePrivateEndpoint** | **Boolean** | Whether the master&#39;s internal IP address is used as the cluster endpoint. | [optional] 
**enablePrivateNodes** | **Boolean** | Whether nodes have internal IP addresses only. If enabled, all nodes are given only RFC 1918 private addresses and communicate with the master via private networking. | [optional] 
**masterGlobalAccessConfig** | [**PrivateClusterMasterGlobalAccessConfig**](PrivateClusterMasterGlobalAccessConfig.md) |  | [optional] 
**masterIpv4CidrBlock** | **String** | The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning internal IP addresses to the master or set of masters, as well as the ILB VIP. This range must not overlap with any other ranges in use within the cluster&#39;s network. | [optional] 
**peeringName** | **String** | Output only. The peering name in the customer VPC used by this cluster. | [optional] 
**privateEndpoint** | **String** | Output only. The internal IP address of this cluster&#39;s master endpoint. | [optional] 
**privateEndpointSubnetwork** | **String** | Subnet to provision the master&#39;s private endpoint during cluster creation. Specified in projects/_*_/regions/_*_/subnetworks/_* format. | [optional] 
**publicEndpoint** | **String** | Output only. The external IP address of this cluster&#39;s master endpoint. | [optional] 


