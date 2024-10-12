

# ImageConfig

Specifies how to handle de-identification of image pixels.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**textRedactionMode** | [**TextRedactionModeEnum**](#TextRedactionModeEnum) | Determines how to redact text from image. |  [optional] |



## Enum: TextRedactionModeEnum

| Name | Value |
|---- | -----|
| TEXT_REDACTION_MODE_UNSPECIFIED | &quot;TEXT_REDACTION_MODE_UNSPECIFIED&quot; |
| REDACT_ALL_TEXT | &quot;REDACT_ALL_TEXT&quot; |
| REDACT_SENSITIVE_TEXT | &quot;REDACT_SENSITIVE_TEXT&quot; |
| REDACT_NO_TEXT | &quot;REDACT_NO_TEXT&quot; |



