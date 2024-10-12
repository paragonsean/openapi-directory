

# GooglePrivacyDlpV2InfoTypeDescription

InfoType description.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | [**List&lt;GooglePrivacyDlpV2InfoTypeCategory&gt;**](GooglePrivacyDlpV2InfoTypeCategory.md) | The category of the infoType. |  [optional] |
|**description** | **String** | Description of the infotype. Translated when language is provided in the request. |  [optional] |
|**displayName** | **String** | Human readable form of the infoType name. |  [optional] |
|**name** | **String** | Internal name of the infoType. |  [optional] |
|**sensitivityScore** | [**GooglePrivacyDlpV2SensitivityScore**](GooglePrivacyDlpV2SensitivityScore.md) |  |  [optional] |
|**supportedBy** | [**List&lt;SupportedByEnum&gt;**](#List&lt;SupportedByEnum&gt;) | Which parts of the API supports this InfoType. |  [optional] |
|**versions** | [**List&lt;GooglePrivacyDlpV2VersionDescription&gt;**](GooglePrivacyDlpV2VersionDescription.md) | A list of available versions for the infotype. |  [optional] |



## Enum: List&lt;SupportedByEnum&gt;

| Name | Value |
|---- | -----|
| ENUM_TYPE_UNSPECIFIED | &quot;ENUM_TYPE_UNSPECIFIED&quot; |
| INSPECT | &quot;INSPECT&quot; |
| RISK_ANALYSIS | &quot;RISK_ANALYSIS&quot; |



