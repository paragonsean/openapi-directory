# GoogleWalletApi.Barcode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateText** | **String** | An optional text that will override the default text that shows under the barcode. This field is intended for a human readable equivalent of the barcode value, used when the barcode cannot be scanned. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#barcode\&quot;&#x60;. | [optional] 
**renderEncoding** | **String** | The render encoding for the barcode. When specified, barcode is rendered in the given encoding. Otherwise best known encoding is chosen by Google. | [optional] 
**showCodeText** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**type** | **String** | The type of barcode. | [optional] 
**value** | **String** | The value encoded in the barcode. | [optional] 



## Enum: RenderEncodingEnum


* `RENDER_ENCODING_UNSPECIFIED` (value: `"RENDER_ENCODING_UNSPECIFIED"`)

* `UTF_8` (value: `"UTF_8"`)





## Enum: TypeEnum


* `BARCODE_TYPE_UNSPECIFIED` (value: `"BARCODE_TYPE_UNSPECIFIED"`)

* `AZTEC` (value: `"AZTEC"`)

* `aztec` (value: `"aztec"`)

* `CODE_39` (value: `"CODE_39"`)

* `code39` (value: `"code39"`)

* `CODE_128` (value: `"CODE_128"`)

* `code128` (value: `"code128"`)

* `CODABAR` (value: `"CODABAR"`)

* `codabar` (value: `"codabar"`)

* `DATA_MATRIX` (value: `"DATA_MATRIX"`)

* `dataMatrix` (value: `"dataMatrix"`)

* `EAN_8` (value: `"EAN_8"`)

* `ean8` (value: `"ean8"`)

* `EAN_13` (value: `"EAN_13"`)

* `ean13` (value: `"ean13"`)

* `EAN13` (value: `"EAN13"`)

* `ITF_14` (value: `"ITF_14"`)

* `itf14` (value: `"itf14"`)

* `PDF_417` (value: `"PDF_417"`)

* `pdf417` (value: `"pdf417"`)

* `PDF417` (value: `"PDF417"`)

* `QR_CODE` (value: `"QR_CODE"`)

* `qrCode` (value: `"qrCode"`)

* `qrcode` (value: `"qrcode"`)

* `UPC_A` (value: `"UPC_A"`)

* `upcA` (value: `"upcA"`)

* `TEXT_ONLY` (value: `"TEXT_ONLY"`)

* `textOnly` (value: `"textOnly"`)




