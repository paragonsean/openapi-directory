

# Constraint

A `Constraint` describes a way in which a resource's configuration can be restricted. For example, it controls which cloud services can be activated across an organization, or whether a Compute Engine instance can have serial port connections established. `Constraints` can be configured by the organization's policy administrator to fit the needs of the organzation by setting Policies for `Constraints` at different locations in the organization's resource hierarchy. Policies are inherited down the resource hierarchy from higher levels, but can also be overridden. For details about the inheritance rules please read about [Policies](/resource-manager/reference/rest/v1/Policy). `Constraints` have a default behavior determined by the `constraint_default` field, which is the enforcement behavior that is used in the absence of a `Policy` being defined or inherited for the resource in question.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**booleanConstraint** | **Object** | A &#x60;Constraint&#x60; that is either enforced or not. For example a constraint &#x60;constraints/compute.disableSerialPortAccess&#x60;. If it is enforced on a VM instance, serial port connections will not be opened to that instance. |  [optional] |
|**constraintDefault** | [**ConstraintDefaultEnum**](#ConstraintDefaultEnum) | The evaluation behavior of this constraint in the absence of &#39;Policy&#39;. |  [optional] |
|**description** | **String** | Detailed description of what this &#x60;Constraint&#x60; controls as well as how and where it is enforced. Mutable. |  [optional] |
|**displayName** | **String** | The human readable name. Mutable. |  [optional] |
|**listConstraint** | [**ListConstraint**](ListConstraint.md) |  |  [optional] |
|**name** | **String** | Immutable value, required to globally be unique. For example, &#x60;constraints/serviceuser.services&#x60; |  [optional] |
|**version** | **Integer** | Version of the &#x60;Constraint&#x60;. Default version is 0; |  [optional] |



## Enum: ConstraintDefaultEnum

| Name | Value |
|---- | -----|
| CONSTRAINT_DEFAULT_UNSPECIFIED | &quot;CONSTRAINT_DEFAULT_UNSPECIFIED&quot; |
| ALLOW | &quot;ALLOW&quot; |
| DENY | &quot;DENY&quot; |



