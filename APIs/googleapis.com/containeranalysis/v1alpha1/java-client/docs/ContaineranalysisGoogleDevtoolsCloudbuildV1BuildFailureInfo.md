

# ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfo

A fatal problem encountered during the execution of the build.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | Explains the failure issue in more detail using hard-coded text. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The name of the failure. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FAILURE_TYPE_UNSPECIFIED | &quot;FAILURE_TYPE_UNSPECIFIED&quot; |
| PUSH_FAILED | &quot;PUSH_FAILED&quot; |
| PUSH_IMAGE_NOT_FOUND | &quot;PUSH_IMAGE_NOT_FOUND&quot; |
| PUSH_NOT_AUTHORIZED | &quot;PUSH_NOT_AUTHORIZED&quot; |
| LOGGING_FAILURE | &quot;LOGGING_FAILURE&quot; |
| USER_BUILD_STEP | &quot;USER_BUILD_STEP&quot; |
| FETCH_SOURCE_FAILED | &quot;FETCH_SOURCE_FAILED&quot; |



