

# UpdateWorkspaceQuotas

The properties for update Quota response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Specifies the resource ID. |  [optional] [readonly] |
|**limit** | **Long** | The maximum permitted quota of the resource. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of update workspace quota. |  [optional] |
|**type** | **String** | Specifies the resource type. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | An enum describing the unit of quota measurement. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| SUCCESS | &quot;Success&quot; |
| FAILURE | &quot;Failure&quot; |
| INVALID_QUOTA_BELOW_CLUSTER_MINIMUM | &quot;InvalidQuotaBelowClusterMinimum&quot; |
| INVALID_QUOTA_EXCEEDS_SUBSCRIPTION_LIMIT | &quot;InvalidQuotaExceedsSubscriptionLimit&quot; |
| INVALID_VM_FAMILY_NAME | &quot;InvalidVMFamilyName&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |



