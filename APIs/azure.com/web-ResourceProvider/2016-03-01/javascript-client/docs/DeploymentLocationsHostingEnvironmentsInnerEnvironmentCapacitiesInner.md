# ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableCapacity** | **Number** | Available capacity (# of machines, bytes of storage etc...). | [optional] 
**computeMode** | **String** | Shared/dedicated workers. | [optional] 
**excludeFromCapacityAllocation** | **Boolean** | If &lt;code&gt;true&lt;/code&gt;, it includes basic apps. Basic apps are not used for capacity allocation. | [optional] 
**isApplicableForAllComputeModes** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if capacity is applicable for all apps; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**name** | **String** | Name of the stamp. | [optional] 
**siteMode** | **String** | Shared or Dedicated. | [optional] 
**totalCapacity** | **Number** | Total capacity (# of machines, bytes of storage etc...). | [optional] 
**unit** | **String** | Name of the unit. | [optional] 
**workerSize** | **String** | Size of the machines. | [optional] 
**workerSizeId** | **Number** | Size ID of machines:  0 - Small 1 - Medium 2 - Large | [optional] 



## Enum: ComputeModeEnum


* `Shared` (value: `"Shared"`)

* `Dedicated` (value: `"Dedicated"`)

* `Dynamic` (value: `"Dynamic"`)





## Enum: WorkerSizeEnum


* `Default` (value: `"Default"`)

* `Small` (value: `"Small"`)

* `Medium` (value: `"Medium"`)

* `Large` (value: `"Large"`)

* `D1` (value: `"D1"`)

* `D2` (value: `"D2"`)

* `D3` (value: `"D3"`)




