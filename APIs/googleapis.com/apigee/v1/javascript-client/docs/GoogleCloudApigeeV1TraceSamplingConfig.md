# ApigeeApi.GoogleCloudApigeeV1TraceSamplingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sampler** | **String** | Sampler of distributed tracing. OFF is the default value. | [optional] 
**samplingRate** | **Number** | Field sampling rate. This value is only applicable when using the PROBABILITY sampler. The supported values are &gt; 0 and &lt;&#x3D; 0.5. | [optional] 



## Enum: SamplerEnum


* `SAMPLER_UNSPECIFIED` (value: `"SAMPLER_UNSPECIFIED"`)

* `false` (value: `"false"`)

* `PROBABILITY` (value: `"PROBABILITY"`)




