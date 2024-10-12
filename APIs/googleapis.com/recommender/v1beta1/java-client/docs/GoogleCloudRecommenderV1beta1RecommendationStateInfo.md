

# GoogleCloudRecommenderV1beta1RecommendationStateInfo

Information for state. Contains state and metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | The state of the recommendation, Eg ACTIVE, SUCCEEDED, FAILED. |  [optional] |
|**stateMetadata** | **Map&lt;String, String&gt;** | A map of metadata for the state, provided by user or automations systems. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CLAIMED | &quot;CLAIMED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| DISMISSED | &quot;DISMISSED&quot; |



