# ServiceConsumerManagementApi.HttpRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalBindings** | [**[HttpRule]**](HttpRule.md) | Additional HTTP bindings for the selector. Nested bindings must not contain an &#x60;additional_bindings&#x60; field themselves (that is, the nesting may only be one level deep). | [optional] 
**body** | **String** | The name of the request field whose value is mapped to the HTTP request body, or &#x60;*&#x60; for mapping all request fields not captured by the path pattern to the HTTP body, or omitted for not having any HTTP request body. NOTE: the referred field must be present at the top-level of the request message type. | [optional] 
**custom** | [**CustomHttpPattern**](CustomHttpPattern.md) |  | [optional] 
**_delete** | **String** | Maps to HTTP DELETE. Used for deleting a resource. | [optional] 
**get** | **String** | Maps to HTTP GET. Used for listing and getting information about resources. | [optional] 
**patch** | **String** | Maps to HTTP PATCH. Used for updating a resource. | [optional] 
**post** | **String** | Maps to HTTP POST. Used for creating a resource or performing an action. | [optional] 
**put** | **String** | Maps to HTTP PUT. Used for replacing a resource. | [optional] 
**responseBody** | **String** | Optional. The name of the response field whose value is mapped to the HTTP response body. When omitted, the entire response message will be used as the HTTP response body. NOTE: The referred field must be present at the top-level of the response message type. | [optional] 
**selector** | **String** | Selects a method to which this rule applies. Refer to selector for syntax details. | [optional] 


