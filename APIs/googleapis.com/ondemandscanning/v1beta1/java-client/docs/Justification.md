

# Justification

Justification provides the justification when the state of the assessment if NOT_AFFECTED.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Additional details on why this justification was chosen. |  [optional] |
|**justificationType** | [**JustificationTypeEnum**](#JustificationTypeEnum) | The justification type for this vulnerability. |  [optional] |



## Enum: JustificationTypeEnum

| Name | Value |
|---- | -----|
| JUSTIFICATION_TYPE_UNSPECIFIED | &quot;JUSTIFICATION_TYPE_UNSPECIFIED&quot; |
| COMPONENT_NOT_PRESENT | &quot;COMPONENT_NOT_PRESENT&quot; |
| VULNERABLE_CODE_NOT_PRESENT | &quot;VULNERABLE_CODE_NOT_PRESENT&quot; |
| VULNERABLE_CODE_NOT_IN_EXECUTE_PATH | &quot;VULNERABLE_CODE_NOT_IN_EXECUTE_PATH&quot; |
| VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY | &quot;VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY&quot; |
| INLINE_MITIGATIONS_ALREADY_EXIST | &quot;INLINE_MITIGATIONS_ALREADY_EXIST&quot; |



