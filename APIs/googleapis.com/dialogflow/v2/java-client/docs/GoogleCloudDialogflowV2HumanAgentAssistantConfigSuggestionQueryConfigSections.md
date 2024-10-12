

# GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigSections

Custom sections to return when requesting a summary of a conversation. This is only supported when `baseline_model_version` == '2.0'. Supported features: CONVERSATION_SUMMARIZATION, CONVERSATION_SUMMARIZATION_VOICE.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sectionTypes** | [**List&lt;SectionTypesEnum&gt;**](#List&lt;SectionTypesEnum&gt;) | The selected sections chosen to return when requesting a summary of a conversation. A duplicate selected section will be treated as a single selected section. If section types are not provided, the default will be {SITUATION, ACTION, RESULT}. |  [optional] |



## Enum: List&lt;SectionTypesEnum&gt;

| Name | Value |
|---- | -----|
| SECTION_TYPE_UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| SITUATION | &quot;SITUATION&quot; |
| ACTION | &quot;ACTION&quot; |
| RESOLUTION | &quot;RESOLUTION&quot; |
| REASON_FOR_CANCELLATION | &quot;REASON_FOR_CANCELLATION&quot; |
| CUSTOMER_SATISFACTION | &quot;CUSTOMER_SATISFACTION&quot; |
| ENTITIES | &quot;ENTITIES&quot; |



