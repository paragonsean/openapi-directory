

# GoogleCloudAiplatformV1beta1SafetySetting

Safety settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | Required. Harm category. |  [optional] |
|**threshold** | [**ThresholdEnum**](#ThresholdEnum) | Required. The harm block threshold. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;HARM_CATEGORY_UNSPECIFIED&quot; |
| HATE_SPEECH | &quot;HARM_CATEGORY_HATE_SPEECH&quot; |
| DANGEROUS_CONTENT | &quot;HARM_CATEGORY_DANGEROUS_CONTENT&quot; |
| HARASSMENT | &quot;HARM_CATEGORY_HARASSMENT&quot; |
| SEXUALLY_EXPLICIT | &quot;HARM_CATEGORY_SEXUALLY_EXPLICIT&quot; |



## Enum: ThresholdEnum

| Name | Value |
|---- | -----|
| HARM_BLOCK_THRESHOLD_UNSPECIFIED | &quot;HARM_BLOCK_THRESHOLD_UNSPECIFIED&quot; |
| BLOCK_LOW_AND_ABOVE | &quot;BLOCK_LOW_AND_ABOVE&quot; |
| BLOCK_MEDIUM_AND_ABOVE | &quot;BLOCK_MEDIUM_AND_ABOVE&quot; |
| BLOCK_ONLY_HIGH | &quot;BLOCK_ONLY_HIGH&quot; |
| BLOCK_NONE | &quot;BLOCK_NONE&quot; |



