# FabricAdminClient.ScaleUnitModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isMultiNode** | **Boolean** | Denotes if more than one node in cluster. | [optional] 
**logicalFaultDomain** | **Number** | Fault domain name of the cluster. | [optional] 
**model** | **String** | Model of the servers in the cluster. | [optional] 
**nodes** | **[String]** | List of nodes in the server. | [optional] 
**scaleUnitType** | **String** | Type of cluster. | [optional] 
**state** | **String** | Current state of the cluster. | [optional] 
**totalCapacity** | [**ScaleUnitCapacity**](ScaleUnitCapacity.md) |  | [optional] 



## Enum: ScaleUnitTypeEnum


* `Unknown` (value: `"Unknown"`)

* `ComputeOnly` (value: `"ComputeOnly"`)

* `StorageOnly` (value: `"StorageOnly"`)

* `HyperConverged` (value: `"HyperConverged"`)





## Enum: StateEnum


* `Unknown` (value: `"Unknown"`)

* `Creating` (value: `"Creating"`)

* `Running` (value: `"Running"`)

* `Upgrading` (value: `"Upgrading"`)

* `Deleting` (value: `"Deleting"`)




