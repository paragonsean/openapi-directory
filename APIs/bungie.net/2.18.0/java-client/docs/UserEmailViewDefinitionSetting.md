

# UserEmailViewDefinitionSetting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localization** | [**Map&lt;String, UserEMailSettingLocalization&gt;**](UserEMailSettingLocalization.md) | A dictionary of localized text for the EMail setting, keyed by the locale. |  [optional] |
|**name** | **String** | The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired. |  [optional] |
|**optInAggregateValue** | **Long** | The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting. |  [optional] |
|**setByDefault** | **Boolean** | If true, this setting should be set by default if the user hasn&#39;t chosen whether it&#39;s set or cleared yet. |  [optional] |
|**subscriptions** | [**List&lt;UserEmailSubscriptionDefinition&gt;**](UserEmailSubscriptionDefinition.md) | The subscriptions to show as children of this setting, if any. |  [optional] |



