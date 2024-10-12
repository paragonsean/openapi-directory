# SensitiveDataProtectionDlp.GooglePrivacyDlpV2RedactImageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractedText** | **String** | If an image was being inspected and the InspectConfig&#39;s include_quote was set to true, then this field will include all text, if any, that was found in the image. | [optional] 
**inspectResult** | [**GooglePrivacyDlpV2InspectResult**](GooglePrivacyDlpV2InspectResult.md) |  | [optional] 
**redactedImage** | **Blob** | The redacted image. The type will be the same as the original image. | [optional] 


