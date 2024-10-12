# CloudAssetApi.GoogleCloudAssetV1CustomConstraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionType** | **String** | Allow or deny type. | [optional] 
**condition** | **String** | Organization Policy condition/expression. For example: &#x60;resource.instanceName.matches(\&quot;[production|test]_.*_(\\d)+\&quot;)&#39;&#x60; or, &#x60;resource.management.auto_upgrade &#x3D;&#x3D; true&#x60; | [optional] 
**description** | **String** | Detailed information about this custom policy constraint. | [optional] 
**displayName** | **String** | One line display name for the UI. | [optional] 
**methodTypes** | **[String]** | All the operations being applied for this constraint. | [optional] 
**name** | **String** | Name of the constraint. This is unique within the organization. Format of the name should be * &#x60;organizations/{organization_id}/customConstraints/{custom_constraint_id}&#x60; Example : \&quot;organizations/123/customConstraints/custom.createOnlyE2TypeVms\&quot; | [optional] 
**resourceTypes** | **[String]** | The Resource Instance type on which this policy applies to. Format will be of the form : \&quot;/\&quot; Example: * &#x60;compute.googleapis.com/Instance&#x60;. | [optional] 



## Enum: ActionTypeEnum


* `ACTION_TYPE_UNSPECIFIED` (value: `"ACTION_TYPE_UNSPECIFIED"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)





## Enum: [MethodTypesEnum]


* `METHOD_TYPE_UNSPECIFIED` (value: `"METHOD_TYPE_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)

* `DELETE` (value: `"DELETE"`)




