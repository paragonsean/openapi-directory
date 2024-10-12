

# Compute

Machine Learning compute object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeLocation** | **String** | Location for the underlying compute |  [optional] |
|**computeType** | **ComputeType** |  |  |
|**createdOn** | **OffsetDateTime** | The date and time when the compute was created. |  [optional] [readonly] |
|**description** | **String** | The description of the Machine Learning compute. |  [optional] |
|**isAttachedCompute** | **Boolean** | Indicating whether the compute was provisioned by user and brought from outside if true, or machine learning service provisioned it if false. |  [optional] [readonly] |
|**modifiedOn** | **OffsetDateTime** | The date and time when the compute was last modified. |  [optional] [readonly] |
|**provisioningErrors** | [**List&lt;MachineLearningServiceError&gt;**](MachineLearningServiceError.md) | Errors during provisioning |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. |  [optional] [readonly] |
|**resourceId** | **String** | ARM resource id of the underlying compute |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UPDATING | &quot;Updating&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



