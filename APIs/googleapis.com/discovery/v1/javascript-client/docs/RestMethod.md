# ApiDiscoveryService.RestMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **Boolean** | Whether this method is deprecated. | [optional] 
**description** | **String** | Description of this method. | [optional] 
**etagRequired** | **Boolean** | Whether this method requires an ETag to be specified. The ETag is sent as an HTTP If-Match or If-None-Match header. | [optional] 
**flatPath** | **String** | The URI path of this REST method in (RFC 6570) format without level 2 features ({+var}). Supplementary to the path property. | [optional] 
**httpMethod** | **String** | HTTP method used by this method. | [optional] 
**id** | **String** | A unique ID for this method. This property can be used to match methods between different versions of Discovery. | [optional] 
**mediaUpload** | [**RestMethodMediaUpload**](RestMethodMediaUpload.md) |  | [optional] 
**parameterOrder** | **[String]** | Ordered list of required parameters, serves as a hint to clients on how to structure their method signatures. The array is ordered such that the \&quot;most-significant\&quot; parameter appears first. | [optional] 
**parameters** | [**{String: JsonSchema}**](JsonSchema.md) | Details for all parameters in this method. | [optional] 
**path** | **String** | The URI path of this REST method. Should be used in conjunction with the basePath property at the api-level. | [optional] 
**request** | [**RestMethodRequest**](RestMethodRequest.md) |  | [optional] 
**response** | [**RestMethodResponse**](RestMethodResponse.md) |  | [optional] 
**scopes** | **[String]** | OAuth 2.0 scopes applicable to this method. | [optional] 
**supportsMediaDownload** | **Boolean** | Whether this method supports media downloads. | [optional] 
**supportsMediaUpload** | **Boolean** | Whether this method supports media uploads. | [optional] 
**supportsSubscription** | **Boolean** | Whether this method supports subscriptions. | [optional] 
**useMediaDownloadService** | **Boolean** | Indicates that downloads from this method should use the download service URL (i.e. \&quot;/download\&quot;). Only applies if the method supports media download. | [optional] 


