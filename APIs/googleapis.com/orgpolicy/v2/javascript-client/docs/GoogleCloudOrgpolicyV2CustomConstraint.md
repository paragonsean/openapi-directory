# OrganizationPolicyApi.GoogleCloudOrgpolicyV2CustomConstraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionType** | **String** | Allow or deny type. | [optional] 
**condition** | **String** | Org policy condition/expression. For example: &#x60;resource.instanceName.matches(\&quot;[production|test]_.*_(\\d)+\&quot;)&#x60; or, &#x60;resource.management.auto_upgrade &#x3D;&#x3D; true&#x60; The max length of the condition is 1000 characters. | [optional] 
**description** | **String** | Detailed information about this custom policy constraint. The max length of the description is 2000 characters. | [optional] 
**displayName** | **String** | One line display name for the UI. The max length of the display_name is 200 characters. | [optional] 
**methodTypes** | **[String]** | All the operations being applied for this constraint. | [optional] 
**name** | **String** | Immutable. Name of the constraint. This is unique within the organization. Format of the name should be * &#x60;organizations/{organization_id}/customConstraints/{custom_constraint_id}&#x60; Example: &#x60;organizations/123/customConstraints/custom.createOnlyE2TypeVms&#x60; The max length is 70 characters and the minimum length is 1. Note that the prefix &#x60;organizations/{organization_id}/customConstraints/&#x60; is not counted. | [optional] 
**resourceTypes** | **[String]** | Immutable. The resource instance type on which this policy applies. Format will be of the form : &#x60;/&#x60; Example: * &#x60;compute.googleapis.com/Instance&#x60;. | [optional] 
**updateTime** | **String** | Output only. The last time this custom constraint was updated. This represents the last time that the &#x60;CreateCustomConstraint&#x60; or &#x60;UpdateCustomConstraint&#x60; RPC was called | [optional] [readonly] 



## Enum: ActionTypeEnum


* `ACTION_TYPE_UNSPECIFIED` (value: `"ACTION_TYPE_UNSPECIFIED"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)





## Enum: [MethodTypesEnum]


* `METHOD_TYPE_UNSPECIFIED` (value: `"METHOD_TYPE_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)

* `DELETE` (value: `"DELETE"`)




