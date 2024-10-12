

# WorkloadProfile

workload resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**application** | [**Layer**](Layer.md) |  |  [optional] |
|**ascs** | [**Layer**](Layer.md) |  |  [optional] |
|**database** | [**Layer**](Layer.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. such as name, description, version. More example can be found in deployment |  [optional] |
|**name** | **String** | Identifier. name of resource names have the form &#39;projects/{project_id}/workloads/{workload_id}&#39; |  [optional] |
|**refreshedTime** | **String** | Required. time when the workload data was refreshed |  [optional] |
|**sapWorkload** | [**SapWorkload**](SapWorkload.md) |  |  [optional] |
|**sqlserverWorkload** | [**SqlserverWorkload**](SqlserverWorkload.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. [output only] the current state if a a workload |  [optional] [readonly] |
|**threeTierWorkload** | [**ThreeTierWorkload**](ThreeTierWorkload.md) |  |  [optional] |
|**workloadType** | [**WorkloadTypeEnum**](#WorkloadTypeEnum) | Required. The type of the workload |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DEPLOYING | &quot;DEPLOYING&quot; |
| DESTROYING | &quot;DESTROYING&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |



## Enum: WorkloadTypeEnum

| Name | Value |
|---- | -----|
| WORKLOAD_TYPE_UNSPECIFIED | &quot;WORKLOAD_TYPE_UNSPECIFIED&quot; |
| S4_HANA | &quot;S4_HANA&quot; |
| SQL_SERVER | &quot;SQL_SERVER&quot; |
| THREE_TIER_WEB_APP | &quot;THREE_TIER_WEB_APP&quot; |



