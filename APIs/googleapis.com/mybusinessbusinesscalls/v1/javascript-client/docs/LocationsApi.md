# MyBusinessBusinessCallsApi.LocationsApi

All URIs are relative to *https://mybusinessbusinesscalls.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessbusinesscallsLocationsBusinesscallsinsightsList**](LocationsApi.md#mybusinessbusinesscallsLocationsBusinesscallsinsightsList) | **GET** /v1/{parent}/businesscallsinsights | 
[**mybusinessbusinesscallsLocationsGetBusinesscallssettings**](LocationsApi.md#mybusinessbusinesscallsLocationsGetBusinesscallssettings) | **GET** /v1/{name} | 
[**mybusinessbusinesscallsLocationsUpdateBusinesscallssettings**](LocationsApi.md#mybusinessbusinesscallsLocationsUpdateBusinesscallssettings) | **PATCH** /v1/{name} | 



## mybusinessbusinesscallsLocationsBusinesscallsinsightsList

> ListBusinessCallsInsightsResponse mybusinessbusinesscallsLocationsBusinesscallsinsightsList(parent, opts)



Returns insights for Business calls for a location.

### Example

```javascript
import MyBusinessBusinessCallsApi from 'my_business_business_calls_api';

let apiInstance = new MyBusinessBusinessCallsApi.LocationsApi();
let parent = "parent_example"; // String | Required. The parent location to fetch calls insights for. Format: locations/{location_id}
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. A filter constraining the calls insights to return. The response includes only entries that match the filter. If the MetricType is not provided, AGGREGATE_COUNT is returned. If no end_date is provided, the last date for which data is available is used. If no start_date is provided, we will default to the first date for which data is available, which is currently 6 months. If start_date is before the date when data is available, data is returned starting from the date when it is available. At this time we support following filters. 1. start_date=\"DATE\" where date is in YYYY-MM-DD format. 2. end_date=\"DATE\" where date is in YYYY-MM-DD format. 3. metric_type=XYZ where XYZ is a valid MetricType. 4. Conjunctions(AND) of all of the above. e.g., \"start_date=2021-08-01 AND end_date=2021-08-10 AND metric_type=AGGREGATE_COUNT\" The AGGREGATE_COUNT metric_type ignores the DD part of the date.
  'pageSize': 56, // Number | Optional. The maximum number of BusinessCallsInsights to return. If unspecified, at most 20 will be returned. Some of the metric_types(e.g, AGGREGATE_COUNT) returns a single page. For these metrics, the page_size is ignored.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous `ListBusinessCallsInsights` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBusinessCallsInsights` must match the call that provided the page token. Some of the metric_types (e.g, AGGREGATE_COUNT) returns a single page. For these metrics, the pake_token is ignored.
};
apiInstance.mybusinessbusinesscallsLocationsBusinesscallsinsightsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent location to fetch calls insights for. Format: locations/{location_id} | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. A filter constraining the calls insights to return. The response includes only entries that match the filter. If the MetricType is not provided, AGGREGATE_COUNT is returned. If no end_date is provided, the last date for which data is available is used. If no start_date is provided, we will default to the first date for which data is available, which is currently 6 months. If start_date is before the date when data is available, data is returned starting from the date when it is available. At this time we support following filters. 1. start_date&#x3D;\&quot;DATE\&quot; where date is in YYYY-MM-DD format. 2. end_date&#x3D;\&quot;DATE\&quot; where date is in YYYY-MM-DD format. 3. metric_type&#x3D;XYZ where XYZ is a valid MetricType. 4. Conjunctions(AND) of all of the above. e.g., \&quot;start_date&#x3D;2021-08-01 AND end_date&#x3D;2021-08-10 AND metric_type&#x3D;AGGREGATE_COUNT\&quot; The AGGREGATE_COUNT metric_type ignores the DD part of the date. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of BusinessCallsInsights to return. If unspecified, at most 20 will be returned. Some of the metric_types(e.g, AGGREGATE_COUNT) returns a single page. For these metrics, the page_size is ignored. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListBusinessCallsInsights&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListBusinessCallsInsights&#x60; must match the call that provided the page token. Some of the metric_types (e.g, AGGREGATE_COUNT) returns a single page. For these metrics, the pake_token is ignored. | [optional] 

### Return type

[**ListBusinessCallsInsightsResponse**](ListBusinessCallsInsightsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinessbusinesscallsLocationsGetBusinesscallssettings

> BusinessCallsSettings mybusinessbusinesscallsLocationsGetBusinesscallssettings(name, opts)



Returns the Business calls settings resource for the given location.

### Example

```javascript
import MyBusinessBusinessCallsApi from 'my_business_business_calls_api';

let apiInstance = new MyBusinessBusinessCallsApi.LocationsApi();
let name = "name_example"; // String | Required. The BusinessCallsSettings to get. The `name` field is used to identify the business call settings to get. Format: locations/{location_id}/businesscallssettings.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.mybusinessbusinesscallsLocationsGetBusinesscallssettings(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The BusinessCallsSettings to get. The &#x60;name&#x60; field is used to identify the business call settings to get. Format: locations/{location_id}/businesscallssettings. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**BusinessCallsSettings**](BusinessCallsSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinessbusinesscallsLocationsUpdateBusinesscallssettings

> BusinessCallsSettings mybusinessbusinesscallsLocationsUpdateBusinesscallssettings(name, opts)



Updates the Business call settings for the specified location.

### Example

```javascript
import MyBusinessBusinessCallsApi from 'my_business_business_calls_api';

let apiInstance = new MyBusinessBusinessCallsApi.LocationsApi();
let name = "name_example"; // String | Required. The resource name of the calls settings. Format: locations/{location}/businesscallssettings
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateMask': "updateMask_example", // String | Required. The list of fields to update.
  'businessCallsSettings': new MyBusinessBusinessCallsApi.BusinessCallsSettings() // BusinessCallsSettings | 
};
apiInstance.mybusinessbusinesscallsLocationsUpdateBusinesscallssettings(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name of the calls settings. Format: locations/{location}/businesscallssettings | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateMask** | **String**| Required. The list of fields to update. | [optional] 
 **businessCallsSettings** | [**BusinessCallsSettings**](BusinessCallsSettings.md)|  | [optional] 

### Return type

[**BusinessCallsSettings**](BusinessCallsSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

