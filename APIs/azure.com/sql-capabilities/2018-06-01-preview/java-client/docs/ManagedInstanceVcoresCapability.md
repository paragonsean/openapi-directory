

# ManagedInstanceVcoresCapability

The managed instance virtual cores capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  |  [optional] |
|**instancePoolSupported** | **Boolean** | True if this service objective is supported for managed instances in an instance pool. |  [optional] [readonly] |
|**name** | **String** | The virtual cores identifier. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**standaloneSupported** | **Boolean** | True if this service objective is supported for standalone managed instances. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedStorageSizes** | [**List&lt;MaxSizeRangeCapability&gt;**](MaxSizeRangeCapability.md) | Storage size ranges. |  [optional] [readonly] |
|**value** | **Integer** | The virtual cores value. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



