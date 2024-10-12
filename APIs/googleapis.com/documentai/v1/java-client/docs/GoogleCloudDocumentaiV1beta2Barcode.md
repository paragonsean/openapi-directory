

# GoogleCloudDocumentaiV1beta2Barcode

Encodes the detailed information of a barcode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | **String** | Format of a barcode. The supported formats are: - &#x60;CODE_128&#x60;: Code 128 type. - &#x60;CODE_39&#x60;: Code 39 type. - &#x60;CODE_93&#x60;: Code 93 type. - &#x60;CODABAR&#x60;: Codabar type. - &#x60;DATA_MATRIX&#x60;: 2D Data Matrix type. - &#x60;ITF&#x60;: ITF type. - &#x60;EAN_13&#x60;: EAN-13 type. - &#x60;EAN_8&#x60;: EAN-8 type. - &#x60;QR_CODE&#x60;: 2D QR code type. - &#x60;UPC_A&#x60;: UPC-A type. - &#x60;UPC_E&#x60;: UPC-E type. - &#x60;PDF417&#x60;: PDF417 type. - &#x60;AZTEC&#x60;: 2D Aztec code type. - &#x60;DATABAR&#x60;: GS1 DataBar code type. |  [optional] |
|**rawValue** | **String** | Raw value encoded in the barcode. For example: &#x60;&#39;MEBKM:TITLE:Google;URL:https://www.google.com;;&#39;&#x60;. |  [optional] |
|**valueFormat** | **String** | Value format describes the format of the value that a barcode encodes. The supported formats are: - &#x60;CONTACT_INFO&#x60;: Contact information. - &#x60;EMAIL&#x60;: Email address. - &#x60;ISBN&#x60;: ISBN identifier. - &#x60;PHONE&#x60;: Phone number. - &#x60;PRODUCT&#x60;: Product. - &#x60;SMS&#x60;: SMS message. - &#x60;TEXT&#x60;: Text string. - &#x60;URL&#x60;: URL address. - &#x60;WIFI&#x60;: Wifi information. - &#x60;GEO&#x60;: Geo-localization. - &#x60;CALENDAR_EVENT&#x60;: Calendar event. - &#x60;DRIVER_LICENSE&#x60;: Driver&#39;s license. |  [optional] |



