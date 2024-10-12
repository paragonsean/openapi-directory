

# ResourceUsageExportConfig

Configuration for exporting cluster resource usages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryDestination** | [**BigQueryDestination**](BigQueryDestination.md) |  |  [optional] |
|**consumptionMeteringConfig** | [**ConsumptionMeteringConfig**](ConsumptionMeteringConfig.md) |  |  [optional] |
|**enableNetworkEgressMetering** | **Boolean** | Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created in the cluster to meter network egress traffic. |  [optional] |



