# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaLoggingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultLogGenerationRule** | [**GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule**](GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule.md) |  | [optional] 
**name** | **String** | Required. Immutable. The name of the LoggingConfig singleton resource. Format: projects/_*_/loggingConfig | [optional] 
**serviceLogGenerationRules** | [**[GoogleCloudRetailV2alphaLoggingConfigServiceLogGenerationRule]**](GoogleCloudRetailV2alphaLoggingConfigServiceLogGenerationRule.md) | Controls logging configurations more granularly for each supported service. This overrides the default_log_generation_rule for the services specified. For those not mentioned, they will fallback to the default log generation rule. | [optional] 


