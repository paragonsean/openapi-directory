

# GoogleIdentityAccesscontextmanagerV1IngressTo

Defines the conditions under which an IngressPolicy matches a request. Conditions are based on information about the ApiOperation intended to be performed on the target resource of the request. The request must satisfy what is defined in `operations` AND `resources` in order to match.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operations** | [**List&lt;GoogleIdentityAccesscontextmanagerV1ApiOperation&gt;**](GoogleIdentityAccesscontextmanagerV1ApiOperation.md) | A list of ApiOperations allowed to be performed by the sources specified in corresponding IngressFrom in this ServicePerimeter. |  [optional] |
|**resources** | **List&lt;String&gt;** | A list of resources, currently only projects in the form &#x60;projects/&#x60;, protected by this ServicePerimeter that are allowed to be accessed by sources defined in the corresponding IngressFrom. If a single &#x60;*&#x60; is specified, then access to all resources inside the perimeter are allowed. |  [optional] |



