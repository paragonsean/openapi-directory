# KubernetesEngineApi.UpdateMasterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterId** | **String** | Required. Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field. | [optional] 
**masterVersion** | **String** | Required. The Kubernetes version to change the master to. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - \&quot;latest\&quot;: picks the highest valid Kubernetes version - \&quot;1.X\&quot;: picks the highest valid patch+gke.N patch in the 1.X version - \&quot;1.X.Y\&quot;: picks the highest valid gke.N patch in the 1.X.Y version - \&quot;1.X.Y-gke.N\&quot;: picks an explicit Kubernetes version - \&quot;-\&quot;: picks the default Kubernetes version | [optional] 
**name** | **String** | The name (project, location, cluster) of the cluster to update. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*&#x60;. | [optional] 
**projectId** | **String** | Required. Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. | [optional] 
**zone** | **String** | Required. Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. | [optional] 


