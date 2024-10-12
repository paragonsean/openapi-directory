# DialogflowApi.GoogleCloudDialogflowCxV3SecuritySettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioExportSettings** | [**GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettings**](GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettings.md) |  | [optional] 
**deidentifyTemplate** | **String** | [DLP](https://cloud.google.com/dlp/docs) deidentify template name. Use this template to define de-identification configuration for the content. The &#x60;DLP De-identify Templates Reader&#x60; role is needed on the Dialogflow service identity service account (has the form &#x60;service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com&#x60;) for your agent&#39;s project. If empty, Dialogflow replaces sensitive info with &#x60;[redacted]&#x60; text. The template name will have one of the following formats: &#x60;projects//locations//deidentifyTemplates/&#x60; OR &#x60;organizations//locations//deidentifyTemplates/&#x60; Note: &#x60;deidentify_template&#x60; must be located in the same region as the &#x60;SecuritySettings&#x60;. | [optional] 
**displayName** | **String** | Required. The human-readable name of the security settings, unique within the location. | [optional] 
**insightsExportSettings** | [**GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettings**](GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettings.md) |  | [optional] 
**inspectTemplate** | **String** | [DLP](https://cloud.google.com/dlp/docs) inspect template name. Use this template to define inspect base settings. The &#x60;DLP Inspect Templates Reader&#x60; role is needed on the Dialogflow service identity service account (has the form &#x60;service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com&#x60;) for your agent&#39;s project. If empty, we use the default DLP inspect config. The template name will have one of the following formats: &#x60;projects//locations//inspectTemplates/&#x60; OR &#x60;organizations//locations//inspectTemplates/&#x60; Note: &#x60;inspect_template&#x60; must be located in the same region as the &#x60;SecuritySettings&#x60;. | [optional] 
**name** | **String** | Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: &#x60;projects//locations//securitySettings/&#x60;. | [optional] 
**purgeDataTypes** | **[String]** | List of types of data to remove when retention settings triggers purge. | [optional] 
**redactionScope** | **String** | Defines the data for which Dialogflow applies redaction. Dialogflow does not redact data that it does not have access to – for example, Cloud logging. | [optional] 
**redactionStrategy** | **String** | Strategy that defines how we do redaction. | [optional] 
**retentionStrategy** | **String** | Specifies the retention behavior defined by SecuritySettings.RetentionStrategy. | [optional] 
**retentionWindowDays** | **Number** | Retains the data for the specified number of days. User must set a value lower than Dialogflow&#39;s default 365d TTL (30 days for Agent Assist traffic), higher value will be ignored and use default. Setting a value higher than that has no effect. A missing value or setting to 0 also means we use default TTL. | [optional] 



## Enum: [PurgeDataTypesEnum]


* `PURGE_DATA_TYPE_UNSPECIFIED` (value: `"PURGE_DATA_TYPE_UNSPECIFIED"`)

* `DIALOGFLOW_HISTORY` (value: `"DIALOGFLOW_HISTORY"`)





## Enum: RedactionScopeEnum


* `REDACTION_SCOPE_UNSPECIFIED` (value: `"REDACTION_SCOPE_UNSPECIFIED"`)

* `REDACT_DISK_STORAGE` (value: `"REDACT_DISK_STORAGE"`)





## Enum: RedactionStrategyEnum


* `REDACTION_STRATEGY_UNSPECIFIED` (value: `"REDACTION_STRATEGY_UNSPECIFIED"`)

* `REDACT_WITH_SERVICE` (value: `"REDACT_WITH_SERVICE"`)





## Enum: RetentionStrategyEnum


* `RETENTION_STRATEGY_UNSPECIFIED` (value: `"RETENTION_STRATEGY_UNSPECIFIED"`)

* `REMOVE_AFTER_CONVERSATION` (value: `"REMOVE_AFTER_CONVERSATION"`)




