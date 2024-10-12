

# HtmlRendererPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**css** | **String** | Custom CSS style content |  [optional] |
|**footer** | **String** | HTML page footer content. Use special CSS classes to inject parameters: \&quot;date\&quot;, \&quot;pageNumber\&quot;, \&quot;totalPages\&quot; |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Output format |  [optional] |
|**header** | **String** | HTML page header content. Use special CSS classes to inject parameters: \&quot;date\&quot;, \&quot;pageNumber\&quot;, \&quot;totalPages\&quot; |  [optional] |
|**html** | **String** | HTML content to render |  |
|**imageHeight** | **Integer** | PNG image height (in pixels). In not specified, the height will automatically adapt to the content |  [optional] |
|**imageWidth** | **Integer** | PNG image width (in pixels) |  [optional] |
|**landscape** | **Boolean** | PDF document orientation |  [optional] |
|**margin** | **String** | PDF page margin (in px, mm, in or cm) |  [optional] |
|**marginBottom** | **String** | PDF bottom margin (in px, mm, in or cm) |  [optional] |
|**marginLeft** | **String** | PDF left margin (in px, mm, in or cm) |  [optional] |
|**marginRight** | **String** | PDF right margin (in px, mm, in or cm) |  [optional] |
|**marginTop** | **String** | PDF top margin (in px, mm, in or cm) |  [optional] |
|**pageHeight** | **String** | Explicit PDF height (in px, mm, in or cm) |  [optional] |
|**pageSize** | [**PageSizeEnum**](#PageSizeEnum) | Default page size of the generated PDF document |  [optional] |
|**pageWidth** | **String** | Explicit PDF width (in px, mm, in or cm) |  [optional] |
|**title** | **String** | Title of the generated PDF document or PNG image |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PDF | &quot;pdf&quot; |
| PNG | &quot;png&quot; |



## Enum: PageSizeEnum

| Name | Value |
|---- | -----|
| LETTER | &quot;letter&quot; |
| LEGAL | &quot;legal&quot; |
| TABLOID | &quot;tabloid&quot; |
| LEDGER | &quot;ledger&quot; |
| A0 | &quot;a0&quot; |
| A1 | &quot;a1&quot; |
| A2 | &quot;a2&quot; |
| A3 | &quot;a3&quot; |
| A4 | &quot;a4&quot; |
| A5 | &quot;a5&quot; |
| A6 | &quot;a6&quot; |



