# TurbineLabsApi.Redirect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from** | **String** | A regexp that will be matched against the URL (not including the host/port). May include capture groups for reference in \&quot;to.\&quot; | 
**headerConstraints** | [**[HeaderConstraint]**](HeaderConstraint.md) |  | [optional] 
**name** | **String** | A unique (to this Domain) name for the Redirect. Must match the regexp \&quot;^[0-9a-zA-Z-]+$\&quot; | 
**redirectType** | **String** | How this redirect should be presented via HTTP response code. | 
**to** | **String** | The new URL that will be constructed from the request. Capture groups from \&quot;from\&quot; may be referenced as \&quot;$&amp;lt;group number&amp;gt;\&quot; which begins at 1. | 



## Enum: RedirectTypeEnum


* `permanent` (value: `"permanent"`)

* `temporary` (value: `"temporary"`)




