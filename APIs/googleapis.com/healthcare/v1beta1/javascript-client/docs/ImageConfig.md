# CloudHealthcareApi.ImageConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInfoTypes** | **[String]** | Additional InfoTypes to redact in the images in addition to those used by &#x60;text_redaction_mode&#x60;. Can only be used when &#x60;text_redaction_mode&#x60; is set to &#x60;REDACT_SENSITIVE_TEXT&#x60;, &#x60;REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS&#x60; or &#x60;TEXT_REDACTION_MODE_UNSPECIFIED&#x60;. | [optional] 
**excludeInfoTypes** | **[String]** | InfoTypes to skip redacting, overriding those used by &#x60;text_redaction_mode&#x60;. Can only be used when &#x60;text_redaction_mode&#x60; is set to &#x60;REDACT_SENSITIVE_TEXT&#x60; or &#x60;REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS&#x60;. | [optional] 
**textRedactionMode** | **String** | Determines how to redact text from image. | [optional] 



## Enum: TextRedactionModeEnum


* `TEXT_REDACTION_MODE_UNSPECIFIED` (value: `"TEXT_REDACTION_MODE_UNSPECIFIED"`)

* `REDACT_ALL_TEXT` (value: `"REDACT_ALL_TEXT"`)

* `REDACT_SENSITIVE_TEXT` (value: `"REDACT_SENSITIVE_TEXT"`)

* `REDACT_NO_TEXT` (value: `"REDACT_NO_TEXT"`)

* `REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS` (value: `"REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS"`)




