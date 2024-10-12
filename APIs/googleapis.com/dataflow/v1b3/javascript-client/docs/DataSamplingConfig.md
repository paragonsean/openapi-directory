# DataflowApi.DataSamplingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behaviors** | **[String]** | List of given sampling behaviors to enable. For example, specifying behaviors &#x3D; [ALWAYS_ON] samples in-flight elements but does not sample exceptions. Can be used to specify multiple behaviors like, behaviors &#x3D; [ALWAYS_ON, EXCEPTIONS] for specifying periodic sampling and exception sampling. If DISABLED is in the list, then sampling will be disabled and ignore the other given behaviors. Ordering does not matter. | [optional] 



## Enum: [BehaviorsEnum]


* `DATA_SAMPLING_BEHAVIOR_UNSPECIFIED` (value: `"DATA_SAMPLING_BEHAVIOR_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `ALWAYS_ON` (value: `"ALWAYS_ON"`)

* `EXCEPTIONS` (value: `"EXCEPTIONS"`)




