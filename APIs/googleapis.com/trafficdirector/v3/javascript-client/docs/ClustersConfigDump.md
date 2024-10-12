# TrafficDirectorApi.ClustersConfigDump

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamicActiveClusters** | [**[DynamicCluster]**](DynamicCluster.md) | The dynamically loaded active clusters. These are clusters that are available to service data plane traffic. | [optional] 
**dynamicWarmingClusters** | [**[DynamicCluster]**](DynamicCluster.md) | The dynamically loaded warming clusters. These are clusters that are currently undergoing warming in preparation to service data plane traffic. Note that if attempting to recreate an Envoy configuration from a configuration dump, the warming clusters should generally be discarded. | [optional] 
**staticClusters** | [**[StaticCluster]**](StaticCluster.md) | The statically loaded cluster configs. | [optional] 
**versionInfo** | **String** | This is the :ref:&#x60;version_info &#x60; in the last processed CDS discovery response. If there are only static bootstrap clusters, this field will be \&quot;\&quot;. | [optional] 


