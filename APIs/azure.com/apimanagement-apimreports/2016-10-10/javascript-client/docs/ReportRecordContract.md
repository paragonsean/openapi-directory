# ApiManagementClient.ReportRecordContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiId** | **String** | API identifier path. /apis/{apiId} | [optional] 
**apiRegion** | **String** | API region identifier. | [optional] 
**apiTimeAvg** | **Number** | Average time it took to process request. | [optional] 
**apiTimeMax** | **Number** | Maximum time it took to process request. | [optional] 
**apiTimeMin** | **Number** | Minimum time it took to process request. | [optional] 
**bandwidth** | **Number** | Bandwidth consumed. | [optional] 
**cacheHitCount** | **Number** | Number of times when content was served from cache policy. | [optional] 
**cacheMissCount** | **Number** | Number of times content was fetched from backend. | [optional] 
**callCountBlocked** | **Number** | Number of calls blocked due to invalid credentials. This includes calls returning HttpStatusCode.Unauthorized and HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests | [optional] 
**callCountFailed** | **Number** | Number of calls failed due to proxy or backend errors. This includes calls returning HttpStatusCode.BadRequest(400) and any Code between HttpStatusCode.InternalServerError (500) and 600 | [optional] 
**callCountOther** | **Number** | Number of other calls. | [optional] 
**callCountSuccess** | **Number** | Number of successful calls. This includes calls returning HttpStatusCode &lt;&#x3D; 301 and HttpStatusCode.NotModified and HttpStatusCode.TemporaryRedirect | [optional] 
**callCountTotal** | **Number** | Total number of calls. | [optional] 
**country** | **String** | Country to which this record data is related. | [optional] 
**interval** | **Number** | Length of aggregation period. | [optional] 
**name** | **String** | Name depending on report endpoint specifies product, API, operation or developer name. | [optional] 
**operationId** | **String** | Operation identifier path. /apis/{apiId}/operations/{operationId} | [optional] 
**productId** | **String** | Product identifier path. /products/{productId} | [optional] [readonly] 
**region** | **String** | Country region to which this record data is related. | [optional] 
**serviceTimeAvg** | **Number** | Average time it took to process request on backend. | [optional] 
**serviceTimeMax** | **Number** | Maximum time it took to process request on backend. | [optional] 
**serviceTimeMin** | **Number** | Minimum time it took to process request on backend. | [optional] 
**subscriptionId** | **String** | Subscription identifier path. /subscriptions/{subscriptionId} | [optional] 
**timestamp** | **Date** | Start of aggregation period. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**userId** | **String** | User identifier path. /users/{userId} | [optional] [readonly] 
**zip** | **String** | Zip code to which this record data is related. | [optional] 


