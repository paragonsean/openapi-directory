

# SapDiscoveryComponent

Message describing the system component.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationProperties** | [**SapDiscoveryComponentApplicationProperties**](SapDiscoveryComponentApplicationProperties.md) |  |  [optional] |
|**databaseProperties** | [**SapDiscoveryComponentDatabaseProperties**](SapDiscoveryComponentDatabaseProperties.md) |  |  [optional] |
|**haHosts** | **List&lt;String&gt;** | Optional. A list of host URIs that are part of the HA configuration if present. An empty list indicates the component is not configured for HA. |  [optional] |
|**hostProject** | **String** | Required. Pantheon Project in which the resources reside. |  [optional] |
|**resources** | [**List&lt;SapDiscoveryResource&gt;**](SapDiscoveryResource.md) | Optional. The resources in a component. |  [optional] |
|**sid** | **String** | Optional. The SAP identifier, used by the SAP software and helps differentiate systems for customers. |  [optional] |
|**topologyType** | [**TopologyTypeEnum**](#TopologyTypeEnum) | Optional. The detected topology of the component. |  [optional] |



## Enum: TopologyTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TOPOLOGY_TYPE_UNSPECIFIED&quot; |
| SCALE_UP | &quot;TOPOLOGY_SCALE_UP&quot; |
| SCALE_OUT | &quot;TOPOLOGY_SCALE_OUT&quot; |



