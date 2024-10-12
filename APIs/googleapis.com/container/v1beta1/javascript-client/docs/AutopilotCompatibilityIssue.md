# KubernetesEngineApi.AutopilotCompatibilityIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraintType** | **String** | The constraint type of the issue. | [optional] 
**description** | **String** | The description of the issue. | [optional] 
**documentationUrl** | **String** | A URL to a public documnetation, which addresses resolving this issue. | [optional] 
**incompatibilityType** | **String** | The incompatibility type of this issue. | [optional] 
**lastObservation** | **String** | The last time when this issue was observed. | [optional] 
**subjects** | **[String]** | The name of the resources which are subject to this issue. | [optional] 



## Enum: IncompatibilityTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `INCOMPATIBILITY` (value: `"INCOMPATIBILITY"`)

* `ADDITIONAL_CONFIG_REQUIRED` (value: `"ADDITIONAL_CONFIG_REQUIRED"`)

* `PASSED_WITH_OPTIONAL_CONFIG` (value: `"PASSED_WITH_OPTIONAL_CONFIG"`)




