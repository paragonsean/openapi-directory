# ApiManagementClient.ApiDiagnosticListByService200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alwaysLog** | **String** | Specifies for what type of messages sampling settings should not apply. | [optional] 
**backend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  | [optional] 
**enableHttpCorrelationHeaders** | **Boolean** | Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true. | [optional] 
**frontend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  | [optional] 
**httpCorrelationProtocol** | **String** | Sets correlation protocol to use for Application Insights diagnostics. | [optional] 
**loggerId** | **String** | Resource Id of a target logger. | 
**sampling** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling**](ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling.md) |  | [optional] 
**verbosity** | **String** | The verbosity level applied to traces emitted by trace policies. | [optional] 



## Enum: AlwaysLogEnum


* `allErrors` (value: `"allErrors"`)





## Enum: HttpCorrelationProtocolEnum


* `None` (value: `"None"`)

* `Legacy` (value: `"Legacy"`)

* `W3C` (value: `"W3C"`)





## Enum: VerbosityEnum


* `verbose` (value: `"verbose"`)

* `information` (value: `"information"`)

* `error` (value: `"error"`)




