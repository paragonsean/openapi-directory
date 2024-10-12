

# DataSamplingConfig

Configuration options for sampling elements.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**behaviors** | [**List&lt;BehaviorsEnum&gt;**](#List&lt;BehaviorsEnum&gt;) | List of given sampling behaviors to enable. For example, specifying behaviors &#x3D; [ALWAYS_ON] samples in-flight elements but does not sample exceptions. Can be used to specify multiple behaviors like, behaviors &#x3D; [ALWAYS_ON, EXCEPTIONS] for specifying periodic sampling and exception sampling. If DISABLED is in the list, then sampling will be disabled and ignore the other given behaviors. Ordering does not matter. |  [optional] |



## Enum: List&lt;BehaviorsEnum&gt;

| Name | Value |
|---- | -----|
| DATA_SAMPLING_BEHAVIOR_UNSPECIFIED | &quot;DATA_SAMPLING_BEHAVIOR_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ALWAYS_ON | &quot;ALWAYS_ON&quot; |
| EXCEPTIONS | &quot;EXCEPTIONS&quot; |



