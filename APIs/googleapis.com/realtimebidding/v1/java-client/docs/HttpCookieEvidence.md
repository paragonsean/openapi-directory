

# HttpCookieEvidence

Evidence for HTTP cookie-related policy violations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cookieNames** | **List&lt;String&gt;** | Names of cookies that violate Google policies. For TOO_MANY_COOKIES policy, this will be the cookie names of top domains with the largest number of cookies. For other policies, this will be all the cookie names that violate the policy. |  [optional] |
|**maxCookieCount** | **Integer** | The largest number of cookies set by a creative. If this field is set, cookie_names above will be set to the cookie names of top domains with the largest number of cookies. This field will only be set for TOO_MANY_COOKIES policy. |  [optional] |



