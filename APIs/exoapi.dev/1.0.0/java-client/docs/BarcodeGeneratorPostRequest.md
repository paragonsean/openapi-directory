

# BarcodeGeneratorPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backgroundColor** | **String** | Image background color (hexadecimal format) |  [optional] |
|**fitWidth** | **Boolean** | Stretch barcodes to exactly fit the &#x60;width&#x60;. Due to the nature of barcodes, where every bar&#39;s width is a multiple of the narrowest bar, stretching may result in slightly blurry images, which are more difficult for devices to scan. |  [optional] |
|**foregroundColor** | **String** | Barcode color (hexadecimal format) |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Output image format |  [optional] |
|**height** | **Integer** | Height of the PNG code image |  [optional] |
|**showText** | **Boolean** | Display human-readable text under barcodes |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of code |  |
|**value** | **String** | Content to encode into the code |  |
|**width** | **Integer** | Width of the PNG code image |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PNG | &quot;png&quot; |
| SVG | &quot;svg&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUSPOST | &quot;auspost&quot; |
| AZTECCODE | &quot;azteccode&quot; |
| AZTECCODECOMPACT | &quot;azteccodecompact&quot; |
| AZTECRUNE | &quot;aztecrune&quot; |
| BC412 | &quot;bc412&quot; |
| CHANNELCODE | &quot;channelcode&quot; |
| CODABLOCKF | &quot;codablockf&quot; |
| CODE11 | &quot;code11&quot; |
| CODE128 | &quot;code128&quot; |
| CODE16K | &quot;code16k&quot; |
| CODE2OF5 | &quot;code2of5&quot; |
| CODE32 | &quot;code32&quot; |
| CODE39 | &quot;code39&quot; |
| CODE39EXT | &quot;code39ext&quot; |
| CODE49 | &quot;code49&quot; |
| CODE93 | &quot;code93&quot; |
| CODE93EXT | &quot;code93ext&quot; |
| CODEONE | &quot;codeone&quot; |
| COOP2OF5 | &quot;coop2of5&quot; |
| DAFT | &quot;daft&quot; |
| DATABAREXPANDED | &quot;databarexpanded&quot; |
| DATABAREXPANDEDCOMPOSITE | &quot;databarexpandedcomposite&quot; |
| DATABAREXPANDEDSTACKED | &quot;databarexpandedstacked&quot; |
| DATABAREXPANDEDSTACKEDCOMPOSITE | &quot;databarexpandedstackedcomposite&quot; |
| DATABARLIMITED | &quot;databarlimited&quot; |
| DATABARLIMITEDCOMPOSITE | &quot;databarlimitedcomposite&quot; |
| DATABAROMNI | &quot;databaromni&quot; |
| DATABAROMNICOMPOSITE | &quot;databaromnicomposite&quot; |
| DATABARSTACKED | &quot;databarstacked&quot; |
| DATABARSTACKEDCOMPOSITE | &quot;databarstackedcomposite&quot; |
| DATABARSTACKEDOMNI | &quot;databarstackedomni&quot; |
| DATABARSTACKEDOMNICOMPOSITE | &quot;databarstackedomnicomposite&quot; |
| DATABARTRUNCATED | &quot;databartruncated&quot; |
| DATABARTRUNCATEDCOMPOSITE | &quot;databartruncatedcomposite&quot; |
| DATALOGIC2OF5 | &quot;datalogic2of5&quot; |
| DATAMATRIX | &quot;datamatrix&quot; |
| DATAMATRIXRECTANGULAR | &quot;datamatrixrectangular&quot; |
| DATAMATRIXRECTANGULAREXTENSION | &quot;datamatrixrectangularextension&quot; |
| DOTCODE | &quot;dotcode&quot; |
| EAN13 | &quot;ean13&quot; |
| EAN13COMPOSITE | &quot;ean13composite&quot; |
| EAN14 | &quot;ean14&quot; |
| EAN2 | &quot;ean2&quot; |
| EAN5 | &quot;ean5&quot; |
| EAN8 | &quot;ean8&quot; |
| EAN8COMPOSITE | &quot;ean8composite&quot; |
| FLATTERMARKEN | &quot;flattermarken&quot; |
| GS1_128 | &quot;gs1-128&quot; |
| GS1_128COMPOSITE | &quot;gs1-128composite&quot; |
| GS1_CC | &quot;gs1-cc&quot; |
| GS1DATAMATRIX | &quot;gs1datamatrix&quot; |
| GS1DATAMATRIXRECTANGULAR | &quot;gs1datamatrixrectangular&quot; |
| GS1NORTHAMERICANCOUPON | &quot;gs1northamericancoupon&quot; |
| GS1QRCODE | &quot;gs1qrcode&quot; |
| HANXIN | &quot;hanxin&quot; |
| HIBCAZTECCODE | &quot;hibcazteccode&quot; |
| HIBCCODABLOCKF | &quot;hibccodablockf&quot; |
| HIBCCODE128 | &quot;hibccode128&quot; |
| HIBCCODE39 | &quot;hibccode39&quot; |
| HIBCDATAMATRIX | &quot;hibcdatamatrix&quot; |
| HIBCDATAMATRIXRECTANGULAR | &quot;hibcdatamatrixrectangular&quot; |
| HIBCMICROPDF417 | &quot;hibcmicropdf417&quot; |
| HIBCPDF417 | &quot;hibcpdf417&quot; |
| HIBCQRCODE | &quot;hibcqrcode&quot; |
| IATA2OF5 | &quot;iata2of5&quot; |
| IDENTCODE | &quot;identcode&quot; |
| INDUSTRIAL2OF5 | &quot;industrial2of5&quot; |
| INTERLEAVED2OF5 | &quot;interleaved2of5&quot; |
| ISBN | &quot;isbn&quot; |
| ISMN | &quot;ismn&quot; |
| ISSN | &quot;issn&quot; |
| ITF14 | &quot;itf14&quot; |
| JAPANPOST | &quot;japanpost&quot; |
| KIX | &quot;kix&quot; |
| LEITCODE | &quot;leitcode&quot; |
| MAILMARK | &quot;mailmark&quot; |
| MATRIX2OF5 | &quot;matrix2of5&quot; |
| MAXICODE | &quot;maxicode&quot; |
| MICROPDF417 | &quot;micropdf417&quot; |
| MICROQRCODE | &quot;microqrcode&quot; |
| MSI | &quot;msi&quot; |
| ONECODE | &quot;onecode&quot; |
| PDF417 | &quot;pdf417&quot; |
| PDF417COMPACT | &quot;pdf417compact&quot; |
| PHARMACODE | &quot;pharmacode&quot; |
| PHARMACODE2 | &quot;pharmacode2&quot; |
| PLANET | &quot;planet&quot; |
| PLESSEY | &quot;plessey&quot; |
| POSICODE | &quot;posicode&quot; |
| POSTNET | &quot;postnet&quot; |
| PZN | &quot;pzn&quot; |
| QRCODE | &quot;qrcode&quot; |
| RATIONALIZED_CODABAR | &quot;rationalizedCodabar&quot; |
| RAW | &quot;raw&quot; |
| ROYALMAIL | &quot;royalmail&quot; |
| SSCC18 | &quot;sscc18&quot; |
| SYMBOL | &quot;symbol&quot; |
| TELEPEN | &quot;telepen&quot; |
| TELEPENNUMERIC | &quot;telepennumeric&quot; |
| ULTRACODE | &quot;ultracode&quot; |
| UPCA | &quot;upca&quot; |
| UPCACOMPOSITE | &quot;upcacomposite&quot; |
| UPCE | &quot;upce&quot; |
| UPCECOMPOSITE | &quot;upcecomposite&quot; |



