

# ReportsListByApi200ResponseValueInner

Report data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiId** | **String** | API identifier path. /apis/{apiId} |  [optional] |
|**apiRegion** | **String** | API region identifier. |  [optional] |
|**apiTimeAvg** | **Double** | Average time it took to process request. |  [optional] |
|**apiTimeMax** | **Double** | Maximum time it took to process request. |  [optional] |
|**apiTimeMin** | **Double** | Minimum time it took to process request. |  [optional] |
|**bandwidth** | **Long** | Bandwidth consumed. |  [optional] |
|**cacheHitCount** | **Integer** | Number of times when content was served from cache policy. |  [optional] |
|**cacheMissCount** | **Integer** | Number of times content was fetched from backend. |  [optional] |
|**callCountBlocked** | **Integer** | Number of calls blocked due to invalid credentials. This includes calls returning HttpStatusCode.Unauthorized and HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests |  [optional] |
|**callCountFailed** | **Integer** | Number of calls failed due to proxy or backend errors. This includes calls returning HttpStatusCode.BadRequest(400) and any Code between HttpStatusCode.InternalServerError (500) and 600 |  [optional] |
|**callCountOther** | **Integer** | Number of other calls. |  [optional] |
|**callCountSuccess** | **Integer** | Number of successful calls. This includes calls returning HttpStatusCode &lt;&#x3D; 301 and HttpStatusCode.NotModified and HttpStatusCode.TemporaryRedirect |  [optional] |
|**callCountTotal** | **Integer** | Total number of calls. |  [optional] |
|**country** | **String** | Country to which this record data is related. |  [optional] |
|**interval** | **String** | Length of aggregation period.  Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO 8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations). |  [optional] |
|**name** | **String** | Name depending on report endpoint specifies product, API, operation or developer name. |  [optional] |
|**operationId** | **String** | Operation identifier path. /apis/{apiId}/operations/{operationId} |  [optional] |
|**productId** | **String** | Product identifier path. /products/{productId} |  [optional] [readonly] |
|**region** | **String** | Country region to which this record data is related. |  [optional] |
|**serviceTimeAvg** | **Double** | Average time it took to process request on backend. |  [optional] |
|**serviceTimeMax** | **Double** | Maximum time it took to process request on backend. |  [optional] |
|**serviceTimeMin** | **Double** | Minimum time it took to process request on backend. |  [optional] |
|**subscriptionId** | **String** | Subscription identifier path. /subscriptions/{subscriptionId} |  [optional] |
|**timestamp** | **OffsetDateTime** | Start of aggregation period. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**userId** | **String** | User identifier path. /users/{userId} |  [optional] [readonly] |
|**zip** | **String** | Zip code to which this record data is related. |  [optional] |



