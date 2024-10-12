# SelectPdfHtmlToPdfApi.ConversionParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseUrl** | **String** | An optional base url parameter can be used together with html to resolve relative paths from the html string | [optional] 
**html** | **String** | The raw html string that will be converted to PDF | [optional] 
**key** | **String** | The license key required to use the API | 
**marginBottom** | **Number** | Bottom margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) | [optional] 
**marginLeft** | **Number** | Left margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) | [optional] 
**marginRight** | **Number** | Right margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) | [optional] 
**marginTop** | **Number** | Top margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) | [optional] 
**pageOrientation** | **String** | Specifies the page orientation of the generated pdf document | [optional] [default to &#39;Portrait&#39;]
**pageSize** | **String** | Specifies the page size of the generated pdf document | [optional] [default to &#39;A4&#39;]
**url** | **String** | The url that will be converted to PDF | [optional] 



## Enum: PageOrientationEnum


* `Portrait` (value: `"Portrait"`)

* `Landscape` (value: `"Landscape"`)





## Enum: PageSizeEnum


* `A1` (value: `"A1"`)

* `A2` (value: `"A2"`)

* `A3` (value: `"A3"`)

* `A4` (value: `"A4"`)

* `A5` (value: `"A5"`)

* `Letter` (value: `"Letter"`)

* `HalfLetter` (value: `"HalfLetter"`)

* `Ledger` (value: `"Ledger"`)

* `Legal` (value: `"Legal"`)




