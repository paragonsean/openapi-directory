

# GoogleCloudAiplatformV1TrialParameter

A message representing a parameter to be tuned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parameterId** | **String** | Output only. The ID of the parameter. The parameter should be defined in StudySpec&#39;s Parameters. |  [optional] [readonly] |
|**value** | **Object** | Output only. The value of the parameter. &#x60;number_value&#x60; will be set if a parameter defined in StudySpec is in type &#39;INTEGER&#39;, &#39;DOUBLE&#39; or &#39;DISCRETE&#39;. &#x60;string_value&#x60; will be set if a parameter defined in StudySpec is in type &#39;CATEGORICAL&#39;. |  [optional] [readonly] |



