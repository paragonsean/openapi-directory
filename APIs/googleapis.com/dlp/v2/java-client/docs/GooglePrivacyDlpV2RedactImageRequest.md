

# GooglePrivacyDlpV2RedactImageRequest

Request to search for potentially sensitive info in an image and redact it by covering it with a colored rectangle.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**byteItem** | [**GooglePrivacyDlpV2ByteContentItem**](GooglePrivacyDlpV2ByteContentItem.md) |  |  [optional] |
|**imageRedactionConfigs** | [**List&lt;GooglePrivacyDlpV2ImageRedactionConfig&gt;**](GooglePrivacyDlpV2ImageRedactionConfig.md) | The configuration for specifying what content to redact from images. |  [optional] |
|**includeFindings** | **Boolean** | Whether the response should include findings along with the redacted image. |  [optional] |
|**inspectConfig** | [**GooglePrivacyDlpV2InspectConfig**](GooglePrivacyDlpV2InspectConfig.md) |  |  [optional] |
|**locationId** | **String** | Deprecated. This field has no effect. |  [optional] |



