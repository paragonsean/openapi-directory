

# Fleet

Fleet is the fleet configuration for the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**membership** | **String** | [Output only] The full resource name of the registered fleet membership of the cluster, in the format &#x60;//gkehub.googleapis.com/projects/_*_/locations/_*_/memberships/_*&#x60;. |  [optional] |
|**preRegistered** | **Boolean** | [Output only] Whether the cluster has been registered through the fleet API. |  [optional] |
|**project** | **String** | The Fleet host project(project ID or project number) where this cluster will be registered to. This field cannot be changed after the cluster has been registered. |  [optional] |



