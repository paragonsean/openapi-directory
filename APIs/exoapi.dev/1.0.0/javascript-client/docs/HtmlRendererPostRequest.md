# ExoApi.HtmlRendererPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**css** | **String** | Custom CSS style content | [optional] 
**footer** | **String** | HTML page footer content. Use special CSS classes to inject parameters: \&quot;date\&quot;, \&quot;pageNumber\&quot;, \&quot;totalPages\&quot; | [optional] 
**format** | **String** | Output format | [optional] [default to &#39;pdf&#39;]
**header** | **String** | HTML page header content. Use special CSS classes to inject parameters: \&quot;date\&quot;, \&quot;pageNumber\&quot;, \&quot;totalPages\&quot; | [optional] 
**html** | **String** | HTML content to render | 
**imageHeight** | **Number** | PNG image height (in pixels). In not specified, the height will automatically adapt to the content | [optional] 
**imageWidth** | **Number** | PNG image width (in pixels) | [optional] [default to 512]
**landscape** | **Boolean** | PDF document orientation | [optional] [default to false]
**margin** | **String** | PDF page margin (in px, mm, in or cm) | [optional] [default to &#39;0&#39;]
**marginBottom** | **String** | PDF bottom margin (in px, mm, in or cm) | [optional] [default to &#39;0&#39;]
**marginLeft** | **String** | PDF left margin (in px, mm, in or cm) | [optional] [default to &#39;0&#39;]
**marginRight** | **String** | PDF right margin (in px, mm, in or cm) | [optional] [default to &#39;0&#39;]
**marginTop** | **String** | PDF top margin (in px, mm, in or cm) | [optional] [default to &#39;0&#39;]
**pageHeight** | **String** | Explicit PDF height (in px, mm, in or cm) | [optional] 
**pageSize** | **String** | Default page size of the generated PDF document | [optional] [default to &#39;a4&#39;]
**pageWidth** | **String** | Explicit PDF width (in px, mm, in or cm) | [optional] 
**title** | **String** | Title of the generated PDF document or PNG image | [optional] 



## Enum: FormatEnum


* `pdf` (value: `"pdf"`)

* `png` (value: `"png"`)





## Enum: PageSizeEnum


* `letter` (value: `"letter"`)

* `legal` (value: `"legal"`)

* `tabloid` (value: `"tabloid"`)

* `ledger` (value: `"ledger"`)

* `a0` (value: `"a0"`)

* `a1` (value: `"a1"`)

* `a2` (value: `"a2"`)

* `a3` (value: `"a3"`)

* `a4` (value: `"a4"`)

* `a5` (value: `"a5"`)

* `a6` (value: `"a6"`)




