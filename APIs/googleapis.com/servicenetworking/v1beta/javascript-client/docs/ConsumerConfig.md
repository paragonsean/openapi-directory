# ServiceNetworkingApi.ConsumerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudsqlConfigs** | [**[CloudSQLConfig]**](CloudSQLConfig.md) | Represents one or multiple Cloud SQL configurations. | [optional] 
**consumerExportCustomRoutes** | **Boolean** | Export custom routes flag value for peering from consumer to producer. | [optional] 
**consumerExportSubnetRoutesWithPublicIp** | **Boolean** | Export subnet routes with public ip flag value for peering from consumer to producer. | [optional] 
**consumerImportCustomRoutes** | **Boolean** | Import custom routes flag value for peering from consumer to producer. | [optional] 
**consumerImportSubnetRoutesWithPublicIp** | **Boolean** | Import subnet routes with public ip flag value for peering from consumer to producer. | [optional] 
**producerExportCustomRoutes** | **Boolean** | Export custom routes flag value for peering from producer to consumer. | [optional] 
**producerExportSubnetRoutesWithPublicIp** | **Boolean** | Export subnet routes with public ip flag value for peering from producer to consumer. | [optional] 
**producerImportCustomRoutes** | **Boolean** | Import custom routes flag value for peering from producer to consumer. | [optional] 
**producerImportSubnetRoutesWithPublicIp** | **Boolean** | Import subnet routes with public ip flag value for peering from producer to consumer. | [optional] 
**producerNetwork** | **String** | Output only. The VPC host network that is used to host managed service instances. In the format, projects/{project}/global/networks/{network} where {project} is the project number e.g. &#39;12345&#39; and {network} is the network name. | [optional] [readonly] 
**reservedRanges** | [**[GoogleCloudServicenetworkingV1ConsumerConfigReservedRange]**](GoogleCloudServicenetworkingV1ConsumerConfigReservedRange.md) | Output only. The reserved ranges associated with this private service access connection. | [optional] [readonly] 
**usedIpRanges** | **[String]** | Output only. The IP ranges already in use by consumer or producer | [optional] [readonly] 
**vpcScReferenceArchitectureEnabled** | **Boolean** | Output only. Indicates whether the VPC Service Controls reference architecture is configured for the producer VPC host network. | [optional] [readonly] 


