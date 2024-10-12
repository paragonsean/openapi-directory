

# LoadBalancingSettingsProperties

The JSON object that contains the properties required to create load balancing settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceState** | **ResourceState** |  |  [optional] |
|**additionalLatencyMilliseconds** | **Integer** | The additional latency in milliseconds for probes to fall into the lowest latency bucket |  [optional] |
|**sampleSize** | **Integer** | The number of samples to consider for load balancing decisions |  [optional] |
|**successfulSamplesRequired** | **Integer** | The number of samples within the sample period that must succeed |  [optional] |



