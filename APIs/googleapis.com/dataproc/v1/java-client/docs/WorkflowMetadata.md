

# WorkflowMetadata

A Dataproc workflow template resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterName** | **String** | Output only. The name of the target cluster. |  [optional] [readonly] |
|**clusterUuid** | **String** | Output only. The UUID of target cluster. |  [optional] [readonly] |
|**createCluster** | [**ClusterOperation**](ClusterOperation.md) |  |  [optional] |
|**dagEndTime** | **String** | Output only. DAG end time, only set for workflows with dag_timeout when DAG ends. |  [optional] [readonly] |
|**dagStartTime** | **String** | Output only. DAG start time, only set for workflows with dag_timeout when DAG begins. |  [optional] [readonly] |
|**dagTimeout** | **String** | Output only. The timeout duration for the DAG of jobs, expressed in seconds (see JSON representation of duration (https://developers.google.com/protocol-buffers/docs/proto3#json)). |  [optional] [readonly] |
|**deleteCluster** | [**ClusterOperation**](ClusterOperation.md) |  |  [optional] |
|**endTime** | **String** | Output only. Workflow end time. |  [optional] [readonly] |
|**graph** | [**WorkflowGraph**](WorkflowGraph.md) |  |  [optional] |
|**parameters** | **Map&lt;String, String&gt;** | Map from parameter names to values that were used for those parameters. |  [optional] |
|**startTime** | **String** | Output only. Workflow start time. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The workflow state. |  [optional] [readonly] |
|**template** | **String** | Output only. The resource name of the workflow template as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/regions/{region}/workflowTemplates/{template_id} For projects.locations.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/locations/{location}/workflowTemplates/{template_id} |  [optional] [readonly] |
|**version** | **Integer** | Output only. The version of template at the time of workflow instantiation. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |



