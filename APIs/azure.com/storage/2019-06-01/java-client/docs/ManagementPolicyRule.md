

# ManagementPolicyRule

An object that wraps the Lifecycle rule. Each rule is uniquely defined by name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**definition** | [**ManagementPolicyDefinition**](ManagementPolicyDefinition.md) |  |  |
|**enabled** | **Boolean** | Rule is enabled if set to true. |  [optional] |
|**name** | **String** | A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The valid value is Lifecycle |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LIFECYCLE | &quot;Lifecycle&quot; |



