

# OperationResultInfoBaseResource

Base class for operation result info.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | [**OperationResultInfoBase**](OperationResultInfoBase.md) |  |  [optional] |
|**headers** | **Map&lt;String, List&lt;String&gt;&gt;** | HTTP headers associated with this operation. |  [optional] |
|**statusCode** | [**StatusCodeEnum**](#StatusCodeEnum) | HTTP Status Code of the operation. |  [optional] |



## Enum: StatusCodeEnum

| Name | Value |
|---- | -----|
| CONTINUE | &quot;Continue&quot; |
| SWITCHING_PROTOCOLS | &quot;SwitchingProtocols&quot; |
| OK | &quot;OK&quot; |
| CREATED | &quot;Created&quot; |
| ACCEPTED | &quot;Accepted&quot; |
| NON_AUTHORITATIVE_INFORMATION | &quot;NonAuthoritativeInformation&quot; |
| NO_CONTENT | &quot;NoContent&quot; |
| RESET_CONTENT | &quot;ResetContent&quot; |
| PARTIAL_CONTENT | &quot;PartialContent&quot; |
| MULTIPLE_CHOICES | &quot;MultipleChoices&quot; |
| AMBIGUOUS | &quot;Ambiguous&quot; |
| MOVED_PERMANENTLY | &quot;MovedPermanently&quot; |
| MOVED | &quot;Moved&quot; |
| FOUND | &quot;Found&quot; |
| REDIRECT | &quot;Redirect&quot; |
| SEE_OTHER | &quot;SeeOther&quot; |
| REDIRECT_METHOD | &quot;RedirectMethod&quot; |
| NOT_MODIFIED | &quot;NotModified&quot; |
| USE_PROXY | &quot;UseProxy&quot; |
| UNUSED | &quot;Unused&quot; |
| TEMPORARY_REDIRECT | &quot;TemporaryRedirect&quot; |
| REDIRECT_KEEP_VERB | &quot;RedirectKeepVerb&quot; |
| BAD_REQUEST | &quot;BadRequest&quot; |
| UNAUTHORIZED | &quot;Unauthorized&quot; |
| PAYMENT_REQUIRED | &quot;PaymentRequired&quot; |
| FORBIDDEN | &quot;Forbidden&quot; |
| NOT_FOUND | &quot;NotFound&quot; |
| METHOD_NOT_ALLOWED | &quot;MethodNotAllowed&quot; |
| NOT_ACCEPTABLE | &quot;NotAcceptable&quot; |
| PROXY_AUTHENTICATION_REQUIRED | &quot;ProxyAuthenticationRequired&quot; |
| REQUEST_TIMEOUT | &quot;RequestTimeout&quot; |
| CONFLICT | &quot;Conflict&quot; |
| GONE | &quot;Gone&quot; |
| LENGTH_REQUIRED | &quot;LengthRequired&quot; |
| PRECONDITION_FAILED | &quot;PreconditionFailed&quot; |
| REQUEST_ENTITY_TOO_LARGE | &quot;RequestEntityTooLarge&quot; |
| REQUEST_URI_TOO_LONG | &quot;RequestUriTooLong&quot; |
| UNSUPPORTED_MEDIA_TYPE | &quot;UnsupportedMediaType&quot; |
| REQUESTED_RANGE_NOT_SATISFIABLE | &quot;RequestedRangeNotSatisfiable&quot; |
| EXPECTATION_FAILED | &quot;ExpectationFailed&quot; |
| UPGRADE_REQUIRED | &quot;UpgradeRequired&quot; |
| INTERNAL_SERVER_ERROR | &quot;InternalServerError&quot; |
| NOT_IMPLEMENTED | &quot;NotImplemented&quot; |
| BAD_GATEWAY | &quot;BadGateway&quot; |
| SERVICE_UNAVAILABLE | &quot;ServiceUnavailable&quot; |
| GATEWAY_TIMEOUT | &quot;GatewayTimeout&quot; |
| HTTP_VERSION_NOT_SUPPORTED | &quot;HttpVersionNotSupported&quot; |



