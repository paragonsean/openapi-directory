

# CorsRule

Specifies a CORS rule for the Blob service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedHeaders** | **List&lt;String&gt;** | Required if CorsRule element is present. A list of headers allowed to be part of the cross-origin request. |  |
|**allowedMethods** | [**List&lt;AllowedMethodsEnum&gt;**](#List&lt;AllowedMethodsEnum&gt;) | Required if CorsRule element is present. A list of HTTP methods that are allowed to be executed by the origin. |  |
|**allowedOrigins** | **List&lt;String&gt;** | Required if CorsRule element is present. A list of origin domains that will be allowed via CORS, or \&quot;*\&quot; to allow all domains |  |
|**exposedHeaders** | **List&lt;String&gt;** | Required if CorsRule element is present. A list of response headers to expose to CORS clients. |  |
|**maxAgeInSeconds** | **Integer** | Required if CorsRule element is present. The number of seconds that the client/browser should cache a preflight response. |  |



## Enum: List&lt;AllowedMethodsEnum&gt;

| Name | Value |
|---- | -----|
| DELETE | &quot;DELETE&quot; |
| GET | &quot;GET&quot; |
| HEAD | &quot;HEAD&quot; |
| MERGE | &quot;MERGE&quot; |
| POST | &quot;POST&quot; |
| OPTIONS | &quot;OPTIONS&quot; |
| PUT | &quot;PUT&quot; |



