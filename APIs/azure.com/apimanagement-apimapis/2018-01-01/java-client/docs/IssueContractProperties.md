

# IssueContractProperties

Issue contract Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Text describing the issue. |  |
|**title** | **String** | The issue title. |  |
|**userId** | **String** | A resource identifier for the user created the issue. |  |
|**apiId** | **String** | A resource identifier for the API the issue was created for. |  [optional] |
|**createdDate** | **OffsetDateTime** | Date and time when the issue was created. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Status of the issue. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PROPOSED | &quot;proposed&quot; |
| OPEN | &quot;open&quot; |
| REMOVED | &quot;removed&quot; |
| RESOLVED | &quot;resolved&quot; |
| CLOSED | &quot;closed&quot; |



