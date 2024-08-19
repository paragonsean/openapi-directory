

# CapabilitiesResult

The Get Capabilities operation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**features** | **List&lt;String&gt;** | The capability features. |  [optional] |
|**quota** | [**QuotaCapability**](QuotaCapability.md) |  |  [optional] |
|**regions** | [**Map&lt;String, RegionsCapability&gt;**](RegionsCapability.md) | The virtual machine size compatibility features. |  [optional] |
|**versions** | [**Map&lt;String, VersionsCapability&gt;**](VersionsCapability.md) | The version capability. |  [optional] |
|**vmSizeFilters** | [**List&lt;VmSizeCompatibilityFilter&gt;**](VmSizeCompatibilityFilter.md) | The virtual machine size compatibility filters. |  [optional] |
|**vmSizes** | [**Map&lt;String, VmSizesCapability&gt;**](VmSizesCapability.md) | The virtual machine sizes. |  [optional] |



