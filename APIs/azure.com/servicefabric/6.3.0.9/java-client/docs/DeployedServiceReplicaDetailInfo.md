

# DeployedServiceReplicaDetailInfo

Information about a Service Fabric service replica deployed on a node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentServiceOperation** | **ServiceOperationName** |  |  [optional] |
|**currentServiceOperationStartTimeUtc** | **OffsetDateTime** | The start time of the current service operation in UTC format. |  [optional] |
|**partitionId** | **UUID** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition ID is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the IDs of its partitions would be different. |  [optional] |
|**reportedLoad** | [**List&lt;LoadMetricReportInfo&gt;**](LoadMetricReportInfo.md) | List of load reported by replica. |  [optional] |
|**serviceKind** | **ServiceKind** |  |  |
|**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. |  [optional] |



