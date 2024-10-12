# CloudResourceManagerApi.Constraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booleanConstraint** | **Object** | A &#x60;Constraint&#x60; that is either enforced or not. For example a constraint &#x60;constraints/compute.disableSerialPortAccess&#x60;. If it is enforced on a VM instance, serial port connections will not be opened to that instance. | [optional] 
**constraintDefault** | **String** | The evaluation behavior of this constraint in the absence of &#39;Policy&#39;. | [optional] 
**description** | **String** | Detailed description of what this &#x60;Constraint&#x60; controls as well as how and where it is enforced. Mutable. | [optional] 
**displayName** | **String** | The human readable name. Mutable. | [optional] 
**listConstraint** | [**ListConstraint**](ListConstraint.md) |  | [optional] 
**name** | **String** | Immutable value, required to globally be unique. For example, &#x60;constraints/serviceuser.services&#x60; | [optional] 
**version** | **Number** | Version of the &#x60;Constraint&#x60;. Default version is 0; | [optional] 



## Enum: ConstraintDefaultEnum


* `CONSTRAINT_DEFAULT_UNSPECIFIED` (value: `"CONSTRAINT_DEFAULT_UNSPECIFIED"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)




