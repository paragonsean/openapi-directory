

# ScalingConfig

Represents the scaling configuration of a metastore service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceSize** | [**InstanceSizeEnum**](#InstanceSizeEnum) | An enum of readable instance sizes, with each instance size mapping to a float value (e.g. InstanceSize.EXTRA_SMALL &#x3D; scaling_factor(0.1)) |  [optional] |
|**scalingFactor** | **Float** | Scaling factor, increments of 0.1 for values less than 1.0, and increments of 1.0 for values greater than 1.0. |  [optional] |



## Enum: InstanceSizeEnum

| Name | Value |
|---- | -----|
| INSTANCE_SIZE_UNSPECIFIED | &quot;INSTANCE_SIZE_UNSPECIFIED&quot; |
| EXTRA_SMALL | &quot;EXTRA_SMALL&quot; |
| SMALL | &quot;SMALL&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| LARGE | &quot;LARGE&quot; |
| EXTRA_LARGE | &quot;EXTRA_LARGE&quot; |



