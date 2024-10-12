

# StampCapacity

Class containing stamp capacity information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableCapacity** | **Long** | Available capacity (# of machines, bytes of storage etc...) |  [optional] |
|**computeMode** | [**ComputeModeEnum**](#ComputeModeEnum) | Shared/Dedicated workers |  [optional] |
|**excludeFromCapacityAllocation** | **Boolean** | If true it includes basic sites              Basic sites are not used for capacity allocation. |  [optional] |
|**isApplicableForAllComputeModes** | **Boolean** | Is capacity applicable for all sites? |  [optional] |
|**name** | **String** | Name of the stamp |  [optional] |
|**siteMode** | **String** | Shared or Dedicated |  [optional] |
|**totalCapacity** | **Long** | Total capacity (# of machines, bytes of storage etc...) |  [optional] |
|**unit** | **String** | Name of the unit |  [optional] |
|**workerSize** | [**WorkerSizeEnum**](#WorkerSizeEnum) | Size of the machines |  [optional] |
|**workerSizeId** | **Integer** | Size Id of machines:               0 - Small              1 - Medium              2 - Large |  [optional] |



## Enum: ComputeModeEnum

| Name | Value |
|---- | -----|
| SHARED | &quot;Shared&quot; |
| DEDICATED | &quot;Dedicated&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



## Enum: WorkerSizeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| SMALL | &quot;Small&quot; |
| MEDIUM | &quot;Medium&quot; |
| LARGE | &quot;Large&quot; |



