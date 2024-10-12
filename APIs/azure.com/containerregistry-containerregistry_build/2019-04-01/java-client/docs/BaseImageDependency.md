

# BaseImageDependency

Properties that describe a base image dependency.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digest** | **String** | The sha256-based digest of the image manifest. |  [optional] |
|**registry** | **String** | The registry login server. |  [optional] |
|**repository** | **String** | The repository name. |  [optional] |
|**tag** | **String** | The tag name. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the base image dependency. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BUILD_TIME | &quot;BuildTime&quot; |
| RUN_TIME | &quot;RunTime&quot; |



