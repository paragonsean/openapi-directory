

# PartitionLoadInformation

Represents load information for a partition, which contains the primary and secondary reported load metrics. In case there is no load reported, PartitionLoadInformation will contain the default load for the service of the partition. For default loads, LoadMetricReport's LastReportedUtc is set to 0.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**partitionId** | **UUID** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition ID is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the IDs of its partitions would be different. |  [optional] |
|**primaryLoadMetricReports** | [**List&lt;LoadMetricReport&gt;**](LoadMetricReport.md) | Array of load reports from the primary replica for this partition. |  [optional] |
|**secondaryLoadMetricReports** | [**List&lt;LoadMetricReport&gt;**](LoadMetricReport.md) | Array of aggregated load reports from all secondary replicas for this partition. Array only contains the latest reported load for each metric. |  [optional] |



