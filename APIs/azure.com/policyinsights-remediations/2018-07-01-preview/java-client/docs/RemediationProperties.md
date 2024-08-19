

# RemediationProperties

The remediation properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdOn** | **OffsetDateTime** | The time at which the remediation was created. |  [optional] [readonly] |
|**deploymentStatus** | [**RemediationDeploymentSummary**](RemediationDeploymentSummary.md) |  |  [optional] |
|**filters** | [**RemediationFilters**](RemediationFilters.md) |  |  [optional] |
|**lastUpdatedOn** | **OffsetDateTime** | The time at which the remediation was last updated. |  [optional] [readonly] |
|**policyAssignmentId** | **String** | The resource ID of the policy assignment that should be remediated. |  [optional] |
|**policyDefinitionReferenceId** | **String** | The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition. |  [optional] |
|**provisioningState** | **String** | The status of the remediation. |  [optional] [readonly] |



