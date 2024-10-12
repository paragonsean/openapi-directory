

# GetOpenIDConfigResponse

GetOpenIDConfigResponse is an OIDC discovery document for the cluster. See the OpenID Connect Discovery 1.0 specification for details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cacheHeader** | [**HttpCacheControlResponseHeader**](HttpCacheControlResponseHeader.md) |  |  [optional] |
|**claimsSupported** | **List&lt;String&gt;** | Supported claims. |  [optional] |
|**grantTypes** | **List&lt;String&gt;** | Supported grant types. |  [optional] |
|**idTokenSigningAlgValuesSupported** | **List&lt;String&gt;** | supported ID Token signing Algorithms. |  [optional] |
|**issuer** | **String** | OIDC Issuer. |  [optional] |
|**jwksUri** | **String** | JSON Web Key uri. |  [optional] |
|**responseTypesSupported** | **List&lt;String&gt;** | Supported response types. |  [optional] |
|**subjectTypesSupported** | **List&lt;String&gt;** | Supported subject types. |  [optional] |



