

# ServiceNetworking

Information about the Kubernetes Service networking configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployment** | **String** | Required. Name of the Kubernetes Deployment whose traffic is managed by the specified Service. |  [optional] |
|**disablePodOverprovisioning** | **Boolean** | Optional. Whether to disable Pod overprovisioning. If Pod overprovisioning is disabled then Cloud Deploy will limit the number of total Pods used for the deployment strategy to the number of Pods the Deployment has on the cluster. |  [optional] |
|**service** | **String** | Required. Name of the Kubernetes Service. |  [optional] |



