

# SdkVersion

The version of the SDK used to run the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bugs** | [**List&lt;SdkBug&gt;**](SdkBug.md) | Output only. Known bugs found in this SDK version. |  [optional] [readonly] |
|**sdkSupportStatus** | [**SdkSupportStatusEnum**](#SdkSupportStatusEnum) | The support status for this SDK version. |  [optional] |
|**version** | **String** | The version of the SDK used to run the job. |  [optional] |
|**versionDisplayName** | **String** | A readable string describing the version of the SDK. |  [optional] |



## Enum: SdkSupportStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| SUPPORTED | &quot;SUPPORTED&quot; |
| STALE | &quot;STALE&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| UNSUPPORTED | &quot;UNSUPPORTED&quot; |



