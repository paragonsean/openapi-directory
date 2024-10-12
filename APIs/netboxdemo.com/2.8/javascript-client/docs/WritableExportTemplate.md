# NetBoxApi.WritableExportTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** |  | 
**description** | **String** |  | [optional] 
**fileExtension** | **String** | Extension to append to the rendered filename | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**mimeType** | **String** | Defaults to &lt;code&gt;text/plain&lt;/code&gt; | [optional] 
**name** | **String** |  | 
**templateCode** | **String** | The list of objects being exported is passed as a context variable named &lt;code&gt;queryset&lt;/code&gt;. | 
**templateLanguage** | **String** |  | [optional] 



## Enum: TemplateLanguageEnum


* `django` (value: `"django"`)

* `jinja2` (value: `"jinja2"`)




