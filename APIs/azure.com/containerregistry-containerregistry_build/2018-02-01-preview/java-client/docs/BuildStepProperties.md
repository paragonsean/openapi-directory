

# BuildStepProperties

Base properties for any build step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the build step. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the step. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DOCKER | &quot;Docker&quot; |



