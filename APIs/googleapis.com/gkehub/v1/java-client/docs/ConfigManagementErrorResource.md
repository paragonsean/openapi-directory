

# ConfigManagementErrorResource

Model for a config file in the git repo with an associated Sync error

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceGvk** | [**ConfigManagementGroupVersionKind**](ConfigManagementGroupVersionKind.md) |  |  [optional] |
|**resourceName** | **String** | Metadata name of the resource that is causing an error |  [optional] |
|**resourceNamespace** | **String** | Namespace of the resource that is causing an error |  [optional] |
|**sourcePath** | **String** | Path in the git repo of the erroneous config |  [optional] |



