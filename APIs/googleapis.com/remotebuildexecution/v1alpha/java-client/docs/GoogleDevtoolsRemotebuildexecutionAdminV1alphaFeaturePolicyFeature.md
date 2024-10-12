

# GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature

Defines whether a feature can be used or what values are accepted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedValues** | **List&lt;String&gt;** | A list of acceptable values. Only effective when the policy is &#x60;RESTRICTED&#x60;. |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) | The policy of the feature. |  [optional] |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| POLICY_UNSPECIFIED | &quot;POLICY_UNSPECIFIED&quot; |
| ALLOWED | &quot;ALLOWED&quot; |
| FORBIDDEN | &quot;FORBIDDEN&quot; |
| RESTRICTED | &quot;RESTRICTED&quot; |



