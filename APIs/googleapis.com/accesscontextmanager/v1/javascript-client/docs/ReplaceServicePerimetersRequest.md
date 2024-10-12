# AccessContextManagerApi.ReplaceServicePerimetersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | Optional. The etag for the version of the Access Policy that this replace operation is to be performed on. If, at the time of replace, the etag for the Access Policy stored in Access Context Manager is different from the specified etag, then the replace operation will not be performed and the call will fail. This field is not required. If etag is not provided, the operation will be performed as if a valid etag is provided. | [optional] 
**servicePerimeters** | [**[ServicePerimeter]**](ServicePerimeter.md) | Required. The desired Service Perimeters that should replace all existing Service Perimeters in the Access Policy. | [optional] 


