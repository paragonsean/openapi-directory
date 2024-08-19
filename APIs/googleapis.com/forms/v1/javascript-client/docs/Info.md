# GoogleFormsApi.Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the form. | [optional] 
**documentTitle** | **String** | Output only. The title of the document which is visible in Drive. If &#x60;Info.title&#x60; is empty, &#x60;document_title&#x60; may appear in its place in the Google Forms UI and be visible to responders. &#x60;document_title&#x60; can be set on create, but cannot be modified by a batchUpdate request. Please use the [Google Drive API](https://developers.google.com/drive/api/v3/reference/files/update) if you need to programmatically update &#x60;document_title&#x60;. | [optional] [readonly] 
**title** | **String** | Required. The title of the form which is visible to responders. | [optional] 


