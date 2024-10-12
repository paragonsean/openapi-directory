

# GoogleCloudDialogflowCxV3beta1SecuritySettings

Represents the settings related to security issues, such as data redaction and data retention. It may take hours for updates on the settings to propagate to all the related components and take effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioExportSettings** | [**GoogleCloudDialogflowCxV3beta1SecuritySettingsAudioExportSettings**](GoogleCloudDialogflowCxV3beta1SecuritySettingsAudioExportSettings.md) |  |  [optional] |
|**deidentifyTemplate** | **String** | [DLP](https://cloud.google.com/dlp/docs) deidentify template name. Use this template to define de-identification configuration for the content. The &#x60;DLP De-identify Templates Reader&#x60; role is needed on the Dialogflow service identity service account (has the form &#x60;service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com&#x60;) for your agent&#39;s project. If empty, Dialogflow replaces sensitive info with &#x60;[redacted]&#x60; text. The template name will have one of the following formats: &#x60;projects//locations//deidentifyTemplates/&#x60; OR &#x60;organizations//locations//deidentifyTemplates/&#x60; Note: &#x60;deidentify_template&#x60; must be located in the same region as the &#x60;SecuritySettings&#x60;. |  [optional] |
|**displayName** | **String** | Required. The human-readable name of the security settings, unique within the location. |  [optional] |
|**insightsExportSettings** | [**GoogleCloudDialogflowCxV3beta1SecuritySettingsInsightsExportSettings**](GoogleCloudDialogflowCxV3beta1SecuritySettingsInsightsExportSettings.md) |  |  [optional] |
|**inspectTemplate** | **String** | [DLP](https://cloud.google.com/dlp/docs) inspect template name. Use this template to define inspect base settings. The &#x60;DLP Inspect Templates Reader&#x60; role is needed on the Dialogflow service identity service account (has the form &#x60;service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com&#x60;) for your agent&#39;s project. If empty, we use the default DLP inspect config. The template name will have one of the following formats: &#x60;projects//locations//inspectTemplates/&#x60; OR &#x60;organizations//locations//inspectTemplates/&#x60; Note: &#x60;inspect_template&#x60; must be located in the same region as the &#x60;SecuritySettings&#x60;. |  [optional] |
|**name** | **String** | Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: &#x60;projects//locations//securitySettings/&#x60;. |  [optional] |
|**purgeDataTypes** | [**List&lt;PurgeDataTypesEnum&gt;**](#List&lt;PurgeDataTypesEnum&gt;) | List of types of data to remove when retention settings triggers purge. |  [optional] |
|**redactionScope** | [**RedactionScopeEnum**](#RedactionScopeEnum) | Defines the data for which Dialogflow applies redaction. Dialogflow does not redact data that it does not have access to – for example, Cloud logging. |  [optional] |
|**redactionStrategy** | [**RedactionStrategyEnum**](#RedactionStrategyEnum) | Strategy that defines how we do redaction. |  [optional] |
|**retentionStrategy** | [**RetentionStrategyEnum**](#RetentionStrategyEnum) | Specifies the retention behavior defined by SecuritySettings.RetentionStrategy. |  [optional] |
|**retentionWindowDays** | **Integer** | Retains data in interaction logging for the specified number of days. This does not apply to Cloud logging, which is owned by the user - not Dialogflow. User must set a value lower than Dialogflow&#39;s default 365d TTL (30 days for Agent Assist traffic), higher value will be ignored and use default. Setting a value higher than that has no effect. A missing value or setting to 0 also means we use default TTL. |  [optional] |



## Enum: List&lt;PurgeDataTypesEnum&gt;

| Name | Value |
|---- | -----|
| PURGE_DATA_TYPE_UNSPECIFIED | &quot;PURGE_DATA_TYPE_UNSPECIFIED&quot; |
| DIALOGFLOW_HISTORY | &quot;DIALOGFLOW_HISTORY&quot; |



## Enum: RedactionScopeEnum

| Name | Value |
|---- | -----|
| REDACTION_SCOPE_UNSPECIFIED | &quot;REDACTION_SCOPE_UNSPECIFIED&quot; |
| REDACT_DISK_STORAGE | &quot;REDACT_DISK_STORAGE&quot; |



## Enum: RedactionStrategyEnum

| Name | Value |
|---- | -----|
| REDACTION_STRATEGY_UNSPECIFIED | &quot;REDACTION_STRATEGY_UNSPECIFIED&quot; |
| REDACT_WITH_SERVICE | &quot;REDACT_WITH_SERVICE&quot; |



## Enum: RetentionStrategyEnum

| Name | Value |
|---- | -----|
| RETENTION_STRATEGY_UNSPECIFIED | &quot;RETENTION_STRATEGY_UNSPECIFIED&quot; |
| REMOVE_AFTER_CONVERSATION | &quot;REMOVE_AFTER_CONVERSATION&quot; |



