# DialogflowApi.GoogleCloudDialogflowV2Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersion** | **String** | Optional. API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query different service endpoints for different API versions. However, bots connectors and webhook calls will follow the specified API version. | [optional] 
**avatarUri** | **String** | Optional. The URI of the agent&#39;s avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. | [optional] 
**classificationThreshold** | **Number** | Optional. To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used. | [optional] 
**defaultLanguageCode** | **String** | Required. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the &#x60;Update&#x60; method. | [optional] 
**description** | **String** | Optional. The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected. | [optional] 
**displayName** | **String** | Required. The name of this agent. | [optional] 
**enableLogging** | **Boolean** | Optional. Determines whether this agent should log conversation queries. | [optional] 
**matchMode** | **String** | Optional. Determines how intents are detected from user queries. | [optional] 
**parent** | **String** | Required. The project of this agent. Format: &#x60;projects/&#x60;. | [optional] 
**supportedLanguageCodes** | **[String]** | Optional. The list of all languages supported by this agent (except for the &#x60;default_language_code&#x60;). | [optional] 
**tier** | **String** | Optional. The agent tier. If not specified, TIER_STANDARD is assumed. | [optional] 
**timeZone** | **String** | Required. The time zone of this agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. | [optional] 



## Enum: ApiVersionEnum


* `UNSPECIFIED` (value: `"API_VERSION_UNSPECIFIED"`)

* `V1` (value: `"API_VERSION_V1"`)

* `V2` (value: `"API_VERSION_V2"`)

* `V2_BETA_1` (value: `"API_VERSION_V2_BETA_1"`)





## Enum: MatchModeEnum


* `UNSPECIFIED` (value: `"MATCH_MODE_UNSPECIFIED"`)

* `HYBRID` (value: `"MATCH_MODE_HYBRID"`)

* `ML_ONLY` (value: `"MATCH_MODE_ML_ONLY"`)





## Enum: TierEnum


* `UNSPECIFIED` (value: `"TIER_UNSPECIFIED"`)

* `STANDARD` (value: `"TIER_STANDARD"`)

* `ENTERPRISE` (value: `"TIER_ENTERPRISE"`)

* `ENTERPRISE_PLUS` (value: `"TIER_ENTERPRISE_PLUS"`)




