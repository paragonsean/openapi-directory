

# SdkBug

A bug found in the Dataflow SDK.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**severity** | [**SeverityEnum**](#SeverityEnum) | Output only. How severe the SDK bug is. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Describes the impact of this SDK bug. |  [optional] [readonly] |
|**uri** | **String** | Output only. Link to more information on the bug. |  [optional] [readonly] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| NOTICE | &quot;NOTICE&quot; |
| WARNING | &quot;WARNING&quot; |
| SEVERE | &quot;SEVERE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GENERAL | &quot;GENERAL&quot; |
| PERFORMANCE | &quot;PERFORMANCE&quot; |
| DATALOSS | &quot;DATALOSS&quot; |



