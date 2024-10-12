# GitHubV3RestApi.MarkdownRenderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **String** | The repository context to use when creating references in &#x60;gfm&#x60; mode.  For example, setting &#x60;context&#x60; to &#x60;octo-org/octo-repo&#x60; will change the text &#x60;#42&#x60; into an HTML link to issue 42 in the &#x60;octo-org/octo-repo&#x60; repository. | [optional] 
**mode** | **String** | The rendering mode. Can be either &#x60;markdown&#x60; or &#x60;gfm&#x60;. | [optional] [default to &#39;markdown&#39;]
**text** | **String** | The Markdown text to render in HTML. | 



## Enum: ModeEnum


* `markdown` (value: `"markdown"`)

* `gfm` (value: `"gfm"`)




