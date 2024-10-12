

# UserWorkloadsConfigMap

User workloads ConfigMap used by Airflow tasks that run with Kubernetes executor or KubernetesPodOperator.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Map&lt;String, String&gt;** | Optional. The \&quot;data\&quot; field of Kubernetes ConfigMap, organized in key-value pairs. For details see: https://kubernetes.io/docs/concepts/configuration/configmap/ |  [optional] |
|**name** | **String** | Identifier. The resource name of the ConfigMap, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}\&quot; |  [optional] |



