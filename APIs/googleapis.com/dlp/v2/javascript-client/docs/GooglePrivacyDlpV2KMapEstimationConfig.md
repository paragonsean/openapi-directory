# SensitiveDataProtectionDlp.GooglePrivacyDlpV2KMapEstimationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auxiliaryTables** | [**[GooglePrivacyDlpV2AuxiliaryTable]**](GooglePrivacyDlpV2AuxiliaryTable.md) | Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers column must appear in exactly one column of one auxiliary table. | [optional] 
**quasiIds** | [**[GooglePrivacyDlpV2TaggedField]**](GooglePrivacyDlpV2TaggedField.md) | Required. Fields considered to be quasi-identifiers. No two columns can have the same tag. | [optional] 
**regionCode** | **String** | ISO 3166-1 alpha-2 region code to use in the statistical modeling. Set if no column is tagged with a region-specific InfoType (like US_ZIP_5) or a region code. | [optional] 


