

# GoogleCloudAssetV1CustomConstraint

The definition of a custom constraint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | Allow or deny type. |  [optional] |
|**condition** | **String** | Organization Policy condition/expression. For example: &#x60;resource.instanceName.matches(\&quot;[production|test]_.*_(\\d)+\&quot;)&#39;&#x60; or, &#x60;resource.management.auto_upgrade &#x3D;&#x3D; true&#x60; |  [optional] |
|**description** | **String** | Detailed information about this custom policy constraint. |  [optional] |
|**displayName** | **String** | One line display name for the UI. |  [optional] |
|**methodTypes** | [**List&lt;MethodTypesEnum&gt;**](#List&lt;MethodTypesEnum&gt;) | All the operations being applied for this constraint. |  [optional] |
|**name** | **String** | Name of the constraint. This is unique within the organization. Format of the name should be * &#x60;organizations/{organization_id}/customConstraints/{custom_constraint_id}&#x60; Example : \&quot;organizations/123/customConstraints/custom.createOnlyE2TypeVms\&quot; |  [optional] |
|**resourceTypes** | **List&lt;String&gt;** | The Resource Instance type on which this policy applies to. Format will be of the form : \&quot;/\&quot; Example: * &#x60;compute.googleapis.com/Instance&#x60;. |  [optional] |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| ACTION_TYPE_UNSPECIFIED | &quot;ACTION_TYPE_UNSPECIFIED&quot; |
| ALLOW | &quot;ALLOW&quot; |
| DENY | &quot;DENY&quot; |



## Enum: List&lt;MethodTypesEnum&gt;

| Name | Value |
|---- | -----|
| METHOD_TYPE_UNSPECIFIED | &quot;METHOD_TYPE_UNSPECIFIED&quot; |
| CREATE | &quot;CREATE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| DELETE | &quot;DELETE&quot; |



