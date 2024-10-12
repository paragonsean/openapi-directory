# ClimateFieldViewPlatformApis.LayersApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4LayersAsAppliedActivityIdContentsGet**](LayersApi.md#v4LayersAsAppliedActivityIdContentsGet) | **GET** /v4/layers/asApplied/{activityId}/contents | Retrieve the raw application activity
[**v4LayersAsAppliedGet**](LayersApi.md#v4LayersAsAppliedGet) | **GET** /v4/layers/asApplied | Retrieve a list of application activities
[**v4LayersAsHarvestedActivityIdContentsGet**](LayersApi.md#v4LayersAsHarvestedActivityIdContentsGet) | **GET** /v4/layers/asHarvested/{activityId}/contents | Retrieve the raw harvest activity
[**v4LayersAsHarvestedGet**](LayersApi.md#v4LayersAsHarvestedGet) | **GET** /v4/layers/asHarvested | Retrieve a list of harvest activities
[**v4LayersAsPlantedActivityIdContentsGet**](LayersApi.md#v4LayersAsPlantedActivityIdContentsGet) | **GET** /v4/layers/asPlanted/{activityId}/contents | Retrieve the raw planting activity
[**v4LayersAsPlantedGet**](LayersApi.md#v4LayersAsPlantedGet) | **GET** /v4/layers/asPlanted | Retrieve a list of planting activities
[**v4LayersScoutingObservationsGet**](LayersApi.md#v4LayersScoutingObservationsGet) | **GET** /v4/layers/scoutingObservations | Retrieve a list of scouting observations
[**v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet**](LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId}/attachments/{attachmentId}/contents | Retrieve the binary contents of a scouting observation’s attachment.
[**v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet**](LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId}/attachments | Retrieve attachments associated with a given scouting observation.
[**v4LayersScoutingObservationsScoutingObservationIdGet**](LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId} | Retrieve individual scouting observation



## v4LayersAsAppliedActivityIdContentsGet

> ApplicationActivityContents v4LayersAsAppliedActivityIdContentsGet(accept, activityId, range)

Retrieve the raw application activity

Retrieve an individual application activity by id.  Ids are retrieved via the  /layers/asApplied route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let activityId = "activityId_example"; // String | Unique identifier of the Application Activity.
let range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
apiInstance.v4LayersAsAppliedActivityIdContentsGet(accept, activityId, range, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **activityId** | **String**| Unique identifier of the Application Activity. | 
 **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | 

### Return type

[**ApplicationActivityContents**](ApplicationActivityContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## v4LayersAsAppliedGet

> ApplicationActivities v4LayersAsAppliedGet(accept, opts)

Retrieve a list of application activities

Retrieve a list of application activities. The id in the response is used for  GET /v4/layers/asApplied/{activityId}/contents.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let opts = {
  'xNextToken': "xNextToken_example", // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
  'xLimit': 56, // Number | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
  'resourceOwnerId': "resourceOwnerId_example", // String | Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
  'occurredAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
  'occurredBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00") // Date | Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
};
apiInstance.v4LayersAsAppliedGet(accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] 
 **xLimit** | **Number**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] 
 **resourceOwnerId** | **String**| Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. | [optional] 
 **occurredAfter** | **Date**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 
 **occurredBefore** | **Date**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 
 **updatedAfter** | **Date**| Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. | [optional] 

### Return type

[**ApplicationActivities**](ApplicationActivities.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v4LayersAsHarvestedActivityIdContentsGet

> HarvestActivityContents v4LayersAsHarvestedActivityIdContentsGet(accept, activityId, range)

Retrieve the raw harvest activity

Retrieve an individual harvest activity by id.  Ids are retrieved via the  /layers/asHarvested route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let activityId = "activityId_example"; // String | Unique identifier of the Harvest Activity.
let range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
apiInstance.v4LayersAsHarvestedActivityIdContentsGet(accept, activityId, range, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **activityId** | **String**| Unique identifier of the Harvest Activity. | 
 **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | 

### Return type

[**HarvestActivityContents**](HarvestActivityContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## v4LayersAsHarvestedGet

> HarvestActivities v4LayersAsHarvestedGet(accept, opts)

Retrieve a list of harvest activities

Retrieve a list of harvest activities. The id in the response is used for  GET /v4/layers/asHarvested/{activityId}/contents.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let opts = {
  'xNextToken': "xNextToken_example", // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
  'xLimit': 56, // Number | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
  'resourceOwnerId': "resourceOwnerId_example", // String | Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
  'occurredAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
  'occurredBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00") // Date | Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
};
apiInstance.v4LayersAsHarvestedGet(accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] 
 **xLimit** | **Number**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] 
 **resourceOwnerId** | **String**| Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. | [optional] 
 **occurredAfter** | **Date**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 
 **occurredBefore** | **Date**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 
 **updatedAfter** | **Date**| Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. | [optional] 

### Return type

[**HarvestActivities**](HarvestActivities.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v4LayersAsPlantedActivityIdContentsGet

> PlantingActivityContents v4LayersAsPlantedActivityIdContentsGet(accept, activityId, range)

Retrieve the raw planting activity

Retrieve an individual planting activity by id.  Ids are retrieved via the  /layers/asPlanted route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).  The data is compressed using .zip format.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let activityId = "activityId_example"; // String | Unique identifier of the Planting Activity.
let range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
apiInstance.v4LayersAsPlantedActivityIdContentsGet(accept, activityId, range, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **activityId** | **String**| Unique identifier of the Planting Activity. | 
 **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | 

### Return type

[**PlantingActivityContents**](PlantingActivityContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## v4LayersAsPlantedGet

> PlantingActivities v4LayersAsPlantedGet(accept, opts)

Retrieve a list of planting activities

Retrieve a list of planting activities. The id in the response is used for  GET /v4/layers/asPlanted/{activityId}/contents.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let opts = {
  'xNextToken': "xNextToken_example", // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
  'xLimit': 56, // Number | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
  'resourceOwnerId': "resourceOwnerId_example", // String | Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
  'occurredAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
  'occurredBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00") // Date | Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
};
apiInstance.v4LayersAsPlantedGet(accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] 
 **xLimit** | **Number**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] 
 **resourceOwnerId** | **String**| Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. | [optional] 
 **occurredAfter** | **Date**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 
 **occurredBefore** | **Date**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 
 **updatedAfter** | **Date**| Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. | [optional] 

### Return type

[**PlantingActivities**](PlantingActivities.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v4LayersScoutingObservationsGet

> ScoutingObservations v4LayersScoutingObservationsGet(opts)

Retrieve a list of scouting observations

Retrieve a list of scouting observations created or updated by the user identified by the Authorization header.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let opts = {
  'xNextToken': "xNextToken_example", // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
  'xLimit': 56, // Number | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
  'occurredAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
  'occurredBefore': new Date("2013-10-20T19:20:30+01:00") // Date | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
};
apiInstance.v4LayersScoutingObservationsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] 
 **xLimit** | **Number**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] 
 **occurredAfter** | **Date**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 
 **occurredBefore** | **Date**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] 

### Return type

[**ScoutingObservations**](ScoutingObservations.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet

> ScoutingObservationAttachmentContents v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(accept, scoutingObservationId, attachmentId, range)

Retrieve the binary contents of a scouting observation’s attachment.

Photos added to scouting notes in the FieldView app are capped to &#x60;20MiB&#x60; (&#x60;20971520 bytes&#x60;), and we won’t store photos larger than that in a scouting note. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let scoutingObservationId = "scoutingObservationId_example"; // String | Unique identifier of the Scouting Observation.
let attachmentId = "attachmentId_example"; // String | Unique identifier of the attachment.
let range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
apiInstance.v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(accept, scoutingObservationId, attachmentId, range, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **scoutingObservationId** | **String**| Unique identifier of the Scouting Observation. | 
 **attachmentId** | **String**| Unique identifier of the attachment. | 
 **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | 

### Return type

[**ScoutingObservationAttachmentContents**](ScoutingObservationAttachmentContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/jpeg, image/png, application/json


## v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet

> ScoutingObservationAttachments v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(scoutingObservationId, opts)

Retrieve attachments associated with a given scouting observation.

Retrieve attachments associated with a given scouting observation. Photos added to scouting notes in the FieldView app are capped to 20MB, and we won’t store photos larger than that in a scouting note.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let scoutingObservationId = "scoutingObservationId_example"; // String | Unique identifier of the Scouting Observation.
let opts = {
  'xNextToken': "xNextToken_example", // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
  'xLimit': 56 // Number | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
};
apiInstance.v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(scoutingObservationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoutingObservationId** | **String**| Unique identifier of the Scouting Observation. | 
 **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] 
 **xLimit** | **Number**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] 

### Return type

[**ScoutingObservationAttachments**](ScoutingObservationAttachments.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v4LayersScoutingObservationsScoutingObservationIdGet

> ScoutingObservation v4LayersScoutingObservationsScoutingObservationIdGet(scoutingObservationId)

Retrieve individual scouting observation

Retrieve an individual scouting observation by id.  Ids are retrieved via the /layers/scoutingObservations route.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.LayersApi();
let scoutingObservationId = "scoutingObservationId_example"; // String | Unique identifier of the Scouting Observation.
apiInstance.v4LayersScoutingObservationsScoutingObservationIdGet(scoutingObservationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoutingObservationId** | **String**| Unique identifier of the Scouting Observation. | 

### Return type

[**ScoutingObservation**](ScoutingObservation.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

