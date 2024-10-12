

# PoolUsageMetrics

Usage metrics for a pool across an aggregation interval.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataEgressGiB** | **Double** | Gets or sets the cross data center network egress in GiB from the pool during this interval. |  |
|**dataIngressGiB** | **Double** | Gets or sets the cross data center network ingress in GiB to the pool during this interval. |  |
|**endTime** | **OffsetDateTime** | Gets or sets the end time of the aggregation interval. |  |
|**poolId** | **String** | Gets or sets the id of the pool whose metrics are being aggregated. |  |
|**startTime** | **OffsetDateTime** | Gets or sets the start time of the aggregation interval. |  |
|**totalCoreHours** | **Double** | Gets or sets the total core hours used in the pool during this aggregation interval. |  |
|**vmSize** | **String** | Gets or sets the size of virtual machines in the pool.  All VMs in a pool are the same size. |  |



