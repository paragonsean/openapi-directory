# GoogleDriveApi.Reply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The action the reply performed to the parent comment. Valid values are: * &#x60;resolve&#x60; * &#x60;reopen&#x60; | [optional] 
**author** | [**User**](User.md) |  | [optional] 
**content** | **String** | The plain text content of the reply. This field is used for setting the content, while &#x60;htmlContent&#x60; should be displayed. This is required on creates if no &#x60;action&#x60; is specified. | [optional] 
**createdTime** | **Date** | The time at which the reply was created (RFC 3339 date-time). | [optional] 
**deleted** | **Boolean** | Output only. Whether the reply has been deleted. A deleted reply has no content. | [optional] 
**htmlContent** | **String** | Output only. The content of the reply with HTML formatting. | [optional] 
**id** | **String** | Output only. The ID of the reply. | [optional] 
**kind** | **String** | Output only. Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#reply\&quot;&#x60;. | [optional] [default to &#39;drive#reply&#39;]
**modifiedTime** | **Date** | The last time the reply was modified (RFC 3339 date-time). | [optional] 


