# HdInsightManagementClient.VmSizeCompatibilityFilterV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterFlavors** | **[String]** | The list of cluster flavors under the effect of the filter. | [optional] 
**clusterVersions** | **[String]** | The list of cluster versions affected in Major.Minor format. | [optional] 
**filterMode** | **String** | The filtering mode. Effectively this can enabling or disabling the VM sizes in a particular set. | [optional] 
**nodeTypes** | **[String]** | The list of node types affected by the filter. | [optional] 
**osType** | **[String]** | The OSType affected, Windows or Linux. | [optional] 
**regions** | **[String]** | The list of regions under the effect of the filter. | [optional] 
**vmSizes** | **[String]** | The list of virtual machine sizes to include or exclude. | [optional] 



## Enum: FilterModeEnum


* `Exclude` (value: `"Exclude"`)

* `Include` (value: `"Include"`)





## Enum: [OsTypeEnum]


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




