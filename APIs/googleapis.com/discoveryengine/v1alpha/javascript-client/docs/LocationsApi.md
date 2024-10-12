# DiscoveryEngineApi.LocationsApi

All URIs are relative to *https://discoveryengine.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discoveryengineLocationsLookupWidgetConfig**](LocationsApi.md#discoveryengineLocationsLookupWidgetConfig) | **POST** /v1alpha/{location}/lookupWidgetConfig | 
[**discoveryengineLocationsWidgetCompleteQuery**](LocationsApi.md#discoveryengineLocationsWidgetCompleteQuery) | **POST** /v1alpha/{location}/widgetCompleteQuery | 
[**discoveryengineLocationsWidgetConverseConversation**](LocationsApi.md#discoveryengineLocationsWidgetConverseConversation) | **POST** /v1alpha/{location}/widgetConverseConversation | 
[**discoveryengineLocationsWidgetSearch**](LocationsApi.md#discoveryengineLocationsWidgetSearch) | **POST** /v1alpha/{location}/widgetSearch | 



## discoveryengineLocationsLookupWidgetConfig

> GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigResponse discoveryengineLocationsLookupWidgetConfig(location, opts)



Gets the Widget Config using the uuid.

### Example

```javascript
import DiscoveryEngineApi from 'discovery_engine_api';
let defaultClient = DiscoveryEngineApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiscoveryEngineApi.LocationsApi();
let location = "location_example"; // String | Required. The location resource where lookup widget will be performed. Format: `locations/{location}`
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
  'googleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest': new DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest() // GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest | 
};
apiInstance.discoveryengineLocationsLookupWidgetConfig(location, opts, (error, data, response) => {
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
 **location** | **String**| Required. The location resource where lookup widget will be performed. Format: &#x60;locations/{location}&#x60; | 
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
 **googleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest** | [**GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest**](GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigResponse**](GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## discoveryengineLocationsWidgetCompleteQuery

> GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryResponse discoveryengineLocationsWidgetCompleteQuery(location, opts)



Performs a user input completion with keyword suggestion. Similar to the CompletionService.CompleteQuery method, but a widget version that allows CompleteQuery without API Key. It supports CompleteQuery with or without JWT token.

### Example

```javascript
import DiscoveryEngineApi from 'discovery_engine_api';
let defaultClient = DiscoveryEngineApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiscoveryEngineApi.LocationsApi();
let location = "location_example"; // String | Required. The location resource where widget complete query will be performed. Format: `locations/{location}`
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
  'googleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest': new DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest() // GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest | 
};
apiInstance.discoveryengineLocationsWidgetCompleteQuery(location, opts, (error, data, response) => {
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
 **location** | **String**| Required. The location resource where widget complete query will be performed. Format: &#x60;locations/{location}&#x60; | 
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
 **googleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest** | [**GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest**](GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryResponse**](GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## discoveryengineLocationsWidgetConverseConversation

> GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationResponse discoveryengineLocationsWidgetConverseConversation(location, opts)



Converse a conversation with Widget.

### Example

```javascript
import DiscoveryEngineApi from 'discovery_engine_api';
let defaultClient = DiscoveryEngineApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiscoveryEngineApi.LocationsApi();
let location = "location_example"; // String | Required. The location resource where widget converse conversation will be performed. Format: `locations/{location}`
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
  'googleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest': new DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest() // GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest | 
};
apiInstance.discoveryengineLocationsWidgetConverseConversation(location, opts, (error, data, response) => {
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
 **location** | **String**| Required. The location resource where widget converse conversation will be performed. Format: &#x60;locations/{location}&#x60; | 
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
 **googleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest** | [**GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest**](GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationResponse**](GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## discoveryengineLocationsWidgetSearch

> GoogleCloudDiscoveryengineV1alphaWidgetSearchResponse discoveryengineLocationsWidgetSearch(location, opts)



Performs a search. Similar to the SearchService.Search method, but a widget version that allows search without API Key. It supports search with or without JWT token.

### Example

```javascript
import DiscoveryEngineApi from 'discovery_engine_api';
let defaultClient = DiscoveryEngineApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiscoveryEngineApi.LocationsApi();
let location = "location_example"; // String | Required. The location resource where widget search will be performed. Format: `locations/{location}`
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
  'googleCloudDiscoveryengineV1alphaWidgetSearchRequest': new DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaWidgetSearchRequest() // GoogleCloudDiscoveryengineV1alphaWidgetSearchRequest | 
};
apiInstance.discoveryengineLocationsWidgetSearch(location, opts, (error, data, response) => {
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
 **location** | **String**| Required. The location resource where widget search will be performed. Format: &#x60;locations/{location}&#x60; | 
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
 **googleCloudDiscoveryengineV1alphaWidgetSearchRequest** | [**GoogleCloudDiscoveryengineV1alphaWidgetSearchRequest**](GoogleCloudDiscoveryengineV1alphaWidgetSearchRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDiscoveryengineV1alphaWidgetSearchResponse**](GoogleCloudDiscoveryengineV1alphaWidgetSearchResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

