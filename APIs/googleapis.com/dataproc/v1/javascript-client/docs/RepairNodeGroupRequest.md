# CloudDataprocApi.RepairNodeGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceNames** | **[String]** | Required. Name of instances to be repaired. These instances must belong to specified node pool. | [optional] 
**repairAction** | **String** | Required. Repair action to take on specified resources of the node pool. | [optional] 
**requestId** | **String** | Optional. A unique ID used to identify the request. If the server receives two RepairNodeGroupRequest with the same ID, the second request is ignored and the first google.longrunning.Operation created and stored in the backend is returned.Recommendation: Set this value to a UUID (https://en.wikipedia.org/wiki/Universally_unique_identifier).The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. | [optional] 



## Enum: RepairActionEnum


* `REPAIR_ACTION_UNSPECIFIED` (value: `"REPAIR_ACTION_UNSPECIFIED"`)

* `REPLACE` (value: `"REPLACE"`)




