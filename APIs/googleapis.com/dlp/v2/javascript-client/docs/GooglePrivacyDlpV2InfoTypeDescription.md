# SensitiveDataProtectionDlp.GooglePrivacyDlpV2InfoTypeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**[GooglePrivacyDlpV2InfoTypeCategory]**](GooglePrivacyDlpV2InfoTypeCategory.md) | The category of the infoType. | [optional] 
**description** | **String** | Description of the infotype. Translated when language is provided in the request. | [optional] 
**displayName** | **String** | Human readable form of the infoType name. | [optional] 
**name** | **String** | Internal name of the infoType. | [optional] 
**sensitivityScore** | [**GooglePrivacyDlpV2SensitivityScore**](GooglePrivacyDlpV2SensitivityScore.md) |  | [optional] 
**supportedBy** | **[String]** | Which parts of the API supports this InfoType. | [optional] 
**versions** | [**[GooglePrivacyDlpV2VersionDescription]**](GooglePrivacyDlpV2VersionDescription.md) | A list of available versions for the infotype. | [optional] 



## Enum: [SupportedByEnum]


* `ENUM_TYPE_UNSPECIFIED` (value: `"ENUM_TYPE_UNSPECIFIED"`)

* `INSPECT` (value: `"INSPECT"`)

* `RISK_ANALYSIS` (value: `"RISK_ANALYSIS"`)




