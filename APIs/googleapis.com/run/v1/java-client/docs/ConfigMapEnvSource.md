

# ConfigMapEnvSource

Not supported by Cloud Run. ConfigMapEnvSource selects a ConfigMap to populate the environment variables with. The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localObjectReference** | [**LocalObjectReference**](LocalObjectReference.md) |  |  [optional] |
|**name** | **String** | The ConfigMap to select from. |  [optional] |
|**optional** | **Boolean** | Specify whether the ConfigMap must be defined. |  [optional] |



