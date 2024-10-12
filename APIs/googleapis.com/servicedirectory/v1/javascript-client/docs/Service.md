# ServiceDirectoryApi.Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Optional. Annotations for the service. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected Note: This field is equivalent to the &#x60;metadata&#x60; field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory. | [optional] 
**endpoints** | [**[Endpoint]**](Endpoint.md) | Output only. Endpoints associated with this service. Returned on LookupService.ResolveService. Control plane clients should use RegistrationService.ListEndpoints. | [optional] [readonly] 
**name** | **String** | Immutable. The resource name for the service in the format &#x60;projects/_*_/locations/_*_/namespaces/_*_/services/_*&#x60;. | [optional] 
**uid** | **String** | Output only. The globally unique identifier of the service in the UUID4 format. | [optional] [readonly] 


