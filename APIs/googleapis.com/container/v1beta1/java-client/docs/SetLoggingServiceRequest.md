

# SetLoggingServiceRequest

SetLoggingServiceRequest sets the logging service of a cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterId** | **String** | Required. Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field. |  [optional] |
|**loggingService** | **String** | Required. The logging service the cluster should use to write logs. Currently available options: * &#x60;logging.googleapis.com/kubernetes&#x60; - The Cloud Logging service with a Kubernetes-native resource model * &#x60;logging.googleapis.com&#x60; - The legacy Cloud Logging service (no longer available as of GKE 1.15). * &#x60;none&#x60; - no logs will be exported from the cluster. If left as an empty string,&#x60;logging.googleapis.com/kubernetes&#x60; will be used for GKE 1.14+ or &#x60;logging.googleapis.com&#x60; for earlier versions. |  [optional] |
|**name** | **String** | The name (project, location, cluster) of the cluster to set logging. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*&#x60;. |  [optional] |
|**projectId** | **String** | Required. Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. |  [optional] |
|**zone** | **String** | Required. Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. |  [optional] |



