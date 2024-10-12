

# GoogleCloudDialogflowCxV3AdvancedSettings

Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged. DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel. Hierarchy: Agent->Flow->Page->Fulfillment/Parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioExportGcsDestination** | [**GoogleCloudDialogflowCxV3GcsDestination**](GoogleCloudDialogflowCxV3GcsDestination.md) |  |  [optional] |
|**dtmfSettings** | [**GoogleCloudDialogflowCxV3AdvancedSettingsDtmfSettings**](GoogleCloudDialogflowCxV3AdvancedSettingsDtmfSettings.md) |  |  [optional] |
|**loggingSettings** | [**GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettings**](GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettings.md) |  |  [optional] |



