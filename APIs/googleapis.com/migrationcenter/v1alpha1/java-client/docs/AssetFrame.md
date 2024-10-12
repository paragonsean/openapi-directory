

# AssetFrame

Contains data reported from an inventory source on an asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, String&gt;** | Generic asset attributes. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs. |  [optional] |
|**performanceSamples** | [**List&lt;PerformanceSample&gt;**](PerformanceSample.md) | Asset performance data samples. Samples that are from more than 40 days ago or after tomorrow are ignored. |  [optional] |
|**reportTime** | **String** | The time the data was reported. |  [optional] |
|**traceToken** | **String** | Optional. Trace token is optionally provided to assist with debugging and traceability. |  [optional] |
|**virtualMachineDetails** | [**VirtualMachineDetails**](VirtualMachineDetails.md) |  |  [optional] |



