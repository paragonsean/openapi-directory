

# GooglePrivacyDlpV2InspectJobConfig

Controls what and how to inspect for findings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;GooglePrivacyDlpV2Action&gt;**](GooglePrivacyDlpV2Action.md) | Actions to execute at the completion of the job. |  [optional] |
|**inspectConfig** | [**GooglePrivacyDlpV2InspectConfig**](GooglePrivacyDlpV2InspectConfig.md) |  |  [optional] |
|**inspectTemplateName** | **String** | If provided, will be used as the default for all values in InspectConfig. &#x60;inspect_config&#x60; will be merged into the values persisted as part of the template. |  [optional] |
|**storageConfig** | [**GooglePrivacyDlpV2StorageConfig**](GooglePrivacyDlpV2StorageConfig.md) |  |  [optional] |



