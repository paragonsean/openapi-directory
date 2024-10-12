# ExoApi.BarcodeGeneratorPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backgroundColor** | **String** | Image background color (hexadecimal format) | [optional] [default to &#39;#ffffff&#39;]
**fitWidth** | **Boolean** | Stretch barcodes to exactly fit the &#x60;width&#x60;. Due to the nature of barcodes, where every bar&#39;s width is a multiple of the narrowest bar, stretching may result in slightly blurry images, which are more difficult for devices to scan. | [optional] [default to false]
**foregroundColor** | **String** | Barcode color (hexadecimal format) | [optional] [default to &#39;#000000&#39;]
**format** | **String** | Output image format | [optional] [default to &#39;png&#39;]
**height** | **Number** | Height of the PNG code image | [optional] 
**showText** | **Boolean** | Display human-readable text under barcodes | [optional] [default to true]
**type** | **String** | Type of code | [default to &#39;qrcode&#39;]
**value** | **String** | Content to encode into the code | 
**width** | **Number** | Width of the PNG code image | [optional] [default to 256]



## Enum: FormatEnum


* `png` (value: `"png"`)

* `svg` (value: `"svg"`)





## Enum: TypeEnum


* `auspost` (value: `"auspost"`)

* `azteccode` (value: `"azteccode"`)

* `azteccodecompact` (value: `"azteccodecompact"`)

* `aztecrune` (value: `"aztecrune"`)

* `bc412` (value: `"bc412"`)

* `channelcode` (value: `"channelcode"`)

* `codablockf` (value: `"codablockf"`)

* `code11` (value: `"code11"`)

* `code128` (value: `"code128"`)

* `code16k` (value: `"code16k"`)

* `code2of5` (value: `"code2of5"`)

* `code32` (value: `"code32"`)

* `code39` (value: `"code39"`)

* `code39ext` (value: `"code39ext"`)

* `code49` (value: `"code49"`)

* `code93` (value: `"code93"`)

* `code93ext` (value: `"code93ext"`)

* `codeone` (value: `"codeone"`)

* `coop2of5` (value: `"coop2of5"`)

* `daft` (value: `"daft"`)

* `databarexpanded` (value: `"databarexpanded"`)

* `databarexpandedcomposite` (value: `"databarexpandedcomposite"`)

* `databarexpandedstacked` (value: `"databarexpandedstacked"`)

* `databarexpandedstackedcomposite` (value: `"databarexpandedstackedcomposite"`)

* `databarlimited` (value: `"databarlimited"`)

* `databarlimitedcomposite` (value: `"databarlimitedcomposite"`)

* `databaromni` (value: `"databaromni"`)

* `databaromnicomposite` (value: `"databaromnicomposite"`)

* `databarstacked` (value: `"databarstacked"`)

* `databarstackedcomposite` (value: `"databarstackedcomposite"`)

* `databarstackedomni` (value: `"databarstackedomni"`)

* `databarstackedomnicomposite` (value: `"databarstackedomnicomposite"`)

* `databartruncated` (value: `"databartruncated"`)

* `databartruncatedcomposite` (value: `"databartruncatedcomposite"`)

* `datalogic2of5` (value: `"datalogic2of5"`)

* `datamatrix` (value: `"datamatrix"`)

* `datamatrixrectangular` (value: `"datamatrixrectangular"`)

* `datamatrixrectangularextension` (value: `"datamatrixrectangularextension"`)

* `dotcode` (value: `"dotcode"`)

* `ean13` (value: `"ean13"`)

* `ean13composite` (value: `"ean13composite"`)

* `ean14` (value: `"ean14"`)

* `ean2` (value: `"ean2"`)

* `ean5` (value: `"ean5"`)

* `ean8` (value: `"ean8"`)

* `ean8composite` (value: `"ean8composite"`)

* `flattermarken` (value: `"flattermarken"`)

* `gs1-128` (value: `"gs1-128"`)

* `gs1-128composite` (value: `"gs1-128composite"`)

* `gs1-cc` (value: `"gs1-cc"`)

* `gs1datamatrix` (value: `"gs1datamatrix"`)

* `gs1datamatrixrectangular` (value: `"gs1datamatrixrectangular"`)

* `gs1northamericancoupon` (value: `"gs1northamericancoupon"`)

* `gs1qrcode` (value: `"gs1qrcode"`)

* `hanxin` (value: `"hanxin"`)

* `hibcazteccode` (value: `"hibcazteccode"`)

* `hibccodablockf` (value: `"hibccodablockf"`)

* `hibccode128` (value: `"hibccode128"`)

* `hibccode39` (value: `"hibccode39"`)

* `hibcdatamatrix` (value: `"hibcdatamatrix"`)

* `hibcdatamatrixrectangular` (value: `"hibcdatamatrixrectangular"`)

* `hibcmicropdf417` (value: `"hibcmicropdf417"`)

* `hibcpdf417` (value: `"hibcpdf417"`)

* `hibcqrcode` (value: `"hibcqrcode"`)

* `iata2of5` (value: `"iata2of5"`)

* `identcode` (value: `"identcode"`)

* `industrial2of5` (value: `"industrial2of5"`)

* `interleaved2of5` (value: `"interleaved2of5"`)

* `isbn` (value: `"isbn"`)

* `ismn` (value: `"ismn"`)

* `issn` (value: `"issn"`)

* `itf14` (value: `"itf14"`)

* `japanpost` (value: `"japanpost"`)

* `kix` (value: `"kix"`)

* `leitcode` (value: `"leitcode"`)

* `mailmark` (value: `"mailmark"`)

* `matrix2of5` (value: `"matrix2of5"`)

* `maxicode` (value: `"maxicode"`)

* `micropdf417` (value: `"micropdf417"`)

* `microqrcode` (value: `"microqrcode"`)

* `msi` (value: `"msi"`)

* `onecode` (value: `"onecode"`)

* `pdf417` (value: `"pdf417"`)

* `pdf417compact` (value: `"pdf417compact"`)

* `pharmacode` (value: `"pharmacode"`)

* `pharmacode2` (value: `"pharmacode2"`)

* `planet` (value: `"planet"`)

* `plessey` (value: `"plessey"`)

* `posicode` (value: `"posicode"`)

* `postnet` (value: `"postnet"`)

* `pzn` (value: `"pzn"`)

* `qrcode` (value: `"qrcode"`)

* `rationalizedCodabar` (value: `"rationalizedCodabar"`)

* `raw` (value: `"raw"`)

* `royalmail` (value: `"royalmail"`)

* `sscc18` (value: `"sscc18"`)

* `symbol` (value: `"symbol"`)

* `telepen` (value: `"telepen"`)

* `telepennumeric` (value: `"telepennumeric"`)

* `ultracode` (value: `"ultracode"`)

* `upca` (value: `"upca"`)

* `upcacomposite` (value: `"upcacomposite"`)

* `upce` (value: `"upce"`)

* `upcecomposite` (value: `"upcecomposite"`)




