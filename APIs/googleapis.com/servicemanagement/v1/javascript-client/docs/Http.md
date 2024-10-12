# ServiceManagementApi.Http

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullyDecodeReservedExpansion** | **Boolean** | When set to true, URL path parameters will be fully URI-decoded except in cases of single segment matches in reserved expansion, where \&quot;%2F\&quot; will be left encoded. The default behavior is to not decode RFC 6570 reserved characters in multi segment matches. | [optional] 
**rules** | [**[HttpRule]**](HttpRule.md) | A list of HTTP configuration rules that apply to individual API methods. **NOTE:** All service configuration rules follow \&quot;last one wins\&quot; order. | [optional] 


