# ForemApiV1.ApiPagesPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bodyJson** | **String** | For JSON pages, the JSON body | [optional] 
**bodyMarkdown** | **String** | The text (in markdown) of the ad (required) | [optional] 
**description** | **String** | For internal use, helps similar pages from one another | [optional] 
**isTopLevelPath** | **Boolean** | If true, the page is available at &#39;/{slug}&#39; instead of &#39;/page/{slug}&#39;, use with caution | [optional] 
**slug** | **String** | Used to link to this page in URLs, must be unique and URL-safe | [optional] 
**template** | **String** | Controls what kind of layout the page is rendered in | [optional] [default to &#39;contained&#39;]
**title** | **String** | Title of the page | [optional] 



## Enum: TemplateEnum


* `contained` (value: `"contained"`)

* `full_within_layout` (value: `"full_within_layout"`)

* `nav_bar_included` (value: `"nav_bar_included"`)

* `json` (value: `"json"`)




