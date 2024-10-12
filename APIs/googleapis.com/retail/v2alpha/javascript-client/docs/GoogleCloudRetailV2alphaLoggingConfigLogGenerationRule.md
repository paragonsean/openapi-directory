# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infoLogSampleRate** | **Number** | The log sample rate for INFO level log entries. You can use this to reduce the number of entries generated for INFO level logs. DO NOT set this field if the logging_level is not LoggingLevel.LOG_ALL. Otherwise, an INVALID_ARGUMENT error is returned. Sample rate for INFO logs defaults to 1 when unset (generate and send all INFO logs to Cloud Logging). Its value must be greater than 0 and less than or equal to 1. | [optional] 
**loggingLevel** | **String** | The logging level. By default it is set to &#x60;LOG_WARNINGS_AND_ABOVE&#x60;. | [optional] 



## Enum: LoggingLevelEnum


* `LOGGING_LEVEL_UNSPECIFIED` (value: `"LOGGING_LEVEL_UNSPECIFIED"`)

* `LOGGING_DISABLED` (value: `"LOGGING_DISABLED"`)

* `LOG_ERRORS_AND_ABOVE` (value: `"LOG_ERRORS_AND_ABOVE"`)

* `LOG_WARNINGS_AND_ABOVE` (value: `"LOG_WARNINGS_AND_ABOVE"`)

* `LOG_ALL` (value: `"LOG_ALL"`)




