# MigrationCenterApi.AssetFrame

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Generic asset attributes. | [optional] 
**labels** | **{String: String}** | Labels as key value pairs. | [optional] 
**performanceSamples** | [**[PerformanceSample]**](PerformanceSample.md) | Asset performance data samples. Samples that are from more than 40 days ago or after tomorrow are ignored. | [optional] 
**reportTime** | **String** | The time the data was reported. | [optional] 
**traceToken** | **String** | Optional. Trace token is optionally provided to assist with debugging and traceability. | [optional] 
**virtualMachineDetails** | [**VirtualMachineDetails**](VirtualMachineDetails.md) |  | [optional] 


