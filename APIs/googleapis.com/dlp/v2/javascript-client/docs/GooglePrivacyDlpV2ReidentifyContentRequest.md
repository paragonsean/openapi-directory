# SensitiveDataProtectionDlp.GooglePrivacyDlpV2ReidentifyContentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inspectConfig** | [**GooglePrivacyDlpV2InspectConfig**](GooglePrivacyDlpV2InspectConfig.md) |  | [optional] 
**inspectTemplateName** | **String** | Template to use. Any configuration directly specified in &#x60;inspect_config&#x60; will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged. | [optional] 
**item** | [**GooglePrivacyDlpV2ContentItem**](GooglePrivacyDlpV2ContentItem.md) |  | [optional] 
**locationId** | **String** | Deprecated. This field has no effect. | [optional] 
**reidentifyConfig** | [**GooglePrivacyDlpV2DeidentifyConfig**](GooglePrivacyDlpV2DeidentifyConfig.md) |  | [optional] 
**reidentifyTemplateName** | **String** | Template to use. References an instance of &#x60;DeidentifyTemplate&#x60;. Any configuration directly specified in &#x60;reidentify_config&#x60; or &#x60;inspect_config&#x60; will override those set in the template. The &#x60;DeidentifyTemplate&#x60; used must include only reversible transformations. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged. | [optional] 


