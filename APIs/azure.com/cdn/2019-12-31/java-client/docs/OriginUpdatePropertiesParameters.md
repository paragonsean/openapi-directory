

# OriginUpdatePropertiesParameters

The JSON object that contains the properties of the origin.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Origin is enabled for load balancing or not |  [optional] |
|**hostName** | **String** | The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint. |  [optional] |
|**httpPort** | **Integer** | The value of the HTTP port. Must be between 1 and 65535. |  [optional] |
|**httpsPort** | **Integer** | The value of the HTTPS port. Must be between 1 and 65535. |  [optional] |
|**originHostHeader** | **String** | The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint |  [optional] |
|**priority** | **Integer** | Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5 |  [optional] |
|**weight** | **Integer** | Weight of the origin in given origin group for load balancing. Must be between 1 and 1000 |  [optional] |



