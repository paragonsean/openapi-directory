

# GoogleCloudAiplatformV1beta1SafetyRating

Safety rating corresponding to the generated content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocked** | **Boolean** | Output only. Indicates whether the content was filtered out because of this rating. |  [optional] [readonly] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Output only. Harm category. |  [optional] [readonly] |
|**probability** | [**ProbabilityEnum**](#ProbabilityEnum) | Output only. Harm probability levels in the content. |  [optional] [readonly] |
|**probabilityScore** | **Float** | Output only. Harm probability score. |  [optional] [readonly] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Output only. Harm severity levels in the content. |  [optional] [readonly] |
|**severityScore** | **Float** | Output only. Harm severity score. |  [optional] [readonly] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;HARM_CATEGORY_UNSPECIFIED&quot; |
| HATE_SPEECH | &quot;HARM_CATEGORY_HATE_SPEECH&quot; |
| DANGEROUS_CONTENT | &quot;HARM_CATEGORY_DANGEROUS_CONTENT&quot; |
| HARASSMENT | &quot;HARM_CATEGORY_HARASSMENT&quot; |
| SEXUALLY_EXPLICIT | &quot;HARM_CATEGORY_SEXUALLY_EXPLICIT&quot; |



## Enum: ProbabilityEnum

| Name | Value |
|---- | -----|
| HARM_PROBABILITY_UNSPECIFIED | &quot;HARM_PROBABILITY_UNSPECIFIED&quot; |
| NEGLIGIBLE | &quot;NEGLIGIBLE&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;HARM_SEVERITY_UNSPECIFIED&quot; |
| NEGLIGIBLE | &quot;HARM_SEVERITY_NEGLIGIBLE&quot; |
| LOW | &quot;HARM_SEVERITY_LOW&quot; |
| MEDIUM | &quot;HARM_SEVERITY_MEDIUM&quot; |
| HIGH | &quot;HARM_SEVERITY_HIGH&quot; |



