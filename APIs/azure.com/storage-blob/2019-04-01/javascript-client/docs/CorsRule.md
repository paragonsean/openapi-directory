# StorageManagementClient.CorsRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedHeaders** | **[String]** | Required if CorsRule element is present. A list of headers allowed to be part of the cross-origin request. | 
**allowedMethods** | **[String]** | Required if CorsRule element is present. A list of HTTP methods that are allowed to be executed by the origin. | 
**allowedOrigins** | **[String]** | Required if CorsRule element is present. A list of origin domains that will be allowed via CORS, or \&quot;*\&quot; to allow all domains | 
**exposedHeaders** | **[String]** | Required if CorsRule element is present. A list of response headers to expose to CORS clients. | 
**maxAgeInSeconds** | **Number** | Required if CorsRule element is present. The number of seconds that the client/browser should cache a preflight response. | 



## Enum: [AllowedMethodsEnum]


* `DELETE` (value: `"DELETE"`)

* `GET` (value: `"GET"`)

* `HEAD` (value: `"HEAD"`)

* `MERGE` (value: `"MERGE"`)

* `POST` (value: `"POST"`)

* `OPTIONS` (value: `"OPTIONS"`)

* `PUT` (value: `"PUT"`)




