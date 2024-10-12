

# CreateProfileRequest

CreateProfileRequest describes a profile resource online creation request. The deployment field must be populated. The profile_type specifies the list of profile types supported by the agent. The creation call will hang until a profile of one of these types needs to be collected. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployment** | [**Deployment**](Deployment.md) |  |  [optional] |
|**profileType** | [**List&lt;ProfileTypeEnum&gt;**](#List&lt;ProfileTypeEnum&gt;) | One or more profile types that the agent is capable of providing. |  [optional] |



## Enum: List&lt;ProfileTypeEnum&gt;

| Name | Value |
|---- | -----|
| PROFILE_TYPE_UNSPECIFIED | &quot;PROFILE_TYPE_UNSPECIFIED&quot; |
| CPU | &quot;CPU&quot; |
| WALL | &quot;WALL&quot; |
| HEAP | &quot;HEAP&quot; |
| THREADS | &quot;THREADS&quot; |
| CONTENTION | &quot;CONTENTION&quot; |
| PEAK_HEAP | &quot;PEAK_HEAP&quot; |
| HEAP_ALLOC | &quot;HEAP_ALLOC&quot; |



