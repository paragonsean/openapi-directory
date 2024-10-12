# ApiManagementClient.ApiDiagnosticListByService200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alwaysLog** | **String** | Specifies for what type of messages sampling settings should not apply. | [optional] 
**backend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  | [optional] 
**enableHttpCorrelationHeaders** | **Boolean** | Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true. | [optional] 
**frontend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  | [optional] 
**loggerId** | **String** | Resource Id of a target logger. | 
**sampling** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling**](ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling.md) |  | [optional] 



## Enum: AlwaysLogEnum


* `allErrors` (value: `"allErrors"`)




