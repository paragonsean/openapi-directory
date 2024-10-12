# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DeidentifyContentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deidentifyConfig** | [**GooglePrivacyDlpV2DeidentifyConfig**](GooglePrivacyDlpV2DeidentifyConfig.md) |  | [optional] 
**deidentifyTemplateName** | **String** | Template to use. Any configuration directly specified in deidentify_config will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged. | [optional] 
**inspectConfig** | [**GooglePrivacyDlpV2InspectConfig**](GooglePrivacyDlpV2InspectConfig.md) |  | [optional] 
**inspectTemplateName** | **String** | Template to use. Any configuration directly specified in inspect_config will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged. | [optional] 
**item** | [**GooglePrivacyDlpV2ContentItem**](GooglePrivacyDlpV2ContentItem.md) |  | [optional] 
**locationId** | **String** | Deprecated. This field has no effect. | [optional] 


