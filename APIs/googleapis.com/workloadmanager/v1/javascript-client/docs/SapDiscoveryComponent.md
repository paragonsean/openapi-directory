# WorkloadManagerApi.SapDiscoveryComponent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationProperties** | [**SapDiscoveryComponentApplicationProperties**](SapDiscoveryComponentApplicationProperties.md) |  | [optional] 
**databaseProperties** | [**SapDiscoveryComponentDatabaseProperties**](SapDiscoveryComponentDatabaseProperties.md) |  | [optional] 
**haHosts** | **[String]** | Optional. A list of host URIs that are part of the HA configuration if present. An empty list indicates the component is not configured for HA. | [optional] 
**hostProject** | **String** | Required. Pantheon Project in which the resources reside. | [optional] 
**resources** | [**[SapDiscoveryResource]**](SapDiscoveryResource.md) | Optional. The resources in a component. | [optional] 
**sid** | **String** | Optional. The SAP identifier, used by the SAP software and helps differentiate systems for customers. | [optional] 
**topologyType** | **String** | Optional. The detected topology of the component. | [optional] 



## Enum: TopologyTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TOPOLOGY_TYPE_UNSPECIFIED"`)

* `SCALE_UP` (value: `"TOPOLOGY_SCALE_UP"`)

* `SCALE_OUT` (value: `"TOPOLOGY_SCALE_OUT"`)




