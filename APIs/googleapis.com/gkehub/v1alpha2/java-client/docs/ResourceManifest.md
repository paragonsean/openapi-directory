

# ResourceManifest

ResourceManifest represents a single Kubernetes resource to be applied to the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterScoped** | **Boolean** | Whether the resource provided in the manifest is &#x60;cluster_scoped&#x60;. If unset, the manifest is assumed to be namespace scoped. This field is used for REST mapping when applying the resource in a cluster. |  [optional] |
|**manifest** | **String** | YAML manifest of the resource. |  [optional] |



