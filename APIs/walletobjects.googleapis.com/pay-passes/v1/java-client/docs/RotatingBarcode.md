

# RotatingBarcode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateText** | **String** | An optional text that will override the default text that shows under the barcode. This field is intended for a human readable equivalent of the barcode value, used when the barcode cannot be scanned. |  [optional] |
|**renderEncoding** | [**RenderEncodingEnum**](#RenderEncodingEnum) | The render encoding for the barcode. When specified, barcode is rendered in the given encoding. Otherwise best known encoding is chosen by Google. |  [optional] |
|**showCodeText** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**totpDetails** | [**RotatingBarcodeTotpDetails**](RotatingBarcodeTotpDetails.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this barcode. |  [optional] |
|**valuePattern** | **String** | String encoded barcode value. This string supports the following substitutions: * {totp_value_n}: Replaced with the TOTP value (see TotpDetails.parameters). * {totp_timestamp_millis}: Replaced with the timestamp (millis since epoch) at which the barcode was generated. * {totp_timestamp_seconds}: Replaced with the timestamp (seconds since epoch) at which the barcode was generated. |  [optional] |



## Enum: RenderEncodingEnum

| Name | Value |
|---- | -----|
| RENDER_ENCODING_UNSPECIFIED | &quot;RENDER_ENCODING_UNSPECIFIED&quot; |
| UTF_8 | &quot;UTF_8&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BARCODE_TYPE_UNSPECIFIED | &quot;BARCODE_TYPE_UNSPECIFIED&quot; |
| AZTEC | &quot;AZTEC&quot; |
| AZTEC2 | &quot;aztec&quot; |
| CODE_39 | &quot;CODE_39&quot; |
| CODE39 | &quot;code39&quot; |
| CODE_128 | &quot;CODE_128&quot; |
| CODE128 | &quot;code128&quot; |
| CODABAR | &quot;CODABAR&quot; |
| CODABAR2 | &quot;codabar&quot; |
| DATA_MATRIX | &quot;DATA_MATRIX&quot; |
| DATA_MATRIX2 | &quot;dataMatrix&quot; |
| EAN_8 | &quot;EAN_8&quot; |
| EAN8 | &quot;ean8&quot; |
| EAN_13 | &quot;EAN_13&quot; |
| EAN13 | &quot;ean13&quot; |
| EAN132 | &quot;EAN13&quot; |
| ITF_14 | &quot;ITF_14&quot; |
| ITF14 | &quot;itf14&quot; |
| PDF_417 | &quot;PDF_417&quot; |
| PDF417 | &quot;pdf417&quot; |
| PDF4172 | &quot;PDF417&quot; |
| QR_CODE | &quot;QR_CODE&quot; |
| QR_CODE2 | &quot;qrCode&quot; |
| QRCODE | &quot;qrcode&quot; |
| UPC_A | &quot;UPC_A&quot; |
| UPC_A2 | &quot;upcA&quot; |
| TEXT_ONLY | &quot;TEXT_ONLY&quot; |
| TEXT_ONLY2 | &quot;textOnly&quot; |



