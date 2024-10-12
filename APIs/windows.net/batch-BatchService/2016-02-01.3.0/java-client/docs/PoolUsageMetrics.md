

# PoolUsageMetrics

Usage metrics for a pool across an aggregation interval.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataEgressGiB** | **Double** | The cross data center network egress in GiB from the pool during this interval. |  |
|**dataIngressGiB** | **Double** | The cross data center network ingress in GiB to the pool during this interval. |  |
|**endTime** | **OffsetDateTime** | The end time of the aggregation interval. |  |
|**poolId** | **String** | The id of the pool whose metrics are being aggregated. |  |
|**startTime** | **OffsetDateTime** | The start time of the aggregation interval. |  |
|**totalCoreHours** | **Double** | The total core hours used in the pool during this aggregation interval. |  |
|**vmSize** | **String** | The size of virtual machines in the pool. All VMs in a pool are the same size. |  |



