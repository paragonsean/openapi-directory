# ServiceConsumerManagementApi.JwtLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **String** | Specifies cookie name to extract JWT token. | [optional] 
**header** | **String** | Specifies HTTP header name to extract JWT token. | [optional] 
**query** | **String** | Specifies URL query parameter name to extract JWT token. | [optional] 
**valuePrefix** | **String** | The value prefix. The value format is \&quot;value_prefix{token}\&quot; Only applies to \&quot;in\&quot; header type. Must be empty for \&quot;in\&quot; query type. If not empty, the header value has to match (case sensitive) this prefix. If not matched, JWT will not be extracted. If matched, JWT will be extracted after the prefix is removed. For example, for \&quot;Authorization: Bearer {JWT}\&quot;, value_prefix&#x3D;\&quot;Bearer \&quot; with a space at the end. | [optional] 


