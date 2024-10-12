

# FixableTotalByDigest

Per resource and severity counts of fixable and total vulnerabilities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fixableCount** | **String** | The number of fixable vulnerabilities associated with this resource. |  [optional] |
|**resourceUri** | **String** | The affected resource. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity for this count. SEVERITY_UNSPECIFIED indicates total across all severities. |  [optional] |
|**totalCount** | **String** | The total number of vulnerabilities associated with this resource. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| MINIMAL | &quot;MINIMAL&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| CRITICAL | &quot;CRITICAL&quot; |



