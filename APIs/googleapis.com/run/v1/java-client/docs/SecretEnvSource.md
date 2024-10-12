

# SecretEnvSource

Not supported by Cloud Run. SecretEnvSource selects a Secret to populate the environment variables with. The contents of the target Secret's Data field will represent the key-value pairs as environment variables.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localObjectReference** | [**LocalObjectReference**](LocalObjectReference.md) |  |  [optional] |
|**name** | **String** | The Secret to select from. |  [optional] |
|**optional** | **Boolean** | Specify whether the Secret must be defined |  [optional] |



