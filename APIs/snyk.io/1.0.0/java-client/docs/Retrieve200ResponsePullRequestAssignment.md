

# Retrieve200ResponsePullRequestAssignment

assign Snyk pull requests

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignees** | **List&lt;Object&gt;** | an array of usernames that have contributed to the organization&#39;s project(s). |  [optional] |
|**enabled** | **Boolean** | if the organization&#39;s project(s) will assign Snyk pull requests. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | a string representing the type of assignment your projects require. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| MANUAL | &quot;manual&quot; |



