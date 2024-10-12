# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1EgressTo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalResources** | **[String]** | A list of external resources that are allowed to be accessed. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently &#39;*&#39; is not allowed. | [optional] 
**operations** | [**[GoogleIdentityAccesscontextmanagerV1ApiOperation]**](GoogleIdentityAccesscontextmanagerV1ApiOperation.md) | A list of ApiOperations allowed to be performed by the sources specified in the corresponding EgressFrom. A request matches if it uses an operation/service in this list. | [optional] 
**resources** | **[String]** | A list of resources, currently only projects in the form &#x60;projects/&#x60;, that are allowed to be accessed by sources defined in the corresponding EgressFrom. A request matches if it contains a resource in this list. If &#x60;*&#x60; is specified for &#x60;resources&#x60;, then this EgressTo rule will authorize access to all resources outside the perimeter. | [optional] 


