

# IncludeReplicas

An IncludeReplicas contains a repeated set of ReplicaSelection which indicates the order in which replicas should be considered.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoFailoverDisabled** | **Boolean** | If true, Spanner will not route requests to a replica outside the include_replicas list when all of the specified replicas are unavailable or unhealthy. Default value is &#x60;false&#x60;. |  [optional] |
|**replicaSelections** | [**List&lt;ReplicaSelection&gt;**](ReplicaSelection.md) | The directed read replica selector. |  [optional] |



