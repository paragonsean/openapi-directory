# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1EngineChatEngineConfigAgentCreationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business** | **String** | Name of the company, organization or other entity that the agent represents. Used for knowledge connector LLM prompt and for knowledge search. | [optional] 
**defaultLanguageCode** | **String** | Required. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. | [optional] 
**location** | **String** | Agent location for Agent creation, supported values: global/us/eu. If not provided, us Engine will create Agent using us-central-1 by default; eu Engine will create Agent using eu-west-1 by default. | [optional] 
**timeZone** | **String** | Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. | [optional] 


