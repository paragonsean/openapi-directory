

# ResponseHeadersPolicySecurityHeadersConfig

A configuration for a set of security-related HTTP response headers. CloudFront adds these headers to HTTP responses that it sends for requests that match a cache behavior associated with this response headers policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**xsSProtection** | [**ResponseHeadersPolicySecurityHeadersConfigXSSProtection**](ResponseHeadersPolicySecurityHeadersConfigXSSProtection.md) |  |  [optional] |
|**frameOptions** | [**ResponseHeadersPolicySecurityHeadersConfigFrameOptions**](ResponseHeadersPolicySecurityHeadersConfigFrameOptions.md) |  |  [optional] |
|**referrerPolicy** | [**ResponseHeadersPolicySecurityHeadersConfigReferrerPolicy**](ResponseHeadersPolicySecurityHeadersConfigReferrerPolicy.md) |  |  [optional] |
|**contentSecurityPolicy** | [**ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy**](ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy.md) |  |  [optional] |
|**contentTypeOptions** | [**ResponseHeadersPolicySecurityHeadersConfigContentTypeOptions**](ResponseHeadersPolicySecurityHeadersConfigContentTypeOptions.md) |  |  [optional] |
|**strictTransportSecurity** | [**ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity**](ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity.md) |  |  [optional] |



