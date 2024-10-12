# CloudSpannerApi.IncludeReplicas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoFailoverDisabled** | **Boolean** | If true, Spanner will not route requests to a replica outside the include_replicas list when all of the specified replicas are unavailable or unhealthy. Default value is &#x60;false&#x60;. | [optional] 
**replicaSelections** | [**[ReplicaSelection]**](ReplicaSelection.md) | The directed read replica selector. | [optional] 


