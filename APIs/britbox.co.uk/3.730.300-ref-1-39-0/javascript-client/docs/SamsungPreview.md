# RocketServices.SamsungPreview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **Number** | For public preview only If specified, the time at which the preview content is updated. The time is at most 1 week into the future. By default, the preview content is updated every 10 minutes, whenever the TV is switched on, or the JSON file changes.  | [optional] 
**expiresOnly** | **Boolean** | For public preview only If this value is \&quot;true\&quot;, the preview content is updated only at the time specified by the \&quot;expires\&quot; parameter.  | [optional] [default to false]
**sections** | [**[SamsungPreviewSection]**](SamsungPreviewSection.md) | Preview sections | 


