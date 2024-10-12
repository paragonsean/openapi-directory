

# IssueContractBaseProperties

Issue contract Base Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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



