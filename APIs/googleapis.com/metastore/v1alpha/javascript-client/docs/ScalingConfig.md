# DataprocMetastoreApi.ScalingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceSize** | **String** | An enum of readable instance sizes, with each instance size mapping to a float value (e.g. InstanceSize.EXTRA_SMALL &#x3D; scaling_factor(0.1)) | [optional] 
**scalingFactor** | **Number** | Scaling factor, increments of 0.1 for values less than 1.0, and increments of 1.0 for values greater than 1.0. | [optional] 



## Enum: InstanceSizeEnum


* `INSTANCE_SIZE_UNSPECIFIED` (value: `"INSTANCE_SIZE_UNSPECIFIED"`)

* `EXTRA_SMALL` (value: `"EXTRA_SMALL"`)

* `SMALL` (value: `"SMALL"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `LARGE` (value: `"LARGE"`)

* `EXTRA_LARGE` (value: `"EXTRA_LARGE"`)




