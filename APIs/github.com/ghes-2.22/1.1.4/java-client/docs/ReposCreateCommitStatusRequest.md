

# ReposCreateCommitStatusRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | **String** | A string label to differentiate this status from the status of other systems. This field is case-insensitive. |  [optional] |
|**description** | **String** | A short description of the status. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the status. Can be one of &#x60;error&#x60;, &#x60;failure&#x60;, &#x60;pending&#x60;, or &#x60;success&#x60;. |  |
|**targetUrl** | **String** | The target URL to associate with this status. This URL will be linked from the GitHub UI to allow users to easily see the source of the status.   For example, if your continuous integration system is posting build status, you would want to provide the deep link for the build output for this specific SHA:   &#x60;http://ci.example.com/user/repo/build/sha&#x60; |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;error&quot; |
| FAILURE | &quot;failure&quot; |
| PENDING | &quot;pending&quot; |
| SUCCESS | &quot;success&quot; |



