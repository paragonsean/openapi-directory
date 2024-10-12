

# RevisionCheckResponse

A third party checking a revision response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The version of the API this client revision should use when calling API methods. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#revisionCheckResponse&#x60;. |  [optional] |
|**revisionStatus** | [**RevisionStatusEnum**](#RevisionStatusEnum) | The result of the revision check. |  [optional] |



## Enum: RevisionStatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| INVALID | &quot;INVALID&quot; |



