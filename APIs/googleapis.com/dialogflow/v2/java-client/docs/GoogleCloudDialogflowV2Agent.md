

# GoogleCloudDialogflowV2Agent

A Dialogflow agent is a virtual agent that handles conversations with your end-users. It is a natural language understanding module that understands the nuances of human language. Dialogflow translates end-user text or audio during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow agent to handle the types of conversations required for your system. For more information about agents, see the [Agent guide](https://cloud.google.com/dialogflow/docs/agents-overview). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | [**ApiVersionEnum**](#ApiVersionEnum) | Optional. API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query different service endpoints for different API versions. However, bots connectors and webhook calls will follow the specified API version. |  [optional] |
|**avatarUri** | **String** | Optional. The URI of the agent&#39;s avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. |  [optional] |
|**classificationThreshold** | **Float** | Optional. To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used. |  [optional] |
|**defaultLanguageCode** | **String** | Required. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the &#x60;Update&#x60; method. |  [optional] |
|**description** | **String** | Optional. The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected. |  [optional] |
|**displayName** | **String** | Required. The name of this agent. |  [optional] |
|**enableLogging** | **Boolean** | Optional. Determines whether this agent should log conversation queries. |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) | Optional. Determines how intents are detected from user queries. |  [optional] |
|**parent** | **String** | Required. The project of this agent. Format: &#x60;projects/&#x60;. |  [optional] |
|**supportedLanguageCodes** | **List&lt;String&gt;** | Optional. The list of all languages supported by this agent (except for the &#x60;default_language_code&#x60;). |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Optional. The agent tier. If not specified, TIER_STANDARD is assumed. |  [optional] |
|**timeZone** | **String** | Required. The time zone of this agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. |  [optional] |



## Enum: ApiVersionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;API_VERSION_UNSPECIFIED&quot; |
| V1 | &quot;API_VERSION_V1&quot; |
| V2 | &quot;API_VERSION_V2&quot; |
| V2_BETA_1 | &quot;API_VERSION_V2_BETA_1&quot; |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MATCH_MODE_UNSPECIFIED&quot; |
| HYBRID | &quot;MATCH_MODE_HYBRID&quot; |
| ML_ONLY | &quot;MATCH_MODE_ML_ONLY&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| STANDARD | &quot;TIER_STANDARD&quot; |
| ENTERPRISE | &quot;TIER_ENTERPRISE&quot; |
| ENTERPRISE_PLUS | &quot;TIER_ENTERPRISE_PLUS&quot; |



