# OrganizationPolicyApi.GoogleCloudOrgpolicyV2Constraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booleanConstraint** | **Object** | A constraint that is either enforced or not. For example, a constraint &#x60;constraints/compute.disableSerialPortAccess&#x60;. If it is enforced on a VM instance, serial port connections will not be opened to that instance. | [optional] 
**constraintDefault** | **String** | The evaluation behavior of this constraint in the absence of a policy. | [optional] 
**description** | **String** | Detailed description of what this constraint controls as well as how and where it is enforced. Mutable. | [optional] 
**displayName** | **String** | The human readable name. Mutable. | [optional] 
**listConstraint** | [**GoogleCloudOrgpolicyV2ConstraintListConstraint**](GoogleCloudOrgpolicyV2ConstraintListConstraint.md) |  | [optional] 
**name** | **String** | Immutable. The resource name of the constraint. Must be in one of the following forms: * &#x60;projects/{project_number}/constraints/{constraint_name}&#x60; * &#x60;folders/{folder_id}/constraints/{constraint_name}&#x60; * &#x60;organizations/{organization_id}/constraints/{constraint_name}&#x60; For example, \&quot;/projects/123/constraints/compute.disableSerialPortAccess\&quot;. | [optional] 
**supportsDryRun** | **Boolean** | Shows if dry run is supported for this constraint or not. | [optional] 



## Enum: ConstraintDefaultEnum


* `CONSTRAINT_DEFAULT_UNSPECIFIED` (value: `"CONSTRAINT_DEFAULT_UNSPECIFIED"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)




