# MigrationCenterApi.ReportSummaryMachineFinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocatedAssetCount** | **String** | Count of assets which were allocated. | [optional] 
**allocatedDiskTypes** | **[String]** | Set of disk types allocated to assets. | [optional] 
**allocatedRegions** | **[String]** | Set of regions in which the assets were allocated. | [optional] 
**machineSeriesAllocations** | [**[ReportSummaryMachineSeriesAllocation]**](ReportSummaryMachineSeriesAllocation.md) | Distribution of assets based on the Machine Series. | [optional] 



## Enum: [AllocatedDiskTypesEnum]


* `UNSPECIFIED` (value: `"PERSISTENT_DISK_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"PERSISTENT_DISK_TYPE_STANDARD"`)

* `BALANCED` (value: `"PERSISTENT_DISK_TYPE_BALANCED"`)

* `SSD` (value: `"PERSISTENT_DISK_TYPE_SSD"`)




