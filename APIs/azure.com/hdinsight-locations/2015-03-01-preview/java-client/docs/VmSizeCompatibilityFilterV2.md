

# VmSizeCompatibilityFilterV2

This class represent a single filter object that defines a multidimensional set. The dimensions of this set are Regions, ClusterFlavors, NodeTypes and ClusterVersions. The constraint should be defined based on the following: FilterMode (Exclude vs Include), VMSizes (the vm sizes in affect of exclusion/inclusion) and the ordering of the Filters. Later filters override previous settings if conflicted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterFlavors** | **List&lt;String&gt;** | The list of cluster flavors under the effect of the filter. |  [optional] |
|**clusterVersions** | **List&lt;String&gt;** | The list of cluster versions affected in Major.Minor format. |  [optional] |
|**filterMode** | [**FilterModeEnum**](#FilterModeEnum) | The filtering mode. Effectively this can enabling or disabling the VM sizes in a particular set. |  [optional] |
|**nodeTypes** | **List&lt;String&gt;** | The list of node types affected by the filter. |  [optional] |
|**osType** | [**List&lt;OsTypeEnum&gt;**](#List&lt;OsTypeEnum&gt;) | The OSType affected, Windows or Linux. |  [optional] |
|**regions** | **List&lt;String&gt;** | The list of regions under the effect of the filter. |  [optional] |
|**vmSizes** | **List&lt;String&gt;** | The list of virtual machine sizes to include or exclude. |  [optional] |



## Enum: FilterModeEnum

| Name | Value |
|---- | -----|
| EXCLUDE | &quot;Exclude&quot; |
| INCLUDE | &quot;Include&quot; |



## Enum: List&lt;OsTypeEnum&gt;

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



