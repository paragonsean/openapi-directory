

# UriOverride

URI Override. When specified, all the HTTP tasks inside the queue will be partially or fully overridden depending on the configured values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | Host override. When specified, replaces the host part of the task URL. For example, if the task URL is \&quot;https://www.google.com,\&quot; and host value is set to \&quot;example.net\&quot;, the overridden URI will be changed to \&quot;https://example.net.\&quot; Host value cannot be an empty string (INVALID_ARGUMENT). |  [optional] |
|**pathOverride** | [**PathOverride**](PathOverride.md) |  |  [optional] |
|**port** | **String** | Port override. When specified, replaces the port part of the task URI. For instance, for a URI http://www.google.com/foo and port&#x3D;123, the overridden URI becomes http://www.google.com:123/foo. Note that the port value must be a positive integer. Setting the port to 0 (Zero) clears the URI port. |  [optional] |
|**queryOverride** | [**QueryOverride**](QueryOverride.md) |  |  [optional] |
|**scheme** | [**SchemeEnum**](#SchemeEnum) | Scheme override. When specified, the task URI scheme is replaced by the provided value (HTTP or HTTPS). |  [optional] |
|**uriOverrideEnforceMode** | [**UriOverrideEnforceModeEnum**](#UriOverrideEnforceModeEnum) | URI Override Enforce Mode When specified, determines the Target UriOverride mode. If not specified, it defaults to ALWAYS. |  [optional] |



## Enum: SchemeEnum

| Name | Value |
|---- | -----|
| SCHEME_UNSPECIFIED | &quot;SCHEME_UNSPECIFIED&quot; |
| HTTP | &quot;HTTP&quot; |
| HTTPS | &quot;HTTPS&quot; |



## Enum: UriOverrideEnforceModeEnum

| Name | Value |
|---- | -----|
| URI_OVERRIDE_ENFORCE_MODE_UNSPECIFIED | &quot;URI_OVERRIDE_ENFORCE_MODE_UNSPECIFIED&quot; |
| IF_NOT_EXISTS | &quot;IF_NOT_EXISTS&quot; |
| ALWAYS | &quot;ALWAYS&quot; |



