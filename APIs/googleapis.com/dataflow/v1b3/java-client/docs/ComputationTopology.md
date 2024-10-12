

# ComputationTopology

All configuration data for a particular Computation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computationId** | **String** | The ID of the computation. |  [optional] |
|**inputs** | [**List&lt;StreamLocation&gt;**](StreamLocation.md) | The inputs to the computation. |  [optional] |
|**keyRanges** | [**List&lt;KeyRangeLocation&gt;**](KeyRangeLocation.md) | The key ranges processed by the computation. |  [optional] |
|**outputs** | [**List&lt;StreamLocation&gt;**](StreamLocation.md) | The outputs from the computation. |  [optional] |
|**stateFamilies** | [**List&lt;StateFamilyConfig&gt;**](StateFamilyConfig.md) | The state family values. |  [optional] |
|**systemStageName** | **String** | The system stage name. |  [optional] |



