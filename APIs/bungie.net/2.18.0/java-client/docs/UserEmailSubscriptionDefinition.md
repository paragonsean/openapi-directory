

# UserEmailSubscriptionDefinition

Defines a single subscription: permission to send emails for a specific, focused subject (generally timeboxed, such as for a specific release of a product or feature).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localization** | [**Map&lt;String, UserEMailSettingSubscriptionLocalization&gt;**](UserEMailSettingSubscriptionLocalization.md) | A dictionary of localized text for the EMail Opt-in setting, keyed by the locale. |  [optional] |
|**name** | **String** | The unique identifier for this subscription. |  [optional] |
|**value** | **Long** | The bitflag value for this subscription. Should be a unique power of two value. |  [optional] |



