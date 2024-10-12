# CloudDataplexApi.GoogleCloudDataplexV1EnvironmentSessionSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableFastStartup** | **Boolean** | Optional. If True, this causes sessions to be pre-created and available for faster startup to enable interactive exploration use-cases. This defaults to False to avoid additional billed charges. These can only be set to True for the environment with name set to \&quot;default\&quot;, and with default configuration. | [optional] 
**maxIdleDuration** | **String** | Optional. The idle time configuration of the session. The session will be auto-terminated at the end of this period. | [optional] 


