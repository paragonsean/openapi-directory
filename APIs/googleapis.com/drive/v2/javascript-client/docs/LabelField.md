# GoogleDriveApi.LabelField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateString** | **[Date]** | Only present if valueType is dateString. RFC 3339 formatted date: YYYY-MM-DD. | [optional] 
**id** | **String** | The identifier of this label field. | [optional] 
**integer** | **[String]** | Only present if &#x60;valueType&#x60; is &#x60;integer&#x60;. | [optional] 
**kind** | **String** | This is always &#x60;drive#labelField&#x60;. | [optional] [default to &#39;drive#labelField&#39;]
**selection** | **[String]** | Only present if &#x60;valueType&#x60; is &#x60;selection&#x60; | [optional] 
**text** | **[String]** | Only present if &#x60;valueType&#x60; is &#x60;text&#x60;. | [optional] 
**user** | [**[User]**](User.md) | Only present if &#x60;valueType&#x60; is &#x60;user&#x60;. | [optional] 
**valueType** | **String** | The field type. While new values may be supported in the future, the following are currently allowed: * &#x60;dateString&#x60; * &#x60;integer&#x60; * &#x60;selection&#x60; * &#x60;text&#x60; * &#x60;user&#x60; | [optional] 


