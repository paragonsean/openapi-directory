

# GoogleCloudRetailV2alphaLoggingConfig

Project level logging config to control what level of log will be generated and written to Cloud Logging.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultLogGenerationRule** | [**GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule**](GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule.md) |  |  [optional] |
|**name** | **String** | Required. Immutable. The name of the LoggingConfig singleton resource. Format: projects/_*_/loggingConfig |  [optional] |
|**serviceLogGenerationRules** | [**List&lt;GoogleCloudRetailV2alphaLoggingConfigServiceLogGenerationRule&gt;**](GoogleCloudRetailV2alphaLoggingConfigServiceLogGenerationRule.md) | Controls logging configurations more granularly for each supported service. This overrides the default_log_generation_rule for the services specified. For those not mentioned, they will fallback to the default log generation rule. |  [optional] |



