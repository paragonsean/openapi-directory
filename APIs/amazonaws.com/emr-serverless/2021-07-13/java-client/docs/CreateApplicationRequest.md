

# CreateApplicationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the application. |  [optional] |
|**releaseLabel** | **String** | The Amazon EMR release associated with the application. |  |
|**type** | **String** | The type of application you want to start, such as Spark or Hive. |  |
|**clientToken** | **String** | The client idempotency token of the application to create. Its value must be unique for each request. |  |
|**initialCapacity** | [**Map&lt;String, InitialCapacityConfig&gt;**](InitialCapacityConfig.md) | The capacity to initialize when the application is created. |  [optional] |
|**maximumCapacity** | [**CreateApplicationRequestMaximumCapacity**](CreateApplicationRequestMaximumCapacity.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags assigned to the application. |  [optional] |
|**autoStartConfiguration** | [**CreateApplicationRequestAutoStartConfiguration**](CreateApplicationRequestAutoStartConfiguration.md) |  |  [optional] |
|**autoStopConfiguration** | [**CreateApplicationRequestAutoStopConfiguration**](CreateApplicationRequestAutoStopConfiguration.md) |  |  [optional] |
|**networkConfiguration** | [**CreateApplicationRequestNetworkConfiguration**](CreateApplicationRequestNetworkConfiguration.md) |  |  [optional] |
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | The CPU architecture of an application. |  [optional] |
|**imageConfiguration** | [**CreateApplicationRequestImageConfiguration**](CreateApplicationRequestImageConfiguration.md) |  |  [optional] |
|**workerTypeSpecifications** | [**Map&lt;String, WorkerTypeSpecificationInput&gt;**](WorkerTypeSpecificationInput.md) | The key-value pairs that specify worker type to &lt;code&gt;WorkerTypeSpecificationInput&lt;/code&gt;. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include &lt;code&gt;Driver&lt;/code&gt; and &lt;code&gt;Executor&lt;/code&gt; for Spark applications and &lt;code&gt;HiveDriver&lt;/code&gt; and &lt;code&gt;TezTask&lt;/code&gt; for Hive applications. You can either set image details in this parameter for each worker type, or in &lt;code&gt;imageConfiguration&lt;/code&gt; for all worker types. |  [optional] |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| ARM64 | &quot;ARM64&quot; |
| X86_64 | &quot;X86_64&quot; |



