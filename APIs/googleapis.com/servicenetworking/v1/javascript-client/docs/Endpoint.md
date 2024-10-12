# ServiceNetworkingApi.Endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **[String]** | Unimplemented. Dot not use. DEPRECATED: This field is no longer supported. Instead of using aliases, please specify multiple google.api.Endpoint for each of the intended aliases. Additional names that this endpoint will be hosted on. | [optional] 
**allowCors** | **Boolean** | Allowing [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), aka cross-domain traffic, would allow the backends served from this endpoint to receive and respond to HTTP OPTIONS requests. The response will be used by the browser to determine whether the subsequent cross-origin request is allowed to proceed. | [optional] 
**name** | **String** | The canonical name of this endpoint. | [optional] 
**target** | **String** | The specification of an Internet routable address of API frontend that will handle requests to this [API Endpoint](https://cloud.google.com/apis/design/glossary). It should be either a valid IPv4 address or a fully-qualified domain name. For example, \&quot;8.8.8.8\&quot; or \&quot;myservice.appspot.com\&quot;. | [optional] 


