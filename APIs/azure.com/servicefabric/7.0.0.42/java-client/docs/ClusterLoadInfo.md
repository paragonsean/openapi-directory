

# ClusterLoadInfo

Information about load in a Service Fabric cluster. It holds a summary of all metrics and their load in a cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastBalancingEndTimeUtc** | **OffsetDateTime** | The end time of last resource balancing run. |  [optional] |
|**lastBalancingStartTimeUtc** | **OffsetDateTime** | The starting time of last resource balancing run. |  [optional] |
|**loadMetricInformation** | [**List&lt;LoadMetricInformation&gt;**](LoadMetricInformation.md) | List that contains metrics and their load information in this cluster. |  [optional] |



