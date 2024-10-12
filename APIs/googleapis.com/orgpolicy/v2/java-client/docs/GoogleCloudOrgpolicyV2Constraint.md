

# GoogleCloudOrgpolicyV2Constraint

A constraint describes a way to restrict resource's configuration. For example, you could enforce a constraint that controls which Google Cloud services can be activated across an organization, or whether a Compute Engine instance can have serial port connections established. Constraints can be configured by the organization policy administrator to fit the needs of the organization by setting a policy that includes constraints at different locations in the organization's resource hierarchy. Policies are inherited down the resource hierarchy from higher levels, but can also be overridden. For details about the inheritance rules please read about `policies`. Constraints have a default behavior determined by the `constraint_default` field, which is the enforcement behavior that is used in the absence of a policy being defined or inherited for the resource in question.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**booleanConstraint** | **Object** | A constraint that is either enforced or not. For example, a constraint &#x60;constraints/compute.disableSerialPortAccess&#x60;. If it is enforced on a VM instance, serial port connections will not be opened to that instance. |  [optional] |
|**constraintDefault** | [**ConstraintDefaultEnum**](#ConstraintDefaultEnum) | The evaluation behavior of this constraint in the absence of a policy. |  [optional] |
|**description** | **String** | Detailed description of what this constraint controls as well as how and where it is enforced. Mutable. |  [optional] |
|**displayName** | **String** | The human readable name. Mutable. |  [optional] |
|**listConstraint** | [**GoogleCloudOrgpolicyV2ConstraintListConstraint**](GoogleCloudOrgpolicyV2ConstraintListConstraint.md) |  |  [optional] |
|**name** | **String** | Immutable. The resource name of the constraint. Must be in one of the following forms: * &#x60;projects/{project_number}/constraints/{constraint_name}&#x60; * &#x60;folders/{folder_id}/constraints/{constraint_name}&#x60; * &#x60;organizations/{organization_id}/constraints/{constraint_name}&#x60; For example, \&quot;/projects/123/constraints/compute.disableSerialPortAccess\&quot;. |  [optional] |
|**supportsDryRun** | **Boolean** | Shows if dry run is supported for this constraint or not. |  [optional] |



## Enum: ConstraintDefaultEnum

| Name | Value |
|---- | -----|
| CONSTRAINT_DEFAULT_UNSPECIFIED | &quot;CONSTRAINT_DEFAULT_UNSPECIFIED&quot; |
| ALLOW | &quot;ALLOW&quot; |
| DENY | &quot;DENY&quot; |



