# CloudMonitoringApi.NotificationChannelDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A human-readable description of the notification channel type. The description may include a description of the properties of the channel and pointers to external documentation. | [optional] 
**displayName** | **String** | A human-readable name for the notification channel type. This form of the name is suitable for a user interface. | [optional] 
**labels** | [**[LabelDescriptor]**](LabelDescriptor.md) | The set of labels that must be defined to identify a particular channel of the corresponding type. Each label includes a description for how that field should be populated. | [optional] 
**launchStage** | **String** | The product launch stage for channels of this type. | [optional] 
**name** | **String** | The full REST resource name for this descriptor. The format is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[TYPE] In the above, [TYPE] is the value of the type field. | [optional] 
**supportedTiers** | **[String]** | The tiers that support this notification channel; the project service tier must be one of the supported_tiers. | [optional] 
**type** | **String** | The type of notification channel, such as \&quot;email\&quot; and \&quot;sms\&quot;. To view the full list of channels, see Channel descriptors (https://cloud.google.com/monitoring/alerts/using-channels-api#ncd). Notification channel types are globally unique. | [optional] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)





## Enum: [SupportedTiersEnum]


* `UNSPECIFIED` (value: `"SERVICE_TIER_UNSPECIFIED"`)

* `BASIC` (value: `"SERVICE_TIER_BASIC"`)

* `PREMIUM` (value: `"SERVICE_TIER_PREMIUM"`)




