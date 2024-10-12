

# GoogleIdentityAccesscontextmanagerV1EgressTo

Defines the conditions under which an EgressPolicy matches a request. Conditions are based on information about the ApiOperation intended to be performed on the `resources` specified. Note that if the destination of the request is also protected by a ServicePerimeter, then that ServicePerimeter must have an IngressPolicy which allows access in order for this request to succeed. The request must match `operations` AND `resources` fields in order to be allowed egress out of the perimeter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalResources** | **List&lt;String&gt;** | A list of external resources that are allowed to be accessed. Only AWS and Azure resources are supported. For Amazon S3, the supported format is s3://BUCKET_NAME. For Azure Storage, the supported format is azure://myaccount.blob.core.windows.net/CONTAINER_NAME. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently &#39;*&#39; is not allowed. |  [optional] |
|**operations** | [**List&lt;GoogleIdentityAccesscontextmanagerV1ApiOperation&gt;**](GoogleIdentityAccesscontextmanagerV1ApiOperation.md) | A list of ApiOperations allowed to be performed by the sources specified in the corresponding EgressFrom. A request matches if it uses an operation/service in this list. |  [optional] |
|**resources** | **List&lt;String&gt;** | A list of resources, currently only projects in the form &#x60;projects/&#x60;, that are allowed to be accessed by sources defined in the corresponding EgressFrom. A request matches if it contains a resource in this list. If &#x60;*&#x60; is specified for &#x60;resources&#x60;, then this EgressTo rule will authorize access to all resources outside the perimeter. |  [optional] |



