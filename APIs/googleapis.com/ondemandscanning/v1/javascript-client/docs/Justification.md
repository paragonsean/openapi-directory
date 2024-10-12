# OnDemandScanningApi.Justification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **String** | Additional details on why this justification was chosen. | [optional] 
**justificationType** | **String** | The justification type for this vulnerability. | [optional] 



## Enum: JustificationTypeEnum


* `JUSTIFICATION_TYPE_UNSPECIFIED` (value: `"JUSTIFICATION_TYPE_UNSPECIFIED"`)

* `COMPONENT_NOT_PRESENT` (value: `"COMPONENT_NOT_PRESENT"`)

* `VULNERABLE_CODE_NOT_PRESENT` (value: `"VULNERABLE_CODE_NOT_PRESENT"`)

* `VULNERABLE_CODE_NOT_IN_EXECUTE_PATH` (value: `"VULNERABLE_CODE_NOT_IN_EXECUTE_PATH"`)

* `VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY` (value: `"VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY"`)

* `INLINE_MITIGATIONS_ALREADY_EXIST` (value: `"INLINE_MITIGATIONS_ALREADY_EXIST"`)




