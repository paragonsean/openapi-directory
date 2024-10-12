

# RegistrationAssignmentProperties

Properties of a registration assignment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Current state of the registration assignment. |  [optional] [readonly] |
|**registrationDefinition** | [**RegistrationAssignmentPropertiesRegistrationDefinition**](RegistrationAssignmentPropertiesRegistrationDefinition.md) |  |  [optional] |
|**registrationDefinitionId** | **String** | Fully qualified path of the registration definition. |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| ACCEPTED | &quot;Accepted&quot; |
| RUNNING | &quot;Running&quot; |
| READY | &quot;Ready&quot; |
| CREATING | &quot;Creating&quot; |
| CREATED | &quot;Created&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |
| CANCELED | &quot;Canceled&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |



