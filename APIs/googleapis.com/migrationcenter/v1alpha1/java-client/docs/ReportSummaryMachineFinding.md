

# ReportSummaryMachineFinding

A set of findings that applies to assets of type Virtual/Physical Machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocatedAssetCount** | **String** | Count of assets which were allocated. |  [optional] |
|**allocatedDiskTypes** | [**List&lt;AllocatedDiskTypesEnum&gt;**](#List&lt;AllocatedDiskTypesEnum&gt;) | Set of disk types allocated to assets. |  [optional] |
|**allocatedRegions** | **List&lt;String&gt;** | Set of regions in which the assets were allocated. |  [optional] |
|**machineSeriesAllocations** | [**List&lt;ReportSummaryMachineSeriesAllocation&gt;**](ReportSummaryMachineSeriesAllocation.md) | Distribution of assets based on the Machine Series. |  [optional] |



## Enum: List&lt;AllocatedDiskTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PERSISTENT_DISK_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;PERSISTENT_DISK_TYPE_STANDARD&quot; |
| BALANCED | &quot;PERSISTENT_DISK_TYPE_BALANCED&quot; |
| SSD | &quot;PERSISTENT_DISK_TYPE_SSD&quot; |



