# AccessContextManagerApi.SupportedService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableOnRestrictedVip** | **Boolean** | True if the service is available on the restricted VIP. Services on the restricted VIP typically either support VPC Service Controls or are core infrastructure services required for the functioning of Google Cloud. | [optional] 
**knownLimitations** | **Boolean** | True if the service is supported with some limitations. Check [documentation](https://cloud.google.com/vpc-service-controls/docs/supported-products) for details. | [optional] 
**name** | **String** | The service name or address of the supported service, such as &#x60;service.googleapis.com&#x60;. | [optional] 
**supportStage** | **String** | The support stage of the service. | [optional] 
**supportedMethods** | [**[MethodSelector]**](MethodSelector.md) | The list of the supported methods. This field exists only in response to GetSupportedService | [optional] 
**title** | **String** | The name of the supported product, such as &#39;Cloud Product API&#39;. | [optional] 



## Enum: SupportStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)




