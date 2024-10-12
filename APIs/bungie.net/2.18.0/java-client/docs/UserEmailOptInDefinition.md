

# UserEmailOptInDefinition

Defines a single opt-in category: a wide-scoped permission to send emails for the subject related to the opt-in.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependentSubscriptions** | [**List&lt;UserEmailSubscriptionDefinition&gt;**](UserEmailSubscriptionDefinition.md) | Information about the dependent subscriptions for this opt-in. |  [optional] |
|**name** | **String** | The unique identifier for this opt-in category. |  [optional] |
|**setByDefault** | **Boolean** | If true, this opt-in setting should be set by default in situations where accounts are created without explicit choices about what they&#39;re opting into. |  [optional] |
|**value** | **Long** | The flag value for this opt-in category. For historical reasons, this is defined as a flags enum. |  [optional] |



