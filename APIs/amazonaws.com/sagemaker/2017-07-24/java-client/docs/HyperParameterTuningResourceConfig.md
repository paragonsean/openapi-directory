

# HyperParameterTuningResourceConfig

<p>The configuration of resources, including compute instances and storage volumes for use in training jobs launched by hyperparameter tuning jobs. <code>HyperParameterTuningResourceConfig</code> is similar to <code>ResourceConfig</code>, but has the additional <code>InstanceConfigs</code> and <code>AllocationStrategy</code> fields to allow for flexible instance management. Specify one or more instance types, count, and the allocation strategy for instance selection.</p> <note> <p> <code>HyperParameterTuningResourceConfig</code> supports the capabilities of <code>ResourceConfig</code> with the exception of <code>KeepAlivePeriodInSeconds</code>. Hyperparameter tuning jobs use warm pools by default, which reuse clusters between training jobs.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceType** | [**TrainingInstanceType**](TrainingInstanceType.md) |  |  [optional] |
|**instanceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**volumeSizeInGB** | [**Integer**](Integer.md) |  |  [optional] |
|**volumeKmsKeyId** | [**String**](String.md) |  |  [optional] |
|**allocationStrategy** | [**HyperParameterTuningAllocationStrategy**](HyperParameterTuningAllocationStrategy.md) |  |  [optional] |
|**instanceConfigs** | [**List**](List.md) |  |  [optional] |



