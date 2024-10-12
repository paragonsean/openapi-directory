

# ScaleCapacity

The number of instances that can be used during this profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_default** | **String** | the number of instances that will be set if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. |  |
|**maximum** | **String** | the maximum number of instances for the resource. The actual maximum number of instances is limited by the cores that are available in the subscription. |  |
|**minimum** | **String** | the minimum number of instances for the resource. |  |



