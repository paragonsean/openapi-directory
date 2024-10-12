

# DomainCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aliases** | **List&lt;String&gt;** | A set of alternate names that this Domain may be referenced by. May start (&#39;*.&#39;) or end (&#39;.*&#39;) with a wildcard.  |  [optional] |
|**checksum** | **String** |  |  [optional] |
|**corsConfig** | [**CORSConfig**](CORSConfig.md) |  |  [optional] |
|**domainKey** | **String** |  |  [optional] |
|**forceHttps** | **Boolean** | If set to true, requests must use TLS. If a request is not using TLS, (as determined by the scheme or the presence of X-Forwarded-Proto header), a 301 redirect will be sent telling the client to use HTTPS.  |  [optional] |
|**gzipEnabled** | **Boolean** | Experimental: if set to true will enable gzip compression on data that passes trough this domain |  [optional] |
|**name** | **String** |  |  |
|**port** | **Integer** |  |  |
|**redirects** | [**List&lt;Redirect&gt;**](Redirect.md) |  |  [optional] |
|**sslConfig** | [**SSLConfig**](SSLConfig.md) |  |  [optional] |
|**zoneKey** | **String** |  |  |



