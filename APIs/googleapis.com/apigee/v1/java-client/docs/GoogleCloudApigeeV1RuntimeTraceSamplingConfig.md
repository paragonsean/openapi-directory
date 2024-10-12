

# GoogleCloudApigeeV1RuntimeTraceSamplingConfig

NEXT ID: 3 RuntimeTraceSamplingConfig represents the detail settings of distributed tracing. Only the fields that are defined in the distributed trace configuration can be overridden using the distribute trace configuration override APIs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sampler** | [**SamplerEnum**](#SamplerEnum) | Sampler of distributed tracing. OFF is the default value. |  [optional] |
|**samplingRate** | **Float** | Field sampling rate. This value is only applicable when using the PROBABILITY sampler. The supported values are &gt; 0 and &lt;&#x3D; 0.5. |  [optional] |



## Enum: SamplerEnum

| Name | Value |
|---- | -----|
| SAMPLER_UNSPECIFIED | &quot;SAMPLER_UNSPECIFIED&quot; |
| FALSE | &quot;false&quot; |
| PROBABILITY | &quot;PROBABILITY&quot; |



