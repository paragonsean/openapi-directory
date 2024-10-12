# HdInsightManagementClient.CapabilitiesResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **[String]** | The capabilty features. | [optional] 
**quota** | [**QuotaCapability**](QuotaCapability.md) |  | [optional] 
**regions** | [**{String: RegionsCapability}**](RegionsCapability.md) | The virtual machine size compatibilty features. | [optional] 
**versions** | [**{String: VersionsCapability}**](VersionsCapability.md) | The version capability. | [optional] 
**vmSizeFilters** | [**[VmSizeCompatibilityFilter]**](VmSizeCompatibilityFilter.md) | The virtual machine size compatibilty filters. | [optional] 
**vmSizes** | [**{String: VmSizesCapability}**](VmSizesCapability.md) | The virtual machine sizes. | [optional] 


