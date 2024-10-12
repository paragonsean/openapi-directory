

# GoogleIdentityAccesscontextmanagerV1ApiOperation

Identification for an API Operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**methodSelectors** | [**List&lt;GoogleIdentityAccesscontextmanagerV1MethodSelector&gt;**](GoogleIdentityAccesscontextmanagerV1MethodSelector.md) | API methods or permissions to allow. Method or permission must belong to the service specified by &#x60;service_name&#x60; field. A single MethodSelector entry with &#x60;*&#x60; specified for the &#x60;method&#x60; field will allow all methods AND permissions for the service specified in &#x60;service_name&#x60;. |  [optional] |
|**serviceName** | **String** | The name of the API whose methods or permissions the IngressPolicy or EgressPolicy want to allow. A single ApiOperation with &#x60;service_name&#x60; field set to &#x60;*&#x60; will allow all methods AND permissions for all services. |  [optional] |



