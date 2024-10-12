

# ReauthSettings

Configuration for IAP reauthentication policies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxAge** | **String** | Reauth session lifetime, how long before a user has to reauthenticate again. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | Reauth method requested. |  [optional] |
|**policyType** | [**PolicyTypeEnum**](#PolicyTypeEnum) | How IAP determines the effective policy in cases of hierarchical policies. Policies are merged from higher in the hierarchy to lower in the hierarchy. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| METHOD_UNSPECIFIED | &quot;METHOD_UNSPECIFIED&quot; |
| LOGIN | &quot;LOGIN&quot; |
| PASSWORD | &quot;PASSWORD&quot; |
| SECURE_KEY | &quot;SECURE_KEY&quot; |
| ENROLLED_SECOND_FACTORS | &quot;ENROLLED_SECOND_FACTORS&quot; |



## Enum: PolicyTypeEnum

| Name | Value |
|---- | -----|
| POLICY_TYPE_UNSPECIFIED | &quot;POLICY_TYPE_UNSPECIFIED&quot; |
| MINIMUM | &quot;MINIMUM&quot; |
| DEFAULT | &quot;DEFAULT&quot; |



