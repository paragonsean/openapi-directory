

# SystemParameter

Define a parameter's name and location. The parameter may be passed as either an HTTP header or a URL query parameter, and if both are passed the behavior is implementation-dependent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**httpHeader** | **String** | Define the HTTP header name to use for the parameter. It is case insensitive. |  [optional] |
|**name** | **String** | Define the name of the parameter, such as \&quot;api_key\&quot; . It is case sensitive. |  [optional] |
|**urlQueryParameter** | **String** | Define the URL query parameter name to use for the parameter. It is case sensitive. |  [optional] |



