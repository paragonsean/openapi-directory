# CloudAssetApi.GoogleCloudAssetV1Constraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booleanConstraint** | **Object** | A &#x60;Constraint&#x60; that is either enforced or not. For example a constraint &#x60;constraints/compute.disableSerialPortAccess&#x60;. If it is enforced on a VM instance, serial port connections will not be opened to that instance. | [optional] 
**constraintDefault** | **String** | The evaluation behavior of this constraint in the absence of &#39;Policy&#39;. | [optional] 
**description** | **String** | Detailed description of what this &#x60;Constraint&#x60; controls as well as how and where it is enforced. | [optional] 
**displayName** | **String** | The human readable name of the constraint. | [optional] 
**listConstraint** | [**GoogleCloudAssetV1ListConstraint**](GoogleCloudAssetV1ListConstraint.md) |  | [optional] 
**name** | **String** | The unique name of the constraint. Format of the name should be * &#x60;constraints/{constraint_name}&#x60; For example, &#x60;constraints/compute.disableSerialPortAccess&#x60;. | [optional] 



## Enum: ConstraintDefaultEnum


* `CONSTRAINT_DEFAULT_UNSPECIFIED` (value: `"CONSTRAINT_DEFAULT_UNSPECIFIED"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)




