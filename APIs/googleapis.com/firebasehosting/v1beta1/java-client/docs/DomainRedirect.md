

# DomainRedirect

Defines the behavior of a domain-level redirect. Domain redirects preserve the path of the redirect but replace the requested domain with the one specified in the redirect configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | **String** | Required. The domain name to redirect to. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The redirect status code. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REDIRECT_TYPE_UNSPECIFIED | &quot;REDIRECT_TYPE_UNSPECIFIED&quot; |
| MOVED_PERMANENTLY | &quot;MOVED_PERMANENTLY&quot; |



