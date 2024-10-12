

# SupportedService

`SupportedService` specifies the VPC Service Controls and its properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableOnRestrictedVip** | **Boolean** | True if the service is available on the restricted VIP. Services on the restricted VIP typically either support VPC Service Controls or are core infrastructure services required for the functioning of Google Cloud. |  [optional] |
|**knownLimitations** | **Boolean** | True if the service is supported with some limitations. Check [documentation](https://cloud.google.com/vpc-service-controls/docs/supported-products) for details. |  [optional] |
|**name** | **String** | The service name or address of the supported service, such as &#x60;service.googleapis.com&#x60;. |  [optional] |
|**supportStage** | [**SupportStageEnum**](#SupportStageEnum) | The support stage of the service. |  [optional] |
|**supportedMethods** | [**List&lt;MethodSelector&gt;**](MethodSelector.md) | The list of the supported methods. This field exists only in response to GetSupportedService |  [optional] |
|**title** | **String** | The name of the supported product, such as &#39;Cloud Product API&#39;. |  [optional] |



## Enum: SupportStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| PRELAUNCH | &quot;PRELAUNCH&quot; |
| EARLY_ACCESS | &quot;EARLY_ACCESS&quot; |
| ALPHA | &quot;ALPHA&quot; |
| BETA | &quot;BETA&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



