# ResourceSettingsApi.GoogleCloudResourcesettingsV1Setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effectiveValue** | [**GoogleCloudResourcesettingsV1Value**](GoogleCloudResourcesettingsV1Value.md) |  | [optional] 
**etag** | **String** | A fingerprint used for optimistic concurrency. See UpdateSetting for more details. | [optional] 
**localValue** | [**GoogleCloudResourcesettingsV1Value**](GoogleCloudResourcesettingsV1Value.md) |  | [optional] 
**metadata** | [**GoogleCloudResourcesettingsV1SettingMetadata**](GoogleCloudResourcesettingsV1SettingMetadata.md) |  | [optional] 
**name** | **String** | The resource name of the setting. Must be in one of the following forms: * &#x60;projects/{project_number}/settings/{setting_name}&#x60; * &#x60;folders/{folder_id}/settings/{setting_name}&#x60; * &#x60;organizations/{organization_id}/settings/{setting_name}&#x60; For example, \&quot;/projects/123/settings/gcp-enableMyFeature\&quot; | [optional] 


