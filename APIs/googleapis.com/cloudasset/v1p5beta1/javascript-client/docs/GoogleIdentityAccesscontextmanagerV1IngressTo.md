# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1IngressTo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**[GoogleIdentityAccesscontextmanagerV1ApiOperation]**](GoogleIdentityAccesscontextmanagerV1ApiOperation.md) | A list of ApiOperations allowed to be performed by the sources specified in corresponding IngressFrom in this ServicePerimeter. | [optional] 
**resources** | **[String]** | A list of resources, currently only projects in the form &#x60;projects/&#x60;, protected by this ServicePerimeter that are allowed to be accessed by sources defined in the corresponding IngressFrom. If a single &#x60;*&#x60; is specified, then access to all resources inside the perimeter are allowed. | [optional] 


