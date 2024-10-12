

# DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner

Stamp capacity information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableCapacity** | **Long** | Available capacity (# of machines, bytes of storage etc...). |  [optional] |
|**computeMode** | [**ComputeModeEnum**](#ComputeModeEnum) | Shared/dedicated workers. |  [optional] |
|**excludeFromCapacityAllocation** | **Boolean** | If &lt;code&gt;true&lt;/code&gt;, it includes basic apps. Basic apps are not used for capacity allocation. |  [optional] |
|**isApplicableForAllComputeModes** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if capacity is applicable for all apps; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**isLinux** | **Boolean** | Is this a linux stamp capacity |  [optional] |
|**name** | **String** | Name of the stamp. |  [optional] |
|**siteMode** | **String** | Shared or Dedicated. |  [optional] |
|**totalCapacity** | **Long** | Total capacity (# of machines, bytes of storage etc...). |  [optional] |
|**unit** | **String** | Name of the unit. |  [optional] |
|**workerSize** | [**WorkerSizeEnum**](#WorkerSizeEnum) | Size of the machines. |  [optional] |
|**workerSizeId** | **Integer** | Size ID of machines:  0 - Small 1 - Medium 2 - Large |  [optional] |



## Enum: ComputeModeEnum

| Name | Value |
|---- | -----|
| SHARED | &quot;Shared&quot; |
| DEDICATED | &quot;Dedicated&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



## Enum: WorkerSizeEnum

| Name | Value |
|---- | -----|
| SMALL | &quot;Small&quot; |
| MEDIUM | &quot;Medium&quot; |
| LARGE | &quot;Large&quot; |
| D1 | &quot;D1&quot; |
| D2 | &quot;D2&quot; |
| D3 | &quot;D3&quot; |
| NESTED_SMALL | &quot;NestedSmall&quot; |
| DEFAULT | &quot;Default&quot; |



