# WebSiteManagementClient.StampCapacity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableCapacity** | **Number** | Available capacity (# of machines, bytes of storage etc...) | [optional] 
**computeMode** | **String** | Shared/Dedicated workers | [optional] 
**excludeFromCapacityAllocation** | **Boolean** | If true it includes basic sites              Basic sites are not used for capacity allocation. | [optional] 
**isApplicableForAllComputeModes** | **Boolean** | Is capacity applicable for all sites? | [optional] 
**name** | **String** | Name of the stamp | [optional] 
**siteMode** | **String** | Shared or Dedicated | [optional] 
**totalCapacity** | **Number** | Total capacity (# of machines, bytes of storage etc...) | [optional] 
**unit** | **String** | Name of the unit | [optional] 
**workerSize** | **String** | Size of the machines | [optional] 
**workerSizeId** | **Number** | Size Id of machines:               0 - Small              1 - Medium              2 - Large | [optional] 



## Enum: ComputeModeEnum


* `Shared` (value: `"Shared"`)

* `Dedicated` (value: `"Dedicated"`)

* `Dynamic` (value: `"Dynamic"`)





## Enum: WorkerSizeEnum


* `Default` (value: `"Default"`)

* `Small` (value: `"Small"`)

* `Medium` (value: `"Medium"`)

* `Large` (value: `"Large"`)




