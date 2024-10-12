

# NotificationChannelDescriptor

A description of a notification channel. The descriptor includes the properties of the channel and the set of labels or fields that must be specified to configure channels of a given type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A human-readable description of the notification channel type. The description may include a description of the properties of the channel and pointers to external documentation. |  [optional] |
|**displayName** | **String** | A human-readable name for the notification channel type. This form of the name is suitable for a user interface. |  [optional] |
|**labels** | [**List&lt;LabelDescriptor&gt;**](LabelDescriptor.md) | The set of labels that must be defined to identify a particular channel of the corresponding type. Each label includes a description for how that field should be populated. |  [optional] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | The product launch stage for channels of this type. |  [optional] |
|**name** | **String** | The full REST resource name for this descriptor. The format is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[TYPE] In the above, [TYPE] is the value of the type field. |  [optional] |
|**supportedTiers** | [**List&lt;SupportedTiersEnum&gt;**](#List&lt;SupportedTiersEnum&gt;) | The tiers that support this notification channel; the project service tier must be one of the supported_tiers. |  [optional] |
|**type** | **String** | The type of notification channel, such as \&quot;email\&quot; and \&quot;sms\&quot;. To view the full list of channels, see Channel descriptors (https://cloud.google.com/monitoring/alerts/using-channels-api#ncd). Notification channel types are globally unique. |  [optional] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| PRELAUNCH | &quot;PRELAUNCH&quot; |
| EARLY_ACCESS | &quot;EARLY_ACCESS&quot; |
| ALPHA | &quot;ALPHA&quot; |
| BETA | &quot;BETA&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



## Enum: List&lt;SupportedTiersEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SERVICE_TIER_UNSPECIFIED&quot; |
| BASIC | &quot;SERVICE_TIER_BASIC&quot; |
| PREMIUM | &quot;SERVICE_TIER_PREMIUM&quot; |



