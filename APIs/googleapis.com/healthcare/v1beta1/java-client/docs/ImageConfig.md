

# ImageConfig

Specifies how to handle de-identification of image pixels.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInfoTypes** | **List&lt;String&gt;** | Additional InfoTypes to redact in the images in addition to those used by &#x60;text_redaction_mode&#x60;. Can only be used when &#x60;text_redaction_mode&#x60; is set to &#x60;REDACT_SENSITIVE_TEXT&#x60;, &#x60;REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS&#x60; or &#x60;TEXT_REDACTION_MODE_UNSPECIFIED&#x60;. |  [optional] |
|**excludeInfoTypes** | **List&lt;String&gt;** | InfoTypes to skip redacting, overriding those used by &#x60;text_redaction_mode&#x60;. Can only be used when &#x60;text_redaction_mode&#x60; is set to &#x60;REDACT_SENSITIVE_TEXT&#x60; or &#x60;REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS&#x60;. |  [optional] |
|**textRedactionMode** | [**TextRedactionModeEnum**](#TextRedactionModeEnum) | Determines how to redact text from image. |  [optional] |



## Enum: TextRedactionModeEnum

| Name | Value |
|---- | -----|
| TEXT_REDACTION_MODE_UNSPECIFIED | &quot;TEXT_REDACTION_MODE_UNSPECIFIED&quot; |
| REDACT_ALL_TEXT | &quot;REDACT_ALL_TEXT&quot; |
| REDACT_SENSITIVE_TEXT | &quot;REDACT_SENSITIVE_TEXT&quot; |
| REDACT_NO_TEXT | &quot;REDACT_NO_TEXT&quot; |
| REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS | &quot;REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS&quot; |



