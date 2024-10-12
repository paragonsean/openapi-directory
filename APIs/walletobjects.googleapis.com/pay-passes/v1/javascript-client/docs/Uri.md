# GooglePayPassesApi.Uri

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The URI&#39;s title appearing in the app as text. Recommended maximum is 20 characters to ensure full string is displayed on smaller screens. Note that in some contexts this text is not used, such as when &#x60;description&#x60; is part of an image. | [optional] 
**id** | **String** | The ID associated with a uri. This field is here to enable ease of management of uris. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#uri\&quot;&#x60;. | [optional] 
**localizedDescription** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**uri** | **String** | The location of a web page, image, or other resource. URIs in the &#x60;LinksModuleData&#x60; module can have different prefixes indicating the type of URI (a link to a web page, a link to a map, a telephone number, or an email address). URIs must have a scheme. | [optional] 


