

# GkeWorkload

A GKE Workload (Deployment, StatefulSet, etc). The field names correspond to the metadata labels on monitored resources that fall under a workload (for example, k8s_container or k8s_pod).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterName** | **String** | The name of the parent cluster. |  [optional] |
|**location** | **String** | The location of the parent cluster. This may be a zone or region. |  [optional] |
|**namespaceName** | **String** | The name of the parent namespace. |  [optional] |
|**projectId** | **String** | Output only. The project this resource lives in. For legacy services migrated from the Custom type, this may be a distinct project from the one parenting the service itself. |  [optional] [readonly] |
|**topLevelControllerName** | **String** | The name of this workload. |  [optional] |
|**topLevelControllerType** | **String** | The type of this workload (for example, \&quot;Deployment\&quot; or \&quot;DaemonSet\&quot;) |  [optional] |



