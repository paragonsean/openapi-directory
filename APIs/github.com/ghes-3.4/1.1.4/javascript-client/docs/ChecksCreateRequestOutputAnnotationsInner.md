# GitHubV3RestApi.ChecksCreateRequestOutputAnnotationsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationLevel** | **String** | The level of the annotation. | 
**endColumn** | **Number** | The end column of the annotation. Annotations only support &#x60;start_column&#x60; and &#x60;end_column&#x60; on the same line. Omit this parameter if &#x60;start_line&#x60; and &#x60;end_line&#x60; have different values. | [optional] 
**endLine** | **Number** | The end line of the annotation. | 
**message** | **String** | A short description of the feedback for these lines of code. The maximum size is 64 KB. | 
**path** | **String** | The path of the file to add an annotation to. For example, &#x60;assets/css/main.css&#x60;. | 
**rawDetails** | **String** | Details about this annotation. The maximum size is 64 KB. | [optional] 
**startColumn** | **Number** | The start column of the annotation. Annotations only support &#x60;start_column&#x60; and &#x60;end_column&#x60; on the same line. Omit this parameter if &#x60;start_line&#x60; and &#x60;end_line&#x60; have different values. Column numbers start at 1. | [optional] 
**startLine** | **Number** | The start line of the annotation. Line numbers start at 1. | 
**title** | **String** | The title that represents the annotation. The maximum size is 255 characters. | [optional] 



## Enum: AnnotationLevelEnum


* `notice` (value: `"notice"`)

* `warning` (value: `"warning"`)

* `failure` (value: `"failure"`)




