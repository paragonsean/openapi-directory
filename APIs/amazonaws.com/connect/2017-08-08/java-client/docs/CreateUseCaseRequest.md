

# CreateUseCaseRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**useCaseType** | [**UseCaseTypeEnum**](#UseCaseTypeEnum) | The type of use case to associate to the integration association. Each integration association can have only one of each use case type. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |



## Enum: UseCaseTypeEnum

| Name | Value |
|---- | -----|
| RULES_EVALUATION | &quot;RULES_EVALUATION&quot; |
| CONNECT_CAMPAIGNS | &quot;CONNECT_CAMPAIGNS&quot; |



