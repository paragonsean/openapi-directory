

# Remediation

Specifies details on how to handle (and presumably, fix) a vulnerability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Contains a comprehensive human-readable discussion of the remediation. |  [optional] |
|**remediationType** | [**RemediationTypeEnum**](#RemediationTypeEnum) | The type of remediation that can be applied. |  [optional] |
|**remediationUri** | [**RelatedUrl**](RelatedUrl.md) |  |  [optional] |



## Enum: RemediationTypeEnum

| Name | Value |
|---- | -----|
| REMEDIATION_TYPE_UNSPECIFIED | &quot;REMEDIATION_TYPE_UNSPECIFIED&quot; |
| MITIGATION | &quot;MITIGATION&quot; |
| NO_FIX_PLANNED | &quot;NO_FIX_PLANNED&quot; |
| NONE_AVAILABLE | &quot;NONE_AVAILABLE&quot; |
| VENDOR_FIX | &quot;VENDOR_FIX&quot; |
| WORKAROUND | &quot;WORKAROUND&quot; |



