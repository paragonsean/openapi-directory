# ApiDiscoveryService.RestDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**RestDescriptionAuth**](RestDescriptionAuth.md) |  | [optional] 
**basePath** | **String** | [DEPRECATED] The base path for REST requests. | [optional] 
**baseUrl** | **String** | [DEPRECATED] The base URL for REST requests. | [optional] 
**batchPath** | **String** | The path for REST batch requests. | [optional] 
**canonicalName** | **String** | Indicates how the API name should be capitalized and split into various parts. Useful for generating pretty class names. | [optional] 
**description** | **String** | The description of this API. | [optional] 
**discoveryVersion** | **String** | Indicate the version of the Discovery API used to generate this doc. | [optional] [default to &#39;v1&#39;]
**documentationLink** | **String** | A link to human readable documentation for the API. | [optional] 
**endpoints** | [**[RestDescriptionEndpointsInner]**](RestDescriptionEndpointsInner.md) | A list of location-based endpoint objects for this API. Each object contains the endpoint URL, location, description and deprecation status. | [optional] 
**etag** | **String** | The ETag for this response. | [optional] [readonly] 
**exponentialBackoffDefault** | **Boolean** | Enable exponential backoff for suitable methods in the generated clients. | [optional] 
**features** | **[String]** | A list of supported features for this API. | [optional] 
**icons** | [**DirectoryListItemsInnerIcons**](DirectoryListItemsInnerIcons.md) |  | [optional] 
**id** | **String** | The ID of this API. | [optional] 
**kind** | **String** | The kind for this response. | [optional] [default to &#39;discovery#restDescription&#39;]
**labels** | **[String]** | Labels for the status of this API, such as labs or deprecated. | [optional] 
**methods** | [**{String: RestMethod}**](RestMethod.md) | API-level methods for this API. | [optional] 
**name** | **String** | The name of this API. | [optional] 
**ownerDomain** | **String** | The domain of the owner of this API. Together with the ownerName and a packagePath values, this can be used to generate a library for this API which would have a unique fully qualified name. | [optional] 
**ownerName** | **String** | The name of the owner of this API. See ownerDomain. | [optional] 
**packagePath** | **String** | The package of the owner of this API. See ownerDomain. | [optional] 
**parameters** | [**{String: JsonSchema}**](JsonSchema.md) | Common parameters that apply across all apis. | [optional] 
**protocol** | **String** | The protocol described by this document. | [optional] [default to &#39;rest&#39;]
**resources** | [**{String: RestResource}**](RestResource.md) | The resources in this API. | [optional] 
**revision** | **String** | The version of this API. | [optional] 
**rootUrl** | **String** | The root URL under which all API services live. | [optional] 
**schemas** | [**{String: JsonSchema}**](JsonSchema.md) | The schemas for this API. | [optional] 
**servicePath** | **String** | The base path for all REST requests. | [optional] 
**title** | **String** | The title of this API. | [optional] 
**version** | **String** | The version of this API. | [optional] 
**versionModule** | **Boolean** |  | [optional] 


