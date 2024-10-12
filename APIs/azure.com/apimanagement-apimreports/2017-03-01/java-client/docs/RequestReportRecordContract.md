

# RequestReportRecordContract

Request Report data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiId** | **String** | API identifier path. /apis/{apiId} |  [optional] |
|**apiRegion** | **String** | Azure region where the gateway that processed this request is located. |  [optional] |
|**apiTime** | **Double** | The total time it took to process this request. |  [optional] |
|**backendResponseCode** | **String** | The HTTP status code received by the gateway as a result of forwarding this request to the backend. |  [optional] |
|**cache** | **String** | Specifies if response cache was involved in generating the response. If the value is none, the cache was not used. If the value is hit, cached response was returned. If the value is miss, the cache was used but lookup resulted in a miss and request was fulfilled by the backend. |  [optional] |
|**ipAddress** | **String** | The client IP address associated with this request. |  [optional] |
|**method** | **String** | The HTTP method associated with this request.. |  [optional] |
|**operationId** | **String** | Operation identifier path. /apis/{apiId}/operations/{operationId} |  [optional] |
|**productId** | **String** | Product identifier path. /products/{productId} |  [optional] [readonly] |
|**requestId** | **String** | Request Identifier. |  [optional] |
|**requestSize** | **Integer** | The size of this request.. |  [optional] |
|**responseCode** | **Integer** | The HTTP status code returned by the gateway. |  [optional] |
|**responseSize** | **Integer** | The size of the response returned by the gateway. |  [optional] |
|**serviceTime** | **Double** | he time it took to forward this request to the backend and get the response back. |  [optional] |
|**subscriptionId** | **String** | Subscription identifier path. /subscriptions/{subscriptionId} |  [optional] |
|**timestamp** | **OffsetDateTime** | The date and time when this request was received by the gateway in ISO 8601 format. |  [optional] |
|**url** | **String** | The full URL associated with this request. |  [optional] |
|**userId** | **String** | User identifier path. /users/{userId} |  [optional] [readonly] |



