

# AdvancedDatapathObservabilityConfig

AdvancedDatapathObservabilityConfig specifies configuration of observability features of advanced datapath.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableMetrics** | **Boolean** | Expose flow metrics on nodes |  [optional] |
|**enableRelay** | **Boolean** | Enable Relay component |  [optional] |
|**relayMode** | [**RelayModeEnum**](#RelayModeEnum) | Method used to make Relay available |  [optional] |



## Enum: RelayModeEnum

| Name | Value |
|---- | -----|
| RELAY_MODE_UNSPECIFIED | &quot;RELAY_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| INTERNAL_VPC_LB | &quot;INTERNAL_VPC_LB&quot; |
| EXTERNAL_LB | &quot;EXTERNAL_LB&quot; |



