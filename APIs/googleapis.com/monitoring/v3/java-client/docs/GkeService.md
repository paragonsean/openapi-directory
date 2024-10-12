

# GkeService

GKE Service. The \"service\" here represents a Kubernetes service object (https://kubernetes.io/docs/concepts/services-networking/service). The field names correspond to the resource labels on k8s_service monitored resources (https://cloud.google.com/monitoring/api/resources#tag_k8s_service).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterName** | **String** | The name of the parent cluster. |  [optional] |
|**location** | **String** | The location of the parent cluster. This may be a zone or region. |  [optional] |
|**namespaceName** | **String** | The name of the parent namespace. |  [optional] |
|**projectId** | **String** | Output only. The project this resource lives in. For legacy services migrated from the Custom type, this may be a distinct project from the one parenting the service itself. |  [optional] [readonly] |
|**serviceName** | **String** | The name of this service. |  [optional] |



