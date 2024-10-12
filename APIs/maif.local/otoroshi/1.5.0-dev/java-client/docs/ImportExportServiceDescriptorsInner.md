

# ImportExportServiceDescriptorsInner

An otoroshi service descriptor. Represent a forward HTTP call on a domain to another location with some optional api management mecanism

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canary** | [**Canary**](Canary.md) |  |  [optional] |
|**additionalHeaders** | **Map&lt;String, String&gt;** | Specify headers that will be added to each client request. Useful to add authentication |  [optional] |
|**api** | [**ExposedApi**](ExposedApi.md) |  |  [optional] |
|**authConfigRef** | **String** | A reference to a global auth module config |  [optional] |
|**buildMode** | **Boolean** | Display a construction page when a user try to use the service |  |
|**chaosConfig** | [**ChaosConfig**](ChaosConfig.md) |  |  [optional] |
|**clientConfig** | [**ClientConfig**](ClientConfig.md) |  |  [optional] |
|**clientValidatorRef** | **String** | A reference to validation authority |  [optional] |
|**cors** | [**CorsSettings**](CorsSettings.md) |  |  [optional] |
|**domain** | **String** | The domain on which the service is available. |  |
|**enabled** | **Boolean** | Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist |  |
|**enforceSecureCommunication** | **Boolean** | When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside |  |
|**env** | **String** | The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is &#39;foo&#39; and line is &#39;preprod&#39;, then the exposed service will be available at &#39;foo.preprod.mydomain&#39; |  |
|**forceHttps** | **Boolean** | Will force redirection to https:// if not present |  |
|**groups** | **List&lt;String&gt;** | Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group |  |
|**gzip** | [**Gzip**](Gzip.md) |  |  [optional] |
|**headersVerification** | **Map&lt;String, String&gt;** | Specify headers that will be verified after routing. |  [optional] |
|**healthCheck** | [**HealthCheck**](HealthCheck.md) |  |  [optional] |
|**id** | **UUID** | A unique random string to identify your service |  |
|**ipFiltering** | [**IpFiltering**](IpFiltering.md) |  |  [optional] |
|**jwtVerifier** | [**ImportExportServiceDescriptorsInnerJwtVerifier**](ImportExportServiceDescriptorsInnerJwtVerifier.md) |  |  [optional] |
|**localHost** | **String** | The host used localy, mainly localhost:xxxx |  [optional] |
|**localScheme** | **String** | The scheme used localy, mainly http |  [optional] |
|**maintenanceMode** | **Boolean** | Display a maintainance page when a user try to use the service |  |
|**matchingHeaders** | **Map&lt;String, String&gt;** | Specify headers that MUST be present on client request to route it. Useful to implement versioning |  [optional] |
|**matchingRoot** | **String** | The root path on which the service is available |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Just a bunch of random properties |  [optional] |
|**name** | **String** | The name of your service. Only for debug and human readability purposes |  |
|**overrideHost** | **Boolean** | Host header will be overriden with Host of the target |  [optional] |
|**privateApp** | **Boolean** | When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain |  |
|**privatePatterns** | **List&lt;String&gt;** | If you define a public pattern that is a little bit too much, you can make some of public URL private again |  [optional] |
|**publicPatterns** | **List&lt;String&gt;** | By default, every services are private only and you&#39;ll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use &#39;/.*&#39; |  [optional] |
|**redirectToLocal** | **Boolean** | If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests |  [optional] |
|**redirection** | [**RedirectionSettings**](RedirectionSettings.md) |  |  [optional] |
|**root** | **String** | Otoroshi will append this root to any target choosen. If the specified root is &#39;/api/foo&#39;, then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar |  |
|**secComExcludedPatterns** | **List&lt;String&gt;** | URI patterns excluded from secured communications |  [optional] |
|**secComSettings** | [**GlobalJwtVerifierAlgoSettings**](GlobalJwtVerifierAlgoSettings.md) |  |  [optional] |
|**sendOtoroshiHeadersBack** | **Boolean** | When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ... |  [optional] |
|**statsdConfig** | [**StatsdConfig**](StatsdConfig.md) |  |  [optional] |
|**subdomain** | **String** | The subdomain on which the service is available |  |
|**targets** | [**List&lt;Target&gt;**](Target.md) | The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures |  |
|**transformerRef** | **String** | A reference to a request transformer |  [optional] |
|**userFacing** | **Boolean** | The fact that this service will be seen by users and cannot be impacted by the Snow Monkey |  [optional] |
|**xForwardedHeaders** | **Boolean** | Send X-Forwarded-* headers |  [optional] |



