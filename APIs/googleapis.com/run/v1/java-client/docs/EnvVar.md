

# EnvVar

EnvVar represents an environment variable present in a Container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. Name of the environment variable. |  [optional] |
|**value** | **String** | Value of the environment variable. Defaults to \&quot;\&quot;. Variable references are not supported in Cloud Run. |  [optional] |
|**valueFrom** | [**EnvVarSource**](EnvVarSource.md) |  |  [optional] |



