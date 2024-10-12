# CloudDataprocApi.NodePool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Required. A unique id of the node pool. Primary and Secondary workers can be specified using special reserved ids PRIMARY_WORKER_POOL and SECONDARY_WORKER_POOL respectively. Aux node pools can be referenced using corresponding pool id. | [optional] 
**instanceNames** | **[String]** | Name of instances to be repaired. These instances must belong to specified node pool. | [optional] 
**repairAction** | **String** | Required. Repair action to take on specified resources of the node pool. | [optional] 



## Enum: RepairActionEnum


* `REPAIR_ACTION_UNSPECIFIED` (value: `"REPAIR_ACTION_UNSPECIFIED"`)

* `DELETE` (value: `"DELETE"`)




