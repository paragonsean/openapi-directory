

# AutoScaleConfiguration

AutoScale configuration properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxReplicas** | **Integer** | The maximum number of replicas for each service. |  [optional] |
|**minReplicas** | **Integer** | The minimum number of replicas for each service. |  [optional] |
|**refreshPeriodInSeconds** | **Integer** | Refresh period in seconds. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | If auto-scale is enabled for all services. Each service can turn it off individually. |  [optional] |
|**targetUtilization** | **BigDecimal** | The target utilization. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



