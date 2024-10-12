# WorkloadManagerApi.WorkloadProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Layer**](Layer.md) |  | [optional] 
**ascs** | [**Layer**](Layer.md) |  | [optional] 
**database** | [**Layer**](Layer.md) |  | [optional] 
**labels** | **{String: String}** | Optional. such as name, description, version. More example can be found in deployment | [optional] 
**name** | **String** | Identifier. name of resource names have the form &#39;projects/{project_id}/workloads/{workload_id}&#39; | [optional] 
**refreshedTime** | **String** | Required. time when the workload data was refreshed | [optional] 
**sapWorkload** | [**SapWorkload**](SapWorkload.md) |  | [optional] 
**sqlserverWorkload** | [**SqlserverWorkload**](SqlserverWorkload.md) |  | [optional] 
**state** | **String** | Output only. [output only] the current state if a a workload | [optional] [readonly] 
**threeTierWorkload** | [**ThreeTierWorkload**](ThreeTierWorkload.md) |  | [optional] 
**workloadType** | **String** | Required. The type of the workload | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DEPLOYING` (value: `"DEPLOYING"`)

* `DESTROYING` (value: `"DESTROYING"`)

* `MAINTENANCE` (value: `"MAINTENANCE"`)





## Enum: WorkloadTypeEnum


* `WORKLOAD_TYPE_UNSPECIFIED` (value: `"WORKLOAD_TYPE_UNSPECIFIED"`)

* `S4_HANA` (value: `"S4_HANA"`)

* `SQL_SERVER` (value: `"SQL_SERVER"`)

* `THREE_TIER_WEB_APP` (value: `"THREE_TIER_WEB_APP"`)




