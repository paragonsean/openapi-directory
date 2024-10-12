# ServiceDirectoryApi.Endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | Optional. An IPv4 or IPv6 address. Service Directory rejects bad addresses like: * &#x60;8.8.8&#x60; * &#x60;8.8.8.8:53&#x60; * &#x60;test:bad:address&#x60; * &#x60;[::1]&#x60; * &#x60;[::1]:8080&#x60; Limited to 45 characters. | [optional] 
**annotations** | **{String: String}** | Optional. Annotations for the endpoint. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 512 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/) Annotations that fails to meet these requirements are rejected. Note: This field is equivalent to the &#x60;metadata&#x60; field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory. | [optional] 
**name** | **String** | Immutable. The resource name for the endpoint in the format &#x60;projects/_*_/locations/_*_/namespaces/_*_/services/_*_/endpoints/_*&#x60;. | [optional] 
**network** | **String** | Immutable. The Google Compute Engine network (VPC) of the endpoint in the format &#x60;projects//locations/global/networks/_*&#x60;. The project must be specified by project number (project id is rejected). Incorrectly formatted networks are rejected, we also check to make sure that you have the servicedirectory.networks.attach permission on the project specified. | [optional] 
**port** | **Number** | Optional. Service Directory rejects values outside of &#x60;[0, 65535]&#x60;. | [optional] 
**uid** | **String** | Output only. The globally unique identifier of the endpoint in the UUID4 format. | [optional] [readonly] 


