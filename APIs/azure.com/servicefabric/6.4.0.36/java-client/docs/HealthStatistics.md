

# HealthStatistics

The health statistics of an entity, returned as part of the health query result when the query description is configured to include statistics. The statistics include health state counts for all children types of the current entity. For example, for cluster, the health statistics include health state counts for nodes, applications, services, partitions, replicas, deployed applications and deployed service packages. For partition, the health statistics include health counts for replicas.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**healthStateCountList** | [**List&lt;EntityKindHealthStateCount&gt;**](EntityKindHealthStateCount.md) | List of health state counts per entity kind, which keeps track of how many children of the queried entity are in Ok, Warning and Error state. |  [optional] |



