

# AutoscalingLimits

The autoscaling limits for the instance. Users can define the minimum and maximum compute capacity allocated to the instance, and the autoscaler will only scale within that range. Users can either use nodes or processing units to specify the limits, but should use the same unit to set both the min_limit and max_limit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxNodes** | **Integer** | Maximum number of nodes allocated to the instance. If set, this number should be greater than or equal to min_nodes. |  [optional] |
|**maxProcessingUnits** | **Integer** | Maximum number of processing units allocated to the instance. If set, this number should be multiples of 1000 and be greater than or equal to min_processing_units. |  [optional] |
|**minNodes** | **Integer** | Minimum number of nodes allocated to the instance. If set, this number should be greater than or equal to 1. |  [optional] |
|**minProcessingUnits** | **Integer** | Minimum number of processing units allocated to the instance. If set, this number should be multiples of 1000. |  [optional] |



