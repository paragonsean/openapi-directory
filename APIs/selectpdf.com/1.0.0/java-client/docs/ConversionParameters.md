

# ConversionParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseUrl** | **String** | An optional base url parameter can be used together with html to resolve relative paths from the html string |  [optional] |
|**html** | **String** | The raw html string that will be converted to PDF |  [optional] |
|**key** | **UUID** | The license key required to use the API |  |
|**marginBottom** | **Integer** | Bottom margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) |  [optional] |
|**marginLeft** | **Integer** | Left margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) |  [optional] |
|**marginRight** | **Integer** | Right margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) |  [optional] |
|**marginTop** | **Integer** | Top margin of the generated PDF document in points (1 point &#x3D; 1/72 inch) |  [optional] |
|**pageOrientation** | [**PageOrientationEnum**](#PageOrientationEnum) | Specifies the page orientation of the generated pdf document |  [optional] |
|**pageSize** | [**PageSizeEnum**](#PageSizeEnum) | Specifies the page size of the generated pdf document |  [optional] |
|**url** | **String** | The url that will be converted to PDF |  [optional] |



## Enum: PageOrientationEnum

| Name | Value |
|---- | -----|
| PORTRAIT | &quot;Portrait&quot; |
| LANDSCAPE | &quot;Landscape&quot; |



## Enum: PageSizeEnum

| Name | Value |
|---- | -----|
| A1 | &quot;A1&quot; |
| A2 | &quot;A2&quot; |
| A3 | &quot;A3&quot; |
| A4 | &quot;A4&quot; |
| A5 | &quot;A5&quot; |
| LETTER | &quot;Letter&quot; |
| HALF_LETTER | &quot;HalfLetter&quot; |
| LEDGER | &quot;Ledger&quot; |
| LEGAL | &quot;Legal&quot; |



