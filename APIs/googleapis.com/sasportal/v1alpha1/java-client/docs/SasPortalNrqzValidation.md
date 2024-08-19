

# SasPortalNrqzValidation

Information about National Radio Quiet Zone validation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseId** | **String** | Validation case ID. |  [optional] |
|**cpiId** | **String** | CPI who signed the validation. |  [optional] |
|**latitude** | **Double** | Device latitude that&#39;s associated with the validation. |  [optional] |
|**longitude** | **Double** | Device longitude that&#39;s associated with the validation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the NRQZ validation info. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| FINAL | &quot;FINAL&quot; |



